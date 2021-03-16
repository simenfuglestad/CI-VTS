import json
import os
from datetime import datetime

_ex_dir = "experiment/experiment_profiles/"


class Experiment(object):
    def __init__(self, stimulus_profile=None, exp_path=None, video_path=None, log_path=None):
        #General settings
        print("lksndf")
        self.duration = 0
        self.video_path = ""
        self.log_path = ""
        self.view_live = False
        self.view_infrared = False

        self.__stimulus_profile = stimulus_profile

        #Additional Settings
        self.dechorionated = False
        self.hatching_time = None

        self.genetics = False
        self.geno_type = None

        self.drugs = False
        self.drug_name = None

        self.crowd_size = 0

    def set_duration(self, hours, mins, secs):
        self.duration = hours * 60 * 60 + mins * 60 + secs

    def set_stimulus_profile(self):
        self.__stimulus_profile = []

    def get_experiment_settings(self):
        return {"duration" : self.duration, "video_path" : self.video_path, "log_path" : self.log_path,
                "view_live" : self.view_live, "view_infrared" : self.view_infrared, "dechorionated" : self.dechorionated,
                "hatching_time" : self.hatching_time, "genetics" : self.genetics, "geno_type" : self.geno_type,
                "drugs" : self.drugs, "drug_name" : self.drug_name, "crowd_size" : self.crowd_size}

    def get_stimulus_profile(self):
        return self.__stimulus_profile


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
def save_experiment_profile(experiment, file_name=None, description=None, file_ext=".json"):
    try:
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

        elif os.path.isfile(_ex_dir + file_name + file_ext):
            done = False
            index = 1
            tmp_file_name = file_name + str(index)
            while not done:
                if not os.path.isfile(_ex_dir + tmp_file_name + file_ext):
                    done = True
                    file_name = tmp_file_name
                else:
                    index = index + 1
                    tmp_file_name = file_name + str(index)

        experiment_settings = experiment.get_settings()
        experiment_stimulus_profile = experiment.get_stimulus_profile()

        profile = {"name" : file_name, "stimulus_profile" : experiment_stimulus_profile,
                   "settings" : experiment_settings, "description": description,
                   "date_created" : str(datetime.now().date())}

        with open(_ex_dir + file_name + file_ext, 'w') as f:
            json.dump(profile, f, ensure_ascii=False, indent=4)

        return profile

    except Exception as e:
        print("Error when saving experiment profile")
        print(e)


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



