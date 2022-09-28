import json
import os.path


# Author: Mark-Anthony Avila
# Notes: Will add comments later, some of these functions will be thrown into a more generic file class for opening and writing later
class ConfigHandler:
    config_data = None
    os_char = "/"

    def __init__(self):
        if os.name == "nt":
            os_char = "\\"

    def receive_config_data(self, data):
        f_dict = {"Project Configuration": {}}
        for key in data:
            f_dict["Project Configuration"].update({key: data[key]})
        self.config_data = f_dict
        self.dump_to_file()

    def dump_to_file(self):
        json_object = json.dumps(self.config_data, indent=1)

        ConfigHandler.make_dir("config_data")
        f = open("config_data{}{}.json".format(self.os_char, self.get("project_name")), "w")
        f.write(json_object)
        f.close()

    def get(self, key):
        temp_pointer = self.config_data
        return ConfigHandler.recursive_get(key, temp_pointer)

    def path_back(self, path, levels=1):
        split_path = path.split(self.os_char)
        final_path = self.os_char.join(split_path[:-levels])
        if final_path == '':
            raise Exception("Path Out of Bounds")
        return final_path

    @staticmethod
    def make_dir(path):
        if not os.path.exists(path):
            os.mkdir(path)

    @staticmethod
    def recursive_get(key, d):
        value = 0
        if key in d:
            return d.get(key)
        for di in d:
            if type(d.get(di)) is dict:
                value = ConfigHandler.recursive_get(key, d.get(di))
        return value
