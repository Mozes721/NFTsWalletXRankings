import sys
import time
import argparse
from typing import Optional, Union, Any, Callable, Tuple, List
from config.config_data import RarityConfig, Other_Config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options


 
class FirefoxDriverWrapper(webdriver.Firefox):

    def __init__(self, download_dir: Optional[str] = "", local_test_mode: Optional[bool] = False) -> None:
        self.Rarityconfig = RarityConfig()
        # self.OSConfig = OSConfig()
        self.Otherconfig = Other_Config()
        self.firefox_options = self.set_firefox_options(local_test_mode=False)
        # self.wait = WebDriverWait(self.driver, 10)
         
    def driver(self, headless):
        self.driver = webdriver.Firefox(options=self.set_firefox_options(local_test_mode=headless))


    # def wait_until_webpage_fully_loaded(self, driver):
    #     """ Waits after the redirect happens to make sure that the full page is loaded """
    #     self.driver = driver
    #     WebDriverWait(self.driver, 2).until(
    #             EC.presence_of_element_located((By.XPATH, self.Rarityconfig.rank_id))
    #         )
        

    
    def set_firefox_options(self, local_test_mode: bool = False) -> webdriver.Chrome:
        firefox_options = Options()

        if local_test_mode:
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--no-sandbox')
            firefox_options.add_argument('--disable-dev-shm-usage')
        return firefox_options
