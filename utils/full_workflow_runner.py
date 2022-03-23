import argparse
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from utils.webdriver_initializer import ChromeDriverWrapper
from config.config_data import RarityConfig
import selenium.webdriver as webdriver

class EssentialsAutomationRunner(webdriver.Chrome):

    def __init__(self) -> None:
        self.bot = ChromeDriverWrapper()
        
        super().__init__(only_run_essentials=True)
       
        print(self.bot)

EssentialsAutomationRunner()