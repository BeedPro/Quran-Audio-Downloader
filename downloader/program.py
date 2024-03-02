import requests
from bs4 import BeautifulSoup


class FailedToFetchURLException(Exception):
    pass


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


if __name__ == "__main__":
    website_url = "https://www.quranicaudio.com/"
    links = get_links(website_url)
    for link in links:
        print(link)
