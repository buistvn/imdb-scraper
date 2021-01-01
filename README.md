# Web Scraper
This tool takes the most popular films of the week from [IMDb](https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm) and extracts relevant data. The list of films is stored in a database which can be accessed with MySQL. The list can be sorted by popularity ranking, title, release date, and average rating. The sorted information is also written to a separate .csv output file for a more accessible and convenient viewing.<br />

In the project directory, you can run:

### `python main.py`

Runs the program, asks for user input, and writes the data to film_data.csv.

In the MySQL Workbench query, you can run:

### `USE filmdb`

Uses the filmdb database.

### `SELECT * FROM films`

Selects all entries from the films table.