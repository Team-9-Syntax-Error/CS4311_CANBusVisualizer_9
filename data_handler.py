import os
import json
from data_object import DataObject


class DataHandler:
    os_char = '/'
    paths = {"Project Configuration": "config_data", "Node Data": "node_data"}
    current_proj_config = None
    current_node = None

    def __init__(self):
        if os.name == "nt":
            self.os_char = '\\'
        self.create_dirs()

    def get(self, data_type, key):
        data_object_pointer = None
        if data_type == "Project Configuration":
            data_object_pointer = self.current_proj_config
        if data_type == "Node Data":
            data_object_pointer = self.current_proj_config
        return data_object_pointer.get(key)

    def receive_data(self, data_type, dictionary):
        data_object = DataObject({data_type: dictionary})
        self.create_file(data_object)
        self.set_current_data_object(data_type, data_object.get_file_name())

    def set_current_data_object(self, data_type, file_name):
        data_object = self.load_from_file(data_type, file_name)
        if data_type == "Project Configuration":
            self.current_proj_config = data_object
        if data_type == "Node Data":
            self.current_node = data_object

    def load_from_file(self, data_type, file_name):
        path = self.create_path(data_type, file_name)
        f = open(path, "r")
        return DataObject(json.load(f))

    def create_file(self, data_object):
        json_object = json.dumps(data_object.get_data(), indent=4)

        f = open(self.create_path(data_object.get_type(), data_object.get_file_name()), "w")
        f.write(json_object)
        f.close()

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
