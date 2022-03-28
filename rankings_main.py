import argparse
import sys
from typing import List
from abc import abstractmethod, ABC
from utils.full_workflow_runner import EssentialsAutomationRunner
from utils.webdriver_initializer import FirefoxDriverWrapper
from config.config_data import RarityConfig
from selenium import webdriver
#TODO PART1
#TODO Access Rarity Tools website 
class RarityWebsiteRunner(FirefoxDriverWrapper):
 
    def __init__(self, args: List) -> None:
        super().__init__()
        self.collection = args.collection
        self.id_ids_or_from_to = args.mode
        self.selling = args.selling
        print(self.collection, self.id_ids_or_from_to, self.selling)
        self.rarity_get_ranks()

    def rarity_get_ranks(self):
        self.driver.get(RarityConfig.url + self.collection)
        
#TODO Select single or multiple NFT collection IDs and their rankings 
#TODO If single select get individual full values 
#TODO Save as JSON single as _ID_traits.json or list as _IDs_list.json    
def parse_args(args: List) -> argparse.Namespace:
    """ Parses arguments from console input. """
    parser = argparse.ArgumentParser()
    parser = RarityConfig.add_default_arguments_to_parser(parser)
    args = parser.parse_args()
    if not args.mode:
            parser.error("One of --id, --ids or --rank must be given")
    return args

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    #sys.argv 
    #choose collection and id or ids, option to buy now rank from and to and price

    #args_ = parse
    #factory = EssentialsWorkflowRunnerFactory() if args_.only_run_essentials else ManualWorkflowRunnerFactory()
    RarityWebsiteRunner(args)
    