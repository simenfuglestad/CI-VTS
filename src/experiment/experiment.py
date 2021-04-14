import json
import os
from datetime import datetime
import math
from PySide6.QtCore import *
import time
import timeit

_ex_dir = "experiment/experiment_profiles/"


class ExperimentRunner(QObject):
    signal_experiment_in_progress = Signal(bytes)

    def __init__(self, plot_data, serial_interface, duration, camera, recording_experiment, resolution=100, parent=None):
        super().__init__(parent)
        self.plot_data = plot_data
        self.serial_interface = serial_interface
        self.resolution = resolution
        self.recording_experiment = recording_experiment
        self.start_time = 0
        self.current_time = 0
        self.duration = duration
        self.timer = QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.setInterval(self.resolution/10)
        self.timer.timeout.connect(self.update)

        self.stim_vals = self.make_stim_vals()

        self.flag_done_plotting = True #use to signal turning stim led when all values are sent

        self.camera = camera

    def make_stim_vals(self):
        result = []
        for item in self.plot_data:
            r = self.make_stim_interval(item)
            result = result + r
        return result

    def make_stim_interval(self, item):
        start_val = item["value"][0]
        end_val = item["value"][1]

        start_time = item["time"][0]
        end_time = item["time"][1]
        run_time = end_time - start_time

        step_val = ((end_val - start_val) / run_time) / self.resolution  #1ms resolution
        val = start_val
        interval_vals = []
        for i in range(0, int(run_time)*self.resolution):
            interval_vals.append(val)
            val = val + step_val

        return interval_vals

    def run(self):
        self.flag_done_plotting = False
        if self.camera.capture_device is not None:
            if not self.camera.capture_device.isOpened():
                print("Capture device is not opened")
                return
        else:
            print("no capture device")
            return

        if len(self.stim_vals) > 0:
            self.start_time = time.perf_counter()
            if self.recording_experiment:
                self.camera.set_rec_mode()
            self.timer.start()
        else:
            print("no values to plot")

    def update(self):
        if len(self.stim_vals) > 0 and not self.flag_done_plotting:
            stim_val = self.stim_vals.pop(0)
            print(stim_val)
            self.serial_interface.send_data(stim_val, "sl")
            if len(self.stim_vals) == 0:
                self.flag_done_plotting = True
                self.serial_interface.send_data("sl", 0)

        self.current_time = time.perf_counter() - self.start_time
        if self.current_time >= self.duration:
            # self.camera.set_live_mode()
            self.timer.stop()
            if self.recording_experiment:
                self.camera.set_live_mode()
            print("timer stopped!")

            self.signal_experiment_in_progress.emit(False)

            self.serial_interface.send_data(0, "sl")
            

def get_ex_dir():
    return _ex_dir


def verify_or_create_ex_dir(func):
    try:
        if not os.path.isdir(_ex_dir):
            os.mkdir(_ex_dir)
        return func
    except Exception as e:
        print("Error when verifying experiment profile dir:")
        print(e)


@verify_or_create_ex_dir
def save_experiment_profile(stimulus_profile=None, experiment_settings=None, file_path=None, file_name=None, description=None, file_ext=".json"):
    try:
        if file_path is None:
            file_path = _ex_dir

        if file_name is None:
            print("kjbfsgsfgnkjbfgkdkfg")
            done = False
            index = 1
            file_name = "experiment_profile"
            while not done:
                if not os.path.isfile(_ex_dir + file_name + file_ext):
                    done = True
                else:
                    file_name = "experiment_profile" + str(index)
                    index = index + 1

        profile = {"name": file_name, "stimulus_profile": stimulus_profile,
                   "settings": experiment_settings, "description": description,
                   "date_created": str(datetime.now().date())}

        with open(file_path + file_name + file_ext, 'w') as f:
            json.dump(profile, f, ensure_ascii=False, indent=4)

        return profile

    except Exception as e:
        print("Error when saving experiment profile")
        print(e)


@verify_or_create_ex_dir
def load_experiment_profile(file_name, file_path=_ex_dir, extension=".json"):
    try:
        with open(file_path + file_name + extension, 'r') as f:
            r_data = json.load(f)
            return r_data
    except Exception as e:
        print("Error when loading experiment profile:")
        print(e)


@verify_or_create_ex_dir
def get_all_experiment_profile_names():
    names = []
    try:
        for p in os.listdir(_ex_dir):
            with open(_ex_dir + p, 'r') as f:
                names.append(json.load(f)["name"])
    except Exception as e:
        print("Error when getting experiment profile names")
        print(e)
    return names



