from os.path import isdir
from typing import List
import requests
from constants import Constants
from tqdm import tqdm
import math
import os

constants = Constants()


def clear_terminal():
    if os.name == "nt":
        os.system("cls")  # type: ignore
    if os.name == "posix":
        os.system("clear")


def download_file_with_progress(url, filename):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        total_size = int(response.headers.get("content-length", 0))
        print(total_size)
        progress_bar = tqdm(
            total=total_size, unit="B", unit_scale=True, desc=filename, ncols=100
        )
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    progress_bar.update(len(chunk))
        progress_bar.close()

        print(f"Downloaded '{filename}' successfully.")
    else:
        print(f"Failed to download '{filename}'. Status code: {response.status_code}")


def download_file(url, download_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(download_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded '{download_path}' successfully.")
    else:
        print(
            f"Failed to download '{download_path}'. Status code: {response.status_code}"
        )


def get_items_on_page(page, data):
    items_per_page: int = 10
    index = (page - 1) * items_per_page
    items_on_page = data[index : index + items_per_page]
    return items_on_page


def display_page(page: int, total_pages: int, data: List[str]) -> List[str]:
    items_on_page = get_items_on_page(page, data)
    for index, item in enumerate(items_on_page):
        print(f"\t{index + 1}. {item}")
    print(f"\nPage {page}/{total_pages}")
    return items_on_page


def choose_qari():
    qari_names: List[str] = list(constants.QARI_DATA.keys())
    qari_names_on_page = ""
    page = 1
    page_input = ""
    total_pages = math.ceil(len(qari_names) / 10)
    while page_input != "a":
        clear_terminal()
        print("Here is the list of Qari names:\n")
        qari_names_on_page = display_page(page, total_pages, qari_names)
        page_input = input("(A)ccept the page, (N)ext page, (P)revious page: ")
        if page_input == "n":
            page = min(page + 1, total_pages)
        elif page_input == "p":
            page = max(page - 1, 1)

    choice = int(input("Enter the number of the Qari you want to download: "))
    qari_name = qari_names_on_page[choice - 1]
    return (qari_name, constants.QARI_DATA[qari_name])


def download_surahs(surah_nums, download_url, download_path):
    for surah in surah_nums:
        if not os.path.isdir(download_path):
            os.mkdir(download_path)
        url = f"{download_url}{surah:03d}.mp3"
        arabic_name = constants.SURAH_DATA[surah]["simple"]
        english_name = constants.SURAH_DATA[surah]["english"].replace('"', "")
        surah_name = f"{surah:03d} - {arabic_name} ({english_name})"
        file_path = f"{download_path}/{surah_name}.mp3"
        print(f"Downloading: {url}")
        # download_file(url, file_path)
        download_file_with_progress(url, file_path)


def get_surah_nums() -> List[int]:
    all_surahs = input("Do you wish to download all surahs? (y/n): ")
    if all_surahs.lower() == "y":
        return list(range(1, 115))
    surah_nums = []
    print("Please enter the surah number you wish to download")
    print("for multiple surahs enter the numbers separated by spaces")
    print("for range of surahs enter the start and end separated by a dash")
    print("for example: 1 2 5-10 112. This will download surah 1 2 5 6 7 8 9 10 112")
    surah_nums_input = input("Enter the surah numbers: ").replace(",", " ")
    for entry in surah_nums_input.split():
        if entry.isdigit():
            surah_nums.append(int(entry))
        else:
            start_index = int(entry.split("-")[0])
            end_index = int(entry.split("-")[1])
            surah_nums.extend(range(start_index, end_index + 1))
    return surah_nums


def handle_recitations():
    qari_name, qari_url = choose_qari()
    clear_terminal()
    print(f"You have chosen: {qari_name}")
    confirmation = input(
        "Are you sure you want to download this Qari's recitations? (y/n): "
    )
    if not confirmation.lower() == "y":
        print("Aborted. Program now exiting...")
    qari_path = f"{constants.DOWNLOAD_PATH}/{qari_name}"
    url = f"{constants.QURANIC_AUDIO_DOWNLOAD_LINK}/{qari_url}"
    surah_nums = get_surah_nums()
    download_surahs(surah_nums, url, qari_path)


def main():
    clear_terminal()
    print("Welcome to the Quranic Audio Downloader!")
    print("Please pick what section of the application you want to download.")
    print("Here are the available sections:\n")
    print("\t1. Recitations")
    print("\t2. Recitations from Haramain Taraweeh")
    print("\t3. Non-Hafs Recitations")
    print("\t4. Recitations with Translation")
    section = int(input("\nEnter the number of the section you want to download: "))
    match section:
        case 1:
            handle_recitations()
        case _:
            print("Invalid section number. Please try again.")


if __name__ == "__main__":
    main()
