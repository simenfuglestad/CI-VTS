import json
import io


class Stimulus(object):
    def __init__(self):
        self.save_profile_to_file("a", "name.json")
        self.load_profile_from_file("name.json")

    def build_profile(self, name, data):
        pass

    def save_profile_to_file(self, profile, file_name, file_format="json"):
        data = json.dumps([{"some_index" : "some_data"}, "1"])
        with open("experiments/" + file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(data)

    def load_profile_from_file(self, file_name):
        with open("experiments/" + file_name, 'r') as f:
            r_data = json.load(f)
            print(json.loads(r_data)[0])

    def update_profile(self, data):
        pass
