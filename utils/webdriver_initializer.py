import sys
import time
import argparse
from typing import Optional, Union, Any, Callable, Tuple, List
from config.config_data import RarityConfig, OSConfig, Other_Config
import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ChromeDriverWrapper(webdriver.Chrome):

    webdriver_timeout = 240

    def __init__(self, download_dir: Optional[str] = "", local_test_mode: Optional[bool] = False) -> None:
        self.Rarityconfig = RarityConfig()
        self.OSconfig = OSConfig()
        self.Otherconfig = Other_Config()
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        options = self.set_chrome_options(local_test_mode)
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
        super().__init__(self.driver)
        

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
    def set_chrome_options(local_test_mode: bool = False) -> webdriver.Chrome:
        chrome_options = Options()
        chrome_options.binary_location = "/home/r.taujenis/.wdm/drivers/chromedriver/linux64/99.0.4844.51/chromedriver"
        if not local_test_mode:
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-gpu')
        return chrome_options
