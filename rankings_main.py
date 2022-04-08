import argparse
import sys
import time
from typing import List
from abc import abstractmethod, ABC
from utils.webdriver_initializer import FirefoxDriverWrapper

from config.config_data import RarityConfig
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#TODO PART1
#TODO Access Rarity Tools website 
class RarityWebsiteRunner(FirefoxDriverWrapper):
 
    webdriver_timeout = 240
 
    def __init__(self, args: List) -> None:
        self.collection = args.collection.replace(" ", "-").lower()
        self.id = args.id    
        self.rank = args.rank
        self.selling = args.selling
        super().__init__()
        super().driver(args.headless)
        print(self.collection, self.id, self.rank, self.selling, args.headless)
        # self.collection_url_rankings()
        self.get_ids_values()

    #Not needed checks just the main ids without entering for full values
    def collection_url_rankings(self):
        self.driver.get(RarityConfig.url + self.collection)
        time.sleep(2)
        if isinstance(self.id, list):
            for ids in self.id:
                self.driver.find_element(By.XPATH, self.Rarityconfig.enter_id).send_keys(ids)
                self.driver.find_element(By.XPATH, self.Rarityconfig.check_id).click()
        if isinstance(self.id, str):
            self.driver.find_element(By.XPATH, self.Rarityconfig.enter_id).send_keys(self.id)
            self.driver.find_element(By.XPATH, self.Rarityconfig.check_id).click()
        if self.rank is not None:
                self.driver.find_element(By.XPATH, self.Rarityconfig.from_rank).click()
                self.driver.find_element(By.XPATH, self.Rarityconfig.from_rank).send_keys(self.rank[0])
                self.driver.find_element(By.XPATH, self.Rarityconfig.to_rank).click()
                self.driver.find_element(By.XPATH, self.Rarityconfig.to_rank).send_keys(self.rank[1])
        if self.selling is not None:
                self.driver.find_element(By.XPATH, self.Rarityconfig.buy_now).click()

    def get_ids_values(self):
        if isinstance(self.id, list):
            for i in self.id:
                self.driver.implicitly_wait(2)
                self.check_id(i)
        if isinstance(self.id, str):
            self.check_id(self.id)
        if self.rank is not None:
            from_rank = int(self.rank[0])
            to_rank = int(self.rank[1])
            while from_rank <= to_rank:
                self.driver.implicitly_wait(2)
                self.check_id(str(from_rank))
                from_rank += 1

    def check_id(self, collection_id):
        self.driver.get(RarityConfig.url + self.collection + '/' + collection_id)
        print(self.driver.find_element(By.XPATH, self.Rarityconfig.rank_id).text)
        print("*"*10)
        print(self.driver.find_element(By.XPATH, self.Rarityconfig.rarity_score).text)
        print(self.driver.find_element(By.XPATH, self.Rarityconfig.owner).text)
        if self.selling is not None:
            try:
                print(self.driver.find_element(By.XPATH, self.Rarityconfig.listed).text)
            except NoSuchElementException:
                print("UNLISTED")
       
            
#TODO Save as JSON single as _ID_traits.json or list as _IDs_list.json    
def parse_args(args: List) -> argparse.Namespace:
    """ Parses arguments from console input. """
    parser = argparse.ArgumentParser()
    parser = RarityConfig.add_default_arguments_to_parser(parser)
    args = parser.parse_args()
    if not args.id and not args.rank:
            parser.error("One of --id, --ids or --rank must be given")
    return args



if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    #sys.argv 
    #choose collection and id or ids, option to buy now rank from and to and price

    #args_ = parse
    #factory = EssentialsWorkflowRunnerFactory() if args_.only_run_essentials else ManualWorkflowRunnerFactory()
    RarityWebsiteRunner(args)
    
