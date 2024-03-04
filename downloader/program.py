from typing import List
from constants import Constants
import math

constants = Constants()


def display_page(page: int, data: List[str]) -> None:
    items_per_page: int = 10
    print(data[0:items_per_page])


def display_qari_names():
    qari_names: List[str] = list(constants.QARI_DATA.keys())
    display_page(1, qari_names)


def main():
    display_qari_names()


if __name__ == "__main__":
    main()
