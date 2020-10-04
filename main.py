from bs4 import BeautifulSoup
from urllib.request import urlopen

from film_data import get_film_data


def main() -> None:
    page_url = "https://letterboxd.com/films/"

    uClient = urlopen(page_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page_html, "html.parser")

    list_items = page_soup.find_all("li", {"class":"listitem"})
    
    for list_item in list_items:
        suffix = list_item.div["data-target-link"]
        link = "https://letterboxd.com" + suffix
        get_film_data(link)
    

if __name__ == "__main__":
    main()