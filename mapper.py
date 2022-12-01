import json


class Mapper():
    def __init__(self):
        self.map = []
        self.key = 0
        self.project_path = self.get_project_path()
    
    # Inserts new data into map.json
    def build_map(self):
        
        node_name = self.grab_nodes()

        # Can only pass if, if not None
        if node_name:
            data =  {"key":self.key , "name": node_name}
            self.map.append(data)
            self.insert_node()
            
    # Grabs name of the node
    def grab_nodes(self):
        print(self.project_path)

        with open(self.project_path + "/decoded_data_json.json") as f:
            node = json.load(f)
        print(node)

        for node_name in node[0].keys():
            print(node_name)
            if node_name not in self.map:
                return node_name
        return None

    def insert_node(self):
        with open(self.project_path + "/map.json", "w") as jsonFile:
                json.dump(self.map, jsonFile)

    def get_project_path(self):
        with open("Current_Working_Project.json", "r") as jsonFile:
                    data = json.load(jsonFile)
                    return data["Project_path"]

