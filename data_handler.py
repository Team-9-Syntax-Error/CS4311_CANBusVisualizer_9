import os
import json
from data_object import DataObject


class DataHandler:
    os_char = '/'
    paths = {"Project Configuration": "config_data"}
    current_proj_config = DataObject()

    def __init__(self):
        if os.name == "nt":
            self.os_char = '\\'
        self.create_dirs()

    def get_data(self, key):
        return self.current_proj_config.get_data(key)

    def receive_data(self, data_type, data):
        f_dict = {data_type: {}}
        for key in data:
            f_dict[data_type].update({key: data[key]})
        data_object = DataObject(f_dict, data_type)
        self.current_proj_config = data_object
        self.dump_to_file(data_object)

    def dump_to_file(self, data_object):
        json_object = data_object.get_json_data()

        f = open(self.create_path(data_object.get_data_type(), data_object.get_file_name()), "w")
        f.write(json_object)
        f.close()

    def set_current_proj(self, data_type, file_name):
        self.current_proj_config = self.load_from_file(data_type, file_name)

    def load_from_file(self, data_type, file_name):
        path = self.create_path(data_type, file_name)
        return json.load(path)

    def create_path(self, data_type, file_name):
        return "{}{}{}.json".format(self.paths[data_type], self.os_char, file_name)

    def create_dirs(self):
        for path in self.paths:
            if not os.path.exists(self.paths[path]):
                os.mkdir(self.paths[path])

    def path_de_traverse(self, path, levels=1):
        split_path = path.split(self.os_char)
        final_path = self.os_char.join(split_path[:-levels])
        if final_path == '':
            raise Exception("Path Out of Bounds")
        return final_path
