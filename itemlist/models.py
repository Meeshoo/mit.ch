from django.db import models


class Itemlist(models.Model):

    def __init__(self):
        pass

class Project():

    def __init__(self, name, description, image, link):
        self.name = name
        self.description = description
        self.image = image
        self.link = link

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getImage(self):
        return self.image

    def getLink(self):
        return self.link
