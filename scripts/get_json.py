import json
from json import encoder
encoder.FLOAT_REPR = lambda o: format(o, '.2f')

json_strings = {
                "RANK": 2,
                "ID": '#3491',
                "Rarity Score": 29452.70,
                "Wallet": 'shiruko',
                "Price": 'UNLISTED'
            }

with open('./files/ranking_data.json', 'r') as f:
    data = json.load(f)

data.append(json_strings)

with open('./files/ranking_data.json', 'w') as f:
    json.dump(data, f)