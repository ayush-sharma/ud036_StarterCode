class MyMovie():
    """ Main MyMovie class to store the details of movie.
	
	This is the main MyMovie class that stores 	the details of the movie. It stores the movie titles,
	movie story line, movie poster URL, and movie trailer URL.

    """

    def __init__(self, movie_title, movie_storyline, movie_poster_url, movie_trailer_url):
        """ Main initialisation function to initialise movie parameters.

		Attributes:
			movie_title (str): The title of the movie.
			movie_storyline (str): The storyline of the movie.
			movie_poster_url (str): The URL of the movie's poster.
			movie_trailer_url (str): The URL of the movie's trailer on YouTube.com.
        """

        self.title = movie_title
        self.story = movie_storyline
        self.poster_image_url = movie_poster_url
        self.trailer_youtube_url = movie_trailer_url
