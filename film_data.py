from bs4 import BeautifulSoup
from urllib.request import urlopen

def get_film_data(link: str) -> None:
    page_url = link
    
    uClient = urlopen(page_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page_html, "html.parser")

    film_title = page_soup.find("h1", {"class":"headline-1"}).text
    film_year = page_soup.find("small", {"class":"number"}).a.text
    film_director = page_soup.find("span", {"class":"prettify"}).text
    film_overview = page_soup.find("div", {"class":"truncate"}).p.text

    print(film_title + " (" + film_year + ") directed by " + film_director)
    print(film_overview)
    print("")