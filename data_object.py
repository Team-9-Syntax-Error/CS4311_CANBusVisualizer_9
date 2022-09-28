import json


class DataObject:

    def __init__(self, data=None, data_type="Data Type Missing"):
        if data is None:
            data = {data_type: {"No Data": ""}}
        self.data_dict = data
        self.data_type = data_type
        self.file_name = self.find_name()

    def find_name(self):
        n_dict = self.data_dict[self.data_type]

        for key in n_dict:
            return n_dict[key]

    def get_data(self, key):
        return self.data_dict[self.data_type][key]

    def get_json_data(self):
        return json.dumps(self.data_dict, indent=4)

    def get_file_name(self):
        return self.file_name

    def get_data_type(self):
        return self.data_type

    """
    def get_value(self, key):
        temp_pointer = self.config_data
        return DataObject.recursive_get(key, temp_pointer)
    
    @staticmethod
    def recursive_get(key, d):
        value = 0
        if key in d:
            return d.get(key)
        for di in d:
            if type(d.get(di)) is dict:
                value = DataObject.recursive_get(key, d.get(di))
        return value
    """
