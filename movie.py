class MyMovie():
	""" Main MyMovie class to store the details of movie. """

	def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_trailer_url):
		""" Main initialisation function to initialise movie parameters. """

		self.title = movie_title
		self.story = movie_storyline
		self.poster_image_url = movie_poster_url
		self.trailer_youtube_url = movie_trailer_url