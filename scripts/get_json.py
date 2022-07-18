import json
class DumpNFTData:
    def __init__(self, collection: str, nft_id: int):
        self.collection = collection
        self.nft_id = nft_id
    
    def json_dump(self,**kwargs):
        print(self.collection)
        try: 
            self.check_if_file_exists(kwargs)
        except FileNotFoundError:
            self.if_not_exists_create(kwargs)
        finally:
            print(f"{self.collection.capitalize()} Nft ID of {self.nft_id} data has been dumped to .json file")
        
    def check_if_file_exists(self, kwargs):
         with open(f'./files/{self.collection}_data.json', 'r') as f:
                data = json.load(f)
         data.append(kwargs)
         with open(f'./files/{self.collection}_data.json', 'w') as f:
            json.dump(data, f)

    def if_not_exists_create(self, kwargs):
        entries = []
        with open(f'./files/{self.collection}_data.json', 'w') as f:
            json.dump(entries, f)
        with open(f'./files/{self.collection}_data.json', 'r') as f:
            data = json.load(f)
        data.append(kwargs)
        with open(f'./files/{self.collection}_data.json', 'w') as f:
            json.dump(data, f)