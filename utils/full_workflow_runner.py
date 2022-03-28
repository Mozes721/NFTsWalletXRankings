import argparse
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from utils.webdriver_initializer import FirefoxDriverWrapper
from config.config_data import RarityConfig
from selenium import webdriver

class EssentialsAutomationRunner(webdriver.Firefox):

    def __init__(self) -> None:
        self.bot = FirefoxDriverWrapper()
         
        print(self.bot)

