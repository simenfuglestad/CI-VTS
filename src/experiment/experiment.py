import json
import os
from datetime import datetime
import math
from PySide6.QtCore import *
import time
import timeit
"""
Module providing a class for handling running experiments as well as a few helper functions for dealing with
saving and loading of experiment profiles.
"""
_ex_dir = "experiment/experiment_profiles/"


class ExperimentRunner(QObject):
    """
    Provides functionality for conducting an experiment.
    This class should be instantiated once per run and destroyed subsequently.

    Attributes
    ----------
    signal_experiment_in_progress:
        Qt signal object, emits boolean indicating if experiment is in progress
    signal_experiment_done:
        Qt signal object, emits boolean when experiment is done
    signal_updating;
        Qt signal object, emits boolean indicating an update. Useful for trakcing progress
    """
    signal_experiment_in_progress = Signal(bytes)
    signal_experiment_done = Signal(bytes)
    signal_updating = Signal(bytes)

    def __init__(self, plot_data, serial_interface, duration, camera, recording_experiment, resolution=100):
        """
        Instantiate a ExperimentRunner and perform preparation for running.
        :param plot_data: stimulus data gathered from plot
        :param serial_interface: serial interface to send stimulus values with
        :param duration: experiment duraion in seconds
        :param camera: camera instance
        :param recording_experiment: bool indicating if recording
        :param resolution: int timer resolution
        """
        super().__init__()
        self.plot_data = plot_data
        self.serial_interface = serial_interface
        self.resolution = resolution
        self.recording_experiment = recording_experiment
        self.start_time = 0
        self.current_time = 0
        self.duration = duration
        self.timer = QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.setInterval(self.resolution/10) #update every 10ms
        self.timer.timeout.connect(self.update)

        self.stim_vals = self.make_stim_vals()

        self.flag_done_plotting = True  # use to signal turning stim led when all values are sent
        self.abort_flag = False  # use to signal experiment aborted

        self.camera = camera

    def make_stim_vals(self):
        """
        Unpacks all intervals, compute intermediary values and collects into single list
        :return: list of stimulus values
        """
        result = []
        for item in self.plot_data:
            r = self.make_stim_interval(item)
            result = result + r
        return result

    def make_stim_interval(self, item):
        """
        'Fills in the gap' of stimulus intervals by computing the intermediary values. This ensures that increasing or
        decreasing the stimulus over a time interval results in a gradual change, as opposed to sudden step.
        :param item: stimulus interval
        :return: list of stimulus value integers
        """
        start_val = item["value"][0]
        end_val = item["value"][1]

        start_time = item["time"][0]
        end_time = item["time"][1]
        run_time = end_time - start_time

        step_val = ((end_val - start_val) / run_time) / self.resolution  # 1ms resolution
        val = start_val
        interval_vals = []
        for i in range(0, int(run_time) * self.resolution):
            interval_vals.append(val)
            val = val + step_val

        return interval_vals

    def run(self):
        """
        Begin an experiment run by starting the timer.
        Note that this run method uses the Qt event loop: A timer deals with emitting precomputed signals at correct
        intervals.
        :return: None
        """
        self.flag_done_plotting = False
        self.abort_flag = False
        self.signal_experiment_in_progress.emit(True)
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
        """
        Event fired by the timer, runs at every time interval specified.
        Sends the next stimulus value to the serial interface until all values are sent or time runs out
        :return: None
        """
        self.signal_updating.emit(True)
        if len(self.stim_vals) > 0 and not self.flag_done_plotting:
            stim_val = self.stim_vals.pop(0)
            self.serial_interface.send_data(stim_val, "sl")
            if len(self.stim_vals) == 0:
                self.flag_done_plotting = True
                time.sleep(0.01)  # wait for port to be available during next send operation
                self.serial_interface.send_data(0, "sl")

        self.current_time = time.perf_counter() - self.start_time
        if self.abort_flag:
            self.timer.stop()
            self.signal_experiment_in_progress.emit(False)
            if self.recording_experiment:
                self.camera.set_live_mode()

        elif self.current_time >= self.duration:
            self.timer.stop()
            if self.recording_experiment:
                self.camera.set_live_mode()

            self.signal_experiment_in_progress.emit(False)
            self.signal_experiment_done.emit(True)


def get_ex_dir():
    """
    :return: path to experiments folder
    """
    return _ex_dir


def verify_or_create_ex_dir(func):
    """
    wrapper function to verify that experiment folder exists, create new if it does not
    :param func: function to wrap around
    :return: function to wrap around
    """
    try:
        if not os.path.isdir(_ex_dir):
            os.mkdir(_ex_dir)
        return func
    except Exception as e:
        print("Error when verifying experiment profile dir:")
        print(e)


@verify_or_create_ex_dir
def save_experiment_profile(stimulus_profile=None, experiment_settings=None, file_path=None, file_name=None,
                            description=None, file_ext=".json"):
    """
    Save a new experiment profile to the user's machine.

    :param stimulus_profile: full data set of a stimulus profile
    :param experiment_settings: dictionary of all experiment settings
    :param file_path: str path to save to
    :param file_name: str name to save as
    :param description: str optional description
    :param file_ext: str file extension, recommend using .json
    :return: fulle data set of new experiment profile
    """
    try:
        if file_path is None:
            file_path = _ex_dir

        if file_name is None:
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
    """
    Load data from a experiment profile
    :param file_name: name of file experiment profile is saved in
    :param file_path: name of path experiment profile is saved in
    :param extension: file extension of profile
    :return: data contained in the experiment profile
    """
    try:
        with open(file_path + file_name + extension, 'r') as f:
            r_data = json.load(f)
            return r_data
    except Exception as e:
        print("Error when loading experiment profile:")
        print(e)


@verify_or_create_ex_dir
def get_all_experiment_profile_names():
    """
    Get a list of the all the experiment profiles in the current experiment profile folder
    :return: list of string with experiment profile names
    """
    names = []
    try:
        for p in os.listdir(_ex_dir):
            with open(_ex_dir + p, 'r') as f:
                names.append(json.load(f)["name"])
    except Exception as e:
        print("Error when getting experiment profile names")
        print(e)
    return names
