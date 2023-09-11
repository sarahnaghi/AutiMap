from django.db import models


class DigitalGame(models.Model):
    game_name= models.CharField(max_length=2048)
    game_image= models.ImageField(upload_to="images/")
    game_description= models.TextField()
    game_url_appstore = models.URLField()
    game_play_store = models.URLField()


class Toy(models.Model):
    game_name= models.CharField(max_length=2048)
    game_image= models.ImageField(upload_to="images/")
    game_description= models.TextField()
    game_url = models.URLField()

