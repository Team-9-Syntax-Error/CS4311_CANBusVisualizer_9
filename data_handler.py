import os
from data_object import DataObject


class DataHandler:
    os_char = '/'
    paths = {"Project Configuration": "config_data"}

    def __init__(self):
        if os.name == "nt":
            self.os_char = '\\'
        self.dir_creator()

    def receive_data(self, data_type, data):
        f_dict = {data_type: {}}
        for key in data:
            f_dict[data_type].update({key: data[key]})
        data_object = DataObject(f_dict, data_type)
        self.dump_to_file(data_object)

    def dump_to_file(self, data_object):
        json_object = data_object.get_json_data()

        f = open("{}{}{}.json".format(self.paths[data_object.get_data_type()], self.os_char, data_object.get_file_name()
                                      ), "w")
        f.write(json_object)
        f.close()

    def dir_creator(self):
        for path in self.paths:
            if not os.path.exists(self.paths[path]):
                os.mkdir(self.paths[path])
