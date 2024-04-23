class Movie:
    movie_database = []

    def __init__(self, title, genre, releaseYear):
        self.title = title
        self.genre = genre
        self.releaseYear = releaseYear
        Movie.movie_database.append(self)

    @classmethod
    def add_movie_to_database(cls, movie):
        cls.movie_database.append(movie)


class User:
    def __init__(self, name):
        self.name = name
        self.favoriteGenre = None

    def recommendMovies(self, genre):
        recommended_movies = []
        for movie in Movie.movie_database:
            if movie.genre == genre:
                recommended_movies.append(movie.title)
        if recommended_movies:
            print(f"Hi {self.name}, here are some movie recommendations for the {genre} genre:")
            for movie_title in recommended_movies:
                print("-", movie_title)
        else:
            print(f"Sorry, no movies available in the {genre} genre.")

movie1 = Movie("Inception", "Science Fiction", 2010)
movie2 = Movie("The Shawshank Redemption", "Drama", 1994)
movie3 = Movie("The Dark Knight", "Action", 2008)

user1 = User("Alice")

user1.recommendMovies("Drama")
