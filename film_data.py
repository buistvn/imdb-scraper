class FilmData:
    def __init__(
        self,
        title: str = " ",
        year: str = " ",
        rating: float = 0,
        popularity: int = 0,
        link: str = " ",
    ):
        self.title = title
        self.year = year
        self.rating = rating
        self.popularity = popularity
        self.link = link