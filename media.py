# Defining Movie class from which several movie instances will be created.
class Movie():
    def __init__(self, title, storyline, img, trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = img
        self.trailer_youtube_url = trailer
