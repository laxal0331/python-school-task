class Post:

    caption = ""

    def __init__(self, image):
        self.image = image
        self.caption = self.caption
        self.likes = 0

    def get_caption(self):
        return self.caption

    def get_image(self):
        return self.image

    def set_caption(self, caption):
        self.caption = caption

    def set_image(self, image):
        self.image = image

    def get_likes(self):
        return self.likes

    def increment_likes(self):
        self.likes += 1

    def __str__(self):  
        return "Image directory = {}, Caption = {}, Likes = {}".format(self.image, self.caption, self.likes)
