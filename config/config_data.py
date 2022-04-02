import argparse
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class RarityConfig:
    url: str = "https://raritysniper.com/"
    table: str = '/html/body/div[1]/div[1]/section/div[4]'
    enter_id: str = '/html/body/div[1]/div[1]/nav/div/div[3]/div[5]/div/div/form/input'
    check_id: str = '/html/body/div[1]/div[1]/nav/div/div[3]/div[5]/div/div/form/button'
    check_if_id_listed: str = '/html/body/div[1]/div[1]/section/div[3]/div[2]/div[2]/div[1]/span[1]/span'
    from_rank: str = '/html/body/div[1]/div[1]/nav/div/div[3]/div[12]/div/div[1]/input'
    to_rank: str = '/html/body/div[1]/div[1]/nav/div/div[3]/div[12]/div/div[2]/input'
    buy_now: str = '/html/body/div[1]/div[1]/nav/div/div[3]/div[7]/div/label'
    collection_table: str = '/html/body/div[1]/div[1]/section/div[4]'
    collection_ids: str = '/html/body/div[1]/div[1]/section/div[4]/div/div'

    @staticmethod
    def add_default_arguments_to_parser(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(description="Enter NFT collection ID, IDs or from to rank example(10, 20) from selected collection. In addition can check if it's on sale")
        parser.add_argument("--collection", type=str, help="NFT collection you want to get", required=True)
        parser.add_argument('--id', type=str, help="Enter your NFT ID", dest='id')
        parser.add_argument('--ids', type=str, help="Enter multiple NFT IDs", nargs='*', dest='id')
        parser.add_argument('--rank', type=str, help="Choose from to ranks", nargs=2, dest='rank')
        parser.add_argument('--selling', help="Will display the collection ID or IDs IF they are on sale", nargs='?', const="&buyItNow=true")
        parser.add_argument('--headless', help="Will run without webbrowser opening", dest='headless', action='store_true')
        return parser

@dataclass
class OSConfig:
    url: str = "https://opensea.io/"

@dataclass
class Other_Config:
    chrome_path="/home/r.taujenis/Desktop/NFT/NFTsWalletXRankings/files/geckodriver"