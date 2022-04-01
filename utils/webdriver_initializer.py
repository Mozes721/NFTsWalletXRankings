import sys
import time
import argparse
from typing import Optional, Union, Any, Callable, Tuple, List
from config.config_data import RarityConfig, OSConfig, Other_Config
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options



class FirefoxDriverWrapper(webdriver.Firefox):

    def __init__(self, download_dir: Optional[str] = "", local_test_mode: Optional[bool] = False) -> None:
        self.Rarityconfig = RarityConfig()
        self.OSconfig = OSConfig()
        self.Otherconfig = Other_Config()
        self.firefox_options = self.set_firefox_options(local_test_mode)
        self.driver = webdriver.Firefox()
        self.wait = WebDriverWait(self.driver, 10)
        
        
    def add_id(self, id):
        self.driver.find_element_by_xpath(self.Rarityconfig.enter_id).sendKeys(id)
        self.driver.find_element_by_xpath(self.Rarityconfig.check_id).click()

    def wait_until(self, expected_condition: EC,
                   ignored_exceptions: Optional[tuple] = None) -> WebElement:
        """ Explicitly waits until expected condition using selenium module functions for time specified
        in webdriver_timeout attribute and ignores exceptions passed to the input arg. Returns found element. """
        return WebDriverWait(self, self.webdriver_timeout, ignored_exceptions=ignored_exceptions) \
            .until(expected_condition)


    def _wait_until_webpage_fully_loaded(self, knox_id: str) -> None:
        """ Waits after the redirect happens to make sure that the full page is loaded """
        redirected_to_webpage_path = EC.url_contains(self.config.brs_main_url)
        self.wait_until(redirected_to_webpage_path)
        time.sleep(8)

    @staticmethod
    def set_firefox_options(local_test_mode: bool = False) -> webdriver.Chrome:
        firefox_options = Options()

        if not local_test_mode:
            firefox_options.add_argument('--headless')
            firefox_options.add_argument('--no-sandbox')
            firefox_options.add_argument('--disable-dev-shm-usage')
        return firefox_options
