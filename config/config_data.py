import argparse
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class RarityConfig:
    url: str = "https://raritysniper.com/"
    table: str = '/html/body/div[1]/div[1]/section/div[4]'
    @staticmethod
    def add_default_arguments_to_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Enter NFT collection ID, IDs or from to rank example(10, 20) from selected collection. In addition can check if it's on sale")
        parser.add_argument("--collection", type=str, help="NFT collection you want to get", required=True)
        parser.add_argument('--id', type=str, help="Enter your NFT ID", dest='mode')
        parser.add_argument('--ids', type=str, help="Enter multiple NFT IDs", nargs='*', dest='mode')
        parser.add_argument('--rank', type=str, help="Choose from to ranks", nargs=2, dest='mode')
        parser.add_argument('--selling', help="Will display the collection ID or IDs IF they are on sale", nargs='?', const="&buyItNow=true")
        return parser

@dataclass
class OSConfig:
    url: str = "https://opensea.io/"

@dataclass
class Other_Config:
    chrome_path="/home/r.taujenis/Desktop/NFT/NFTsWalletXRankings/files/geckodriver"