import requests
import os
import json
from bs4 import BeautifulSoup
from pyquranic.exceptions import FailedToFetchURLException


class Constants:
    def __init__(self):
        self.QURANIC_AUDIO_LINK = "https://www.quranicaudio.com"
        # self.DOWNLOAD_PATH = "."
        self.DOWNLOAD_PATH = "/mnt/SSD_Storage/Audio/Quran"
        self.QURANIC_AUDIO_DOWNLOAD_LINK = "https://download.quranicaudio.com/quran"
        self.QURANIC_DATA_FILE_PATH = "quranic_audio_data.json"
        self.QURANIC_AUDIO_DATA = self.__get_data_from_file()
        self.QARI_DATA = self.__get_qari_data()
        self.SURAH_DATA = self.__get_surah_data()
        self.SECTIONS_DATA = {
            1: "Recitations",
            2: "Recitations from Haramain Taraweeh",
            3: "Non-Hafs Recitations",
            4: "Recitations with Translations",
        }

    def __get_surah_data(self):
        surah_data = {}
        surah_data_entries = self.QURANIC_AUDIO_DATA["surahs"]["entities"].items()
        for key, entry in surah_data_entries:
            name = entry["name"]
            simple = name["simple"]
            english = name["english"]
            surah_data[int(key)] = {"simple": simple, "english": english}
        return surah_data

    def __get_qari_data(self):
        qari_data = {}
        qari_data_entries = self.QURANIC_AUDIO_DATA["qaris"]["entities"].items()
        for _, entry in qari_data_entries:
            name = entry["name"]
            section_id = entry["sectionId"]
            relativePath = entry["relativePath"]
            if section_id == 1:
                qari_data[name] = relativePath
        return qari_data

    def __get_links(self):
        response = requests.get(self.QURANIC_AUDIO_LINK)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            links = soup.find_all("a")
            hrefs = [link.get("href") for link in links]
            cleaned_hrefs = [
                href for href in hrefs if href and not href.startswith("#")
            ]
            return cleaned_hrefs
        else:
            raise FailedToFetchURLException(
                f"Failed to fetch URL: {self.QURANIC_AUDIO_LINK}"
            )

    def __get_data_from_file(self):
        if not os.path.isfile(self.QURANIC_DATA_FILE_PATH):
            data = self.__get_data()
            with open(self.QURANIC_DATA_FILE_PATH, "w+") as json_f:
                if data:
                    json_f.write(data)
        with open(self.QURANIC_DATA_FILE_PATH, "r") as json_f:
            data = json.load(json_f)
        return data

    def __get_data(self):
        recieter_links = self.__get_links()
        response = requests.get(f"{self.QURANIC_AUDIO_LINK}/{recieter_links[0]}")
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            scripts = soup.find("script")
            if scripts:
                return scripts.text.split("window.__data=")[1][:-1]
        return None
