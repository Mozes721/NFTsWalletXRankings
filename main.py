import argparse
import sys
import time
from typing import List
import pyperclip
from utils.webdriver_initializer import FirefoxDriverWrapper
from scripts.get_wallets_ETH import get_account_ballance
from scripts.get_json import DumpNFTData
from config.config_data import RarityConfig
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


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
        self.get_ids_values()

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
            self.driver.implicitly_wait(2)
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
        rank = FirefoxDriverWrapper.wait_until_content_recived(self.driver, self.Rarityconfig.rank_id)
        head_rank, sep, tail = rank.partition('\n')
        rarity_score = FirefoxDriverWrapper.wait_until_content_recived(self.driver, self.Rarityconfig.rarity_score)
        if self.selling is not None:
            try:
                price = FirefoxDriverWrapper.wait_until_content_recived(self.driver, self.Rarityconfig.listed)
                if price[2:] == "N/A":
                    price = "N/A"
                else:
                    price, sep, tail = price.partition('BUY')
                print(price)
            except NoSuchElementException:
                    price = "N/A"
        else:
            price = "N/R"
        owner_OS = FirefoxDriverWrapper.get_owner_OS(self.driver, self.Rarityconfig.owner_OS)
        print(head_rank, rarity_score,price, owner_OS)
        print("Itteration working")
        owner, eth, collected = self.OS_user(owner_OS)
        print(owner, eth, collected)
        print("Second itteration working")
        print("The id: %s rank: %s rarity score: %s owner: %s  market value %s overall collected: %s wallets ETH %s" % (collection_id, head_rank[5:], rarity_score[13:], owner, price, eth, collected))
        DumpNFTData.collection = self.collection
        DumpNFTData.json_dump(id=collection_id, rank_id=head_rank[5:], rarity_score=rarity_score[13:], owner=owner,price=price,collected=collected, eth=eth)

    def OS_user(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(3)
        owner = url[19:]
        #get address
        address = self.get_ETH_address(owner)
        #get ETH
        self.driver.implicitly_wait(3)
        print("waited")
        eth = get_account_ballance(address)
        print(eth)
        try:
            self.driver.implicitly_wait(2)
            collected = self.driver.find_element(By.XPATH, self.Rarityconfig.OS_Collected).text
        except:
            try:
                collected = self.driver.find_element(By.XPATH, self.Rarityconfig.OS_Collected_2).text
            except:
                collected = self.driver.find_element(By.XPATH, self.Rarityconfig.OS_Collected_3).text
        return owner, eth, collected

    def get_ETH_address(self, owner):
        if owner.startswith('0x') and len(owner) >= 20:
            eth_address = owner
            return eth_address
        else:
            try:
                eth_address = FirefoxDriverWrapper.wait_until_content_click(self.driver, self.Rarityconfig.OS_ETH_address)
            except:
                try:
                    eth_address = FirefoxDriverWrapper.wait_until_content_click(self.driver, self.Rarityconfig.OS_ETH_address_2)
                except:
                    eth_address = FirefoxDriverWrapper.wait_until_content_click(self.driver, self.Rarityconfig.OS_ETH_press)
                    eth_address = FirefoxDriverWrapper.wait_until_content_click(self.driver, self.Rarityconfig.OS_ETH_address_3)
            return eth_address


    
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
<<<<<<< HEAD
    RarityWebsiteRunner(args)
=======
    #sys.argv 
    #choose collection and id or ids, option to buy now rank from and to and price

    #args_ = parse
    #factory = EssentialsWorkflowRunnerFactory() if args_.only_run_essentials else ManualWorkflowRunnerFactory()
    RarityWebsiteRunner(args)
>>>>>>> 8d16d8231c004a8c236cac770a5ba753ee0c7abc
