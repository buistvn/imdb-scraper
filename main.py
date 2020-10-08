from bs4 import BeautifulSoup
from urllib.request import urlopen

from film_data import FilmData


def main() -> None:
    page_url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

    uClient = urlopen(page_url)
    page_html = uClient.read()
    uClient.close()

    page_soup = BeautifulSoup(page_html, "html.parser")

    list_container = page_soup.find("tbody", {"class":"lister-list"})
    list_items = list_container.find_all("tr", limit=50)
    
    film_list = []

    for index, list_item in enumerate(list_items, start=1):
        suffix = list_item.td.a["href"]
        link = "https://www.imdb.com" + suffix

        film_title = list_item.find("td", {"class":"titleColumn"}).a.text
        film_year = list_item.find("td", {"class":"titleColumn"}).span.text.replace("(", "").replace(")", "")
        if (list_item.find("td", {"class":"ratingColumn"}).strong):
                film_rating = float(list_item.find("td", {"class":"ratingColumn"}).strong.text)
        else:
                film_rating = 0
        film_popularity = index
        film_link = link

        new_film = FilmData(film_title, film_year, film_rating, film_popularity, film_link)

        film_list.append(new_film)

    f = open("film_data.csv", "w")
    f.write("popularity,title,year,rating,link \n")
    
    print("(1) Sort by popularity")
    print("(2) Sort by title")
    print("(3) Sort by year")
    print("(4) Sort by rating")
    choice = input("How would you like to sort the data: ")

    if choice == "1":
        film_list.sort(key=lambda x: x.popularity, reverse=False)
    elif choice == "2":
        film_list.sort(key=lambda x: x.title, reverse=False)
    elif choice == "3":
        film_list.sort(key=lambda x: x.year, reverse=True)
    elif choice == "4":
        film_list.sort(key=lambda x: x.rating, reverse=True)
    else:
        print("Invalid input, please try again")

    for film in film_list:
        f.write(str(film.popularity) + "," + film.title + "," + film.year + "," + str(film.rating) + "," + film.link + "\n")
    
    f.close()
    

if __name__ == "__main__":
    main()