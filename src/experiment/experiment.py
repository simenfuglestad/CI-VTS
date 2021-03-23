import json
import os
from datetime import datetime
import math
from PySide6.QtCore import QRunnable
import time
import timeit

_ex_dir = "experiment/experiment_profiles/"

class ExperimentRunner(QRunnable):
    def __init__(self, plot_data, serial_interface, resolution=0.1, parent=None):
        super().__init__(parent)
        self.plot_data = plot_data
        self.serial_interface = serial_interface
        self.resolution = resolution

    def send_interval(self, item):
        start_val = item["value"][0]
        end_val = item["value"][1]

        start_time = item["time"][0]
        end_time = item["time"][1]
        run_time = end_time-start_time

        step_val = ((end_val - start_val)/run_time) / (1/self.resolution)

        time_passed = 0
        val = start_val
        while time_passed <= run_time:
            val = val + step_val
            if val > 100:
                val = 100
            elif val < 0.01:  # quick fix to appropriately set val to either 0 or 1, requires testing
                print(val)
                val = 0

            self.serial_interface.send_data(val, "sl")
            time.sleep(self.resolution)
            time_passed = time_passed + self.resolution

        # print(val)

    def run(self):
        for item in self.plot_data:
            self.send_interval(item)

        print("Experiment run completed")


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



