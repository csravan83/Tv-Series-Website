import webbrowser
class Movie():
    def __init__(self, tv_title , tv_story , tv_poster , tv_trailer):
        self.title = tv_title
        self.storyline = tv_story
        self.poster_image_url = tv_poster
        self.trailer_youtube_url = tv_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)