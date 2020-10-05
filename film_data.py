class FilmData:
    def __init__(
        self,
        title: str = " ",
        director: str = " ",
        overview: str = " ",
        rating: float = 0,
        popularity: int = 0,
    ):
        self.title = title
        self.director = director
        self.overview = overview
        self.rating = rating
        self.popularity = popularity