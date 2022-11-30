import json



class mapper:
    def __init__(self):
        self.map = []
        self.key = 0
    
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
        f = open("decoded_data_json.json")
        node = json.loads(f)

        for node_name in node.keys():
            if node_name not in self.map:
                return node_name
        return None

    def insert_node(self):
        with open("CS4311_CANBusVisualizer_9/map.json", "w") as jsonFile:
                json.dump(self.map, jsonFile)
