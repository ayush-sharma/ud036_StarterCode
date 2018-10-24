import movie
import fresh_tomatoes


""" Defining a list of 6 movies from the IMDB box office listings page.
    Each movie has a title, storyline, poster URL, and YouTube trailer URL. """

movie_1 = movie.MyMovie(
	"A Star Is Born",
	"A musician helps a young singer find fame, even as age and alcoholism send his own career into a downward spiral.",
	"https://m.media-amazon.com/images/M/MV5BMjE3MDQ0MTA3M15BMl5BanBnXkFtZTgwMDMwNDY2NTM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"https://www.youtube.com/watch?v=nSbzyEJ8X9E"
	)

movie_2 = movie.MyMovie(
	"Venom",
	"When Eddie Brock acquires the powers of a symbiote, he will have to release his alter-ego \"Venom\" to save his life.",
	"https://m.media-amazon.com/images/M/MV5BNzAwNzUzNjY4MV5BMl5BanBnXkFtZTgwMTQ5MzM0NjM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"https://www.youtube.com/watch?v=u9Mv98Gr5pY"
	)

movie_3 = movie.MyMovie(
	"Goosebumps 2: Haunted Halloween",
	" Two young friends find a magic book that brings a ventriloquist's dummy to life.",
	"https://m.media-amazon.com/images/M/MV5BNzgxMDQ2MDUyMF5BMl5BanBnXkFtZTgwNzgyMjQyNjM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"https://www.youtube.com/watch?v=nQeOzfm-lps"
	)

movie_4 = movie.MyMovie(
	"First Man",
	"A look at the life of the astronaut, Neil Armstrong, and the legendary space mission that led him to become the first man to walk on the Moon on July 20, 1969.",
	"https://m.media-amazon.com/images/M/MV5BMDBhOTMxN2UtYjllYS00NWNiLWE1MzAtZjg3NmExODliMDQ0XkEyXkFqcGdeQXVyMjMxOTE0ODA@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"https://www.youtube.com/watch?v=PSoRx87OO6k"
	)

movie_5 = movie.MyMovie(
	"Smallfoot",
	"A Yeti is convinced that the elusive creatures known as \"humans\" really do exist. ",
	"https://m.media-amazon.com/images/M/MV5BMTc5NzI1NjY4MV5BMl5BanBnXkFtZTgwNDIxNTIyNDM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"https://www.youtube.com/watch?v=34cHO5_LX9g"
	)

movie_6 = movie.MyMovie(
	"The Old Man & the Gun",
	"Based on the true story of Forrest Tucker and his audacious escape from San Quentin at the age of 70 to an unprecedented string of heists that confounded authorities and enchanted the public. ",
	"https://m.media-amazon.com/images/M/MV5BOTk3NjU5MjIxM15BMl5BanBnXkFtZTgwNjU0OTU2NTM@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
	"https://www.youtube.com/watch?v=d7rlUe-Thvk"
	)

""" Putting all 6 movies in a list. """
my_movies = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]

""" Calling library function to generate HTML page for our list of movies. """
fresh_tomatoes.open_movies_page(my_movies)
