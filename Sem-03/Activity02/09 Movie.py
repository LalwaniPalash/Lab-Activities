class Movie:
    def __init__(self, title, director, releaseYear, rating):
        self.title = title
        self.director = director
        self.releaseYear = releaseYear
        self.rating = rating

    def displayMovieInfo(self):
        return f"The title of the movie is {self.title} which was directed by {self.director}. It was released in year {self.releaseYear} and It has received a Rating of {self.rating} stars."

    def compareReleaseYears(self, otherMovie):
        if self.releaseYear < otherMovie.releaseYear:
            return f"{self.title} was released before {otherMovie.title}"
        elif self.releaseYear > otherMovie.releaseYear:
            return f"{self.title} was released after {otherMovie.title}"
        else:
            return f"{self.title} and {otherMovie.title} were released in the same year"


movie1 = Movie("Inception", "Christopher Nolan", 2010, 4.5)
movie2 = Movie("Interstellar", "Christopher Nolan", 2014, 4.8)

print(movie1.displayMovieInfo())
print(movie2.displayMovieInfo())

print(movie1.compareReleaseYears(movie2))
