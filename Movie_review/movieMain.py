from movieReviewDriver import MovieReviewDriver
class Driver:
    def run(self):
        objMovieReviewDriver = MovieReviewDriver()
        objMovieReviewDriver.addMovie("Don", "2006", "Action")
        objMovieReviewDriver.addMovie("Tiger", "2008", "Dramma")
        objMovieReviewDriver.addMovie("Padmaavat", "2006", "Comedy")
        objMovieReviewDriver.addMovie("Lunchbox-2", "2020", "Dramma")
        objMovieReviewDriver.addMovie("Guru", "2006", "Dramma")
        objMovieReviewDriver.addMovie("Metro", "2006", "Romance")

        objMovieReviewDriver.addUser("SRK")
        objMovieReviewDriver.addUser("Salman")
        objMovieReviewDriver.addUser("Deepika")

        objMovieReviewDriver.addReview("SRK", "Don", 2)
        objMovieReviewDriver.addReview("SRK", "Padmaavat", 8)
        objMovieReviewDriver.addReview("Salman", "Don", 5)
        objMovieReviewDriver.addReview("Deepika", "Don", 9)
        objMovieReviewDriver.addReview("Deepika", "Guru", 6)
        objMovieReviewDriver.addReview("SRK", "Don", 10)
        objMovieReviewDriver.addReview("Deepika", "Lunchbox", 6)
        objMovieReviewDriver.addReview("SRK", "Tiger", 5)
        objMovieReviewDriver.addReview("SRK", "Metro", 7)

        objMovieReviewDriver.topN_by_viewer(1, "2006")
        objMovieReviewDriver.topN_by_critics(1, "2006")
        objMovieReviewDriver.topN_by_critics_in_genre(1, "Dramma")
        objMovieReviewDriver.topN_by_genre(1, "Dramma")

        objMovieReviewDriver.average_rating_movie_by_year("2006")

Driver().run()
        








