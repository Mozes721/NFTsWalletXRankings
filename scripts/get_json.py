import json
from json import encoder
from config.config_data import RarityConfig

class DumpNFTData():
    global collection
    collection = ''
    
    def json_dump(**kwargs):
        with open('./files/data.json', 'r') as f:
            data = json.load(f)
        data.append(kwargs)
        with open('./files/data.json', 'w') as f:
            json.dump(data, f)
        print(collection)