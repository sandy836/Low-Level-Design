from movie import Movie
from user import User 
from heapq import *
class MovieReviewDriver:
    def __init__(self):
        self.movie_list = dict()
        self.user_list = dict()
    
    def addMovie(self, movieName, releaseYear, genre):
        ObjMovie = Movie()
        ObjMovie.setMoveName(movieName)
        ObjMovie.setReleaseYear(releaseYear)
        ObjMovie.setGenre(genre)
        self.movie_list[movieName] = ObjMovie
    
    def addUser(self, userName):
        ObjUser = User()
        ObjUser.setUserName(userName)
        self.user_list[userName] = ObjUser
    
    def addReview(self, userName, movieName, rating):
        try:
            if movieName in self.user_list[userName].getReviewedList():
                raise Exception("Exception Multiple Review Not Allowed")
            elif movieName not in self.movie_list:
                raise Exception("Exception Movie Not Yet Released")
            else:
                if self.user_list[userName].getUserType():
                    self.movie_list[movieName].setReviewCount(2)
                    rating = 2*rating
                else:
                    self.movie_list[movieName].setReviewCount(1)
                self.movie_list[movieName].setRating(rating)
                self.user_list[userName].addToReviewedList(movieName)
                self.user_list[userName].setReviewCount()
                if self.user_list[userName].getReviewCount()==3:
                    self.user_list[userName].setUserTypeToCritics(True)
        except Exception as e:
            print(e)
    
    def topN_by_viewer(self, n, year):
        heap = []
        for movieName, movieInfo in self.movie_list.items():
            if movieInfo.getReleaseYear() == year:
                heappush(heap, (-1*movieInfo.getRating(), movieName))
        while n>0 and heap:
            movieRating, movieName = heappop(heap)
            print(movieName+" - "+str(abs(movieRating))+" rating\n")
            n -= 1
    
    def topN_by_critics(self, n, year):
        heap = []
        for userName, userInfo in self.user_list.items():
            if userInfo.getUserType():
                for movieName in userInfo.getReviewedList():
                    if self.movie_list[movieName].getReleaseYear() == year:
                        heappush(heap, (-1*self.movie_list[movieName].getRating(), movieName))
        
        while n>0 and heap:
            movieRating, movieName = heappop(heap)
            print(movieName+" - "+str(abs(movieRating))+" rating\n")
            n -= 1
    
    def topN_by_critics_in_genre(self, n, genre):
        heap = []
        for userName, userInfo in self.user_list.items():
            if userInfo.getUserType():
                for movieName in userInfo.getReviewedList():
                    if self.movie_list[movieName].getGenre() == genre:
                        heappush(heap, (-1*self.movie_list[movieName].getRating(), movieName))

        while n>0 and heap:
            movieRating, movieName = heappop(heap)
            print(movieName+" - "+str(abs(movieRating))+" rating\n")
            n -= 1
    
    def topN_by_genre(self, n, genre):
        heap = []
        for movieName, movieInfo in self.movie_list.items():
            if movieInfo.getGenre() == genre:
                heappush(heap, (-1*self.movie_list[movieName].getRating(), movieName))
        
        while n>0 and heap:
            movieRating, movieName = heappop(heap)
            print(movieName+" - "+str(abs(movieRating))+" rating\n")
            n -= 1
    
    def average_rating_movie_by_year(self, year):
        total=count=0
        for movieName, movieInfo in self.movie_list.items():
            if movieInfo.getReleaseYear() == year:
                count +=  movieInfo.getReviewCount()
                total += movieInfo.getRating()
            
        print(str(total/count)+" rating")




        






