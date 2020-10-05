from bs4 import BeautifulSoup
from urllib.request import urlopen

from film_data import FilmData


def scrape(link: str, index: int):
        uClient = urlopen(link)
        page_html = uClient.read()
        uClient.close()

        page_soup = BeautifulSoup(page_html, "html.parser")

        film_title = page_soup.find("h1").text
        film_title.replace("\uFFFD", " ")
        film_director = page_soup.find("div", {"class":"credit_summary_item"}).a.text
        film_overview = page_soup.find("div", {"class":"summary_text"}).text.strip()
        if (page_soup.find("span", {"itemprop":"ratingValue"})):
                film_rating = float(page_soup.find("span", {"itemprop":"ratingValue"}).text)
        else:
                film_rating = 0
        film_popularity = index

        film = FilmData(film_title, film_director, film_overview, film_rating, film_popularity)

        return film
