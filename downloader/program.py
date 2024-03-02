import requests
from bs4 import BeautifulSoup
from exceptions import FailedToFetchURLException

QURANIC_AUDIO_LINK = "https://www.quranicaudio.com/"


def get_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        links = soup.find_all("a")
        hrefs = [link.get("href") for link in links]
        cleaned_hrefs = [href for href in hrefs if href and not href.startswith("#")]
        return cleaned_hrefs
    else:
        raise FailedToFetchURLException(f"Failed to fetch URL: {url}")


def main():
    recieter_links = get_links(QURANIC_AUDIO_LINK)
    for link in recieter_links:
        print(link)


if __name__ == "__main__":
    main()
