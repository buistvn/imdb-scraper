import mysql.connector
from bs4 import BeautifulSoup
from urllib.request import urlopen

from film_data import FilmData

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123password",
    database="filmdb"
)

mycursor = mydb.cursor()

def main() -> None:
    mycursor.execute("DROP TABLE IF EXISTS films")
    mycursor.execute("CREATE TABLE films (popularity INTEGER(10), title VARCHAR(255), year INTEGER(10), rating FLOAT(10), link VARCHAR(255))")

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

        mycursor.execute("INSERT INTO films (popularity, title, year, rating, link) VALUES (%s, %s, %s, %s, %s)", (film_popularity, film_title, film_year, film_rating, film_link))

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
        mycursor.execute("ALTER TABLE films ORDER BY popularity")
        film_list.sort(key=lambda x: x.popularity, reverse=False)
    elif choice == "2":
        mycursor.execute("ALTER TABLE films ORDER BY title")
        film_list.sort(key=lambda x: x.title, reverse=False)
    elif choice == "3":
        mycursor.execute("ALTER TABLE films ORDER BY year DESC")
        film_list.sort(key=lambda x: x.year, reverse=True)
    elif choice == "4":
        mycursor.execute("ALTER TABLE films ORDER BY rating DESC")
        film_list.sort(key=lambda x: x.rating, reverse=True)
    else:
        print("Invalid input, please try again")

    mydb.commit()

    for film in film_list:
        f.write(str(film.popularity) + "," + film.title + "," + film.year + "," + str(film.rating) + "," + film.link + "\n")
    
    f.close()

if __name__ == "__main__":
    main()
