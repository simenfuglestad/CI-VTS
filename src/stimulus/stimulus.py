import json
import os
from datetime import datetime

_sp_dir = "stimulus/stimulus_profiles/"


def get_sp_dir():
    return _sp_dir


def verify_or_create_sp_dir(func):
    try:
        if not os.path.isdir(_sp_dir):
            os.mkdir(_sp_dir)
        return func
    except Exception as e:
        print("Error verifying stimulus profile dir:")
        print(e)


def save_stimulus_profile(profile, path=_sp_dir):
    try:
        with open(path + profile["name"] + profile["extension"], 'w') as f:
            json.dump(profile, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print("Error when saving stimulus profile")
        print(e)


@verify_or_create_sp_dir
def make_stimulus_profile(data, file_name=None, description=None, file_ext=".json"):
    try:
        if file_name is None:
            done = False
            index = 1
            file_name = "stimulus_profile"
            while not done:
                if not os.path.isfile(_sp_dir + file_name + file_ext):
                    done = True
                else:
                    file_name = "stimulus_profile" + str(index)
                    index = index + 1

        # elif os.path.isfile(_sp_dir + file_name + file_ext):
        #     done = False
        #     index = 1
        #     tmp_file_name = file_name + str(index)
        #     while not done:
        #         if not os.path.isfile(_sp_dir + tmp_file_name + file_ext):
        #             done = True
        #             file_name = tmp_file_name
        #         else:
        #             index = index + 1
        #             tmp_file_name = file_name + str(index)

        profile = {"name": file_name, "description": description, "date_created": str(datetime.now().date()),
                   "data": data, "extension": file_ext}

        return profile

    except Exception as e:
        print("Error when making stimulus profile:")
        print(e)
        return False


@verify_or_create_sp_dir
def load_stimulus_profile(file_name, file_path=_sp_dir, extension=".json"):
    try:
        with open(file_path + file_name + extension, 'r') as f:
            r_data = json.load(f)
            return r_data
    except Exception as e:
        print("Error when loading stimulus profile:")
        print(e)


@verify_or_create_sp_dir
def get_all_stimulus_profile_names():
    names = []
    try:
        for p in os.listdir(_sp_dir):
            with open(_sp_dir + p, 'r') as f:
                names.append(json.load(f)["name"])
    except Exception as e:
        print("Error when getting stimulus profile names:")
        print(e)
    return names


def delete_stimulus_profile(name, ext=".json"):
    try:
        if name is not None:
            os.remove(_sp_dir + name + ext)
            return True
    except Exception as e:
        print("An error occurred when deleting stimulus profile:")
        print(e)
        return False
