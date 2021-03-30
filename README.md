<!-- PROJECT -->
# Web Scraper

![Project Screenshot][project-screenshot]

The web scraper is a tool that extracts relevant data from the most popular films of the week on IMDb. The data is stored in a MySQL database and written to a .csv output file. It can also be sorted by popularity ranking, title, release date, and average rating.



<!-- BUILT WITH -->
## Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running, follow these instructions.

### Prerequisites

* pip
  ```sh
  py -m pip --version
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/buistvn/web-scraper.git
   ```
2. Install Beautiful Soup
   ```sh
   pip install beautifulsoup4
   ```



<!-- USAGE -->
## Usage

* Run the program
  ```sh
  python main.py
  ```
* Set filmdb as the current database in MySQL Workbench
  ```sh
  USE filmdb
  ```
* Select all entries from the films table in MySQL Workbench
  ```sh
  SELECT * FROM films
  ```



<!-- LINKS & IMAGES -->
[project-screenshot]: images/WebScraper.png
