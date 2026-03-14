class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def __init__ (self):
         Movies.__init__(self)
    
    def add_movie(self, movie):
        Movies.add_movie(self, movie)
        return f"Комедии: {self.movies}"

class Drama(Movies):
    def __init__ (self):
         Movies.__init__(self)

    def add_movie(self, movie):
        Movies.add_movie(self, movie)
        return f"Драмы: {self.movies}"
    
comedy_1 = Comedy()
print(comedy_1.add_movie('Большой куш'))

drama_1 = Drama()
print(drama_1.add_movie('Оружейный барон'))