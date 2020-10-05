from bs4 import BeautifulSoup
from urllib.request import urlopen

from scrape import scrape


def main() -> None:
    page_url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

    uClient = urlopen(page_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page_html, "html.parser")

    list_container = page_soup.find("tbody", {"class":"lister-list"})
    list_items = list_container.find_all("tr", limit=10)
    
    film_list = []

    for index, list_item in enumerate(list_items, start=1):
        suffix = list_item.td.a["href"]
        link = "https://www.imdb.com" + suffix

        film_list.append(scrape(link, index))

    f = open("film_data.txt", "w")
    
    f.write("---------- SORTED BY POPULARITY ---------- \n \n")
    for film in film_list:
        f.write(film.title + "directed by " + film.director + "\n")
        f.write(film.overview + "\n")
        f.write("Average Rating: " + str(film.rating) + "\n")
        f.write("Popularity: " + str(film.popularity) + "\n")
        f.write("\n")

    film_list.sort(key=lambda x: x.rating, reverse=True)
    f.write("---------- SORTED BY AVERAGE RATING ---------- \n \n")
    for film in film_list:
        f.write(film.title + "directed by " + film.director + "\n")
        f.write(film.overview + "\n")
        f.write("Average Rating: " + str(film.rating) + "\n")
        f.write("Popularity: " + str(film.popularity) + "\n")
        f.write("\n")

    f.close()

if __name__ == "__main__":
    main()