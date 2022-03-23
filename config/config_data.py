import argparse
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class RarityConfig:
    url: str = "https://raritysniper.com/"
    title_test: str = '//*[@id="wrap"]/div[1]/section/div[1]/div[2]/div/div[1]/h1'
    

@dataclass
class OSConfig:
    url: str = "https://opensea.io/"

@dataclass
class Other_Config:
    chrome_path="/home/r.taujenis/Desktop/NFT/NFTsWalletXRankings/files/geckodriver"