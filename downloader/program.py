from typing import List
from constants import Constants
import math
import os

constants = Constants()


def clear_terminal():
    if os.name == "nt":
        os.system("cls")  # type: ignore
    if os.name == "posix":
        os.system("clear")


def display_page(page: int, total_pages: int, data: List[str]) -> None:
    items_per_page: int = 10
    index = (page - 1) * items_per_page
    items_on_page = data[index : index + items_per_page]
    for index, item in enumerate(items_on_page):
        print(f"\t{index + 1}. {item}")
    print(f"\nPage {page}/{total_pages}")


def display_qari_names():
    qari_names: List[str] = list(constants.QARI_DATA.keys())
    page = 1
    total_pages = math.ceil(len(qari_names) / 10)
    page_input = ""
    while page_input.lower() != "a":
        clear_terminal()
        print("This is the list of Qari names:\n")
        display_page(page, total_pages, qari_names)
        page_input = input("(N)ext, (P)revious, or (E)nter: ")
        match page_input.lower():
            case "n":
                page = min(page + 1, total_pages)
            case "p":
                page = max(page - 1, 1)
            case "e":
                qari_name = input("Enter the name of the Qari: ")
                print(constants.QARI_DATA[qari_name])
                input("Press Enter to continue...")


def main():
    display_qari_names()


if __name__ == "__main__":
    main()
