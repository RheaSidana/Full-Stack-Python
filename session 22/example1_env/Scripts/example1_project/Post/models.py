from django.db import models

# Create your models here
class Post(models.Model):
    post_img = models.ImageField(upload_to='posts/rhea_sidana/')
    post_description = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    saved = models.IntegerField(default=0)