import argparse
from ast import parse
import sys
from typing import List
from abc import abstractmethod, ABC
from utils.full_workflow_runner import EssentialsAutomationRunner



#TODO PART2
#TODO Access OpenSea website
class OSWebsiteRunner():

    running = EssentialsAutomationRunner()
#TODO Check _ID_traits.json or _IDs_list.json for wallets 
#TODO On default get the users ETH amount on Etherscan to know if user is a whale investor
#TODO Create *user_ETH.json or list_ETH.json 
#TODO Add additional argparser for owner whole collection save in excel 


if __name__ == '__main__':
    #sys.argv 
    #choose collection and id or ids, option to buy now rank from and to and price

    #args_ = parse
    #factory = EssentialsWorkflowRunnerFactory() if args_.only_run_essentials else ManualWorkflowRunnerFactory()
    RarityWebsiteRunner()
    