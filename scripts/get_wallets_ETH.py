from requests import get
from config.config_data import Other_Config

def make_api_url(address):
    API = Other_Config.EtherScanAPI
    url = Other_Config.BaseURL +f"?module=account&action=balance&address={address}&tag=latest&apikey={API}"
    return url

def get_account_ballance(address):
    get_balance_url = make_api_url(address)
    response = get(get_balance_url)
    data = response.json()
    print("#"*20)
    value = int(float(data["result"])) / Other_Config.ETH_VALUE
    return value

