from audioop import add
import sys
import time
import argparse
import pyperclip
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

    @staticmethod
    def wait_until_content_recived(driver, xpath):
        """ Waits until content has been recived """
        return WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            ).text

    @staticmethod
    def get_owner_OS(driver, xpath):
        """ Waits until owner for OS has been recived """
        return WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            ).get_attribute('href')
    @staticmethod
    def wait_until_content_click(driver, xpath):
        """ Waits until content has been clicked """
        element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
        element.click()
        address = pyperclip.paste()
        return address


    
    def set_firefox_options(self, local_test_mode: bool = False) -> webdriver.Chrome:
        firefox_options = Options()

        if local_test_mode:
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--no-sandbox')
            firefox_options.add_argument('--disable-dev-shm-usage')
        return firefox_options
