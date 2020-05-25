class Movie:
    def __init__(self):
        self.movieName = '' 
        self.releaseYear = ''
        self.genre = ''
        self.rating = 0
        self.review_count = 0 

    def setMoveName(self, name):
        self.movieName = name 
    
    def getMoveName(self):
        return self.movieName 

    def setReviewCount(self, count):
        self.review_count += count
    
    def getReviewCount(self):
        return self.review_count
    
    def setReleaseYear(self, year):
        self.releaseYear = year 
    
    def getReleaseYear(self):
        return self.releaseYear 
    
    def setGenre(self, genre):
        self.genre = genre 
    
    def getGenre(self):
        return self.genre 
    
    def setRating(self, rating):
        self.rating += rating
    
    def getRating(self):
        return self.rating