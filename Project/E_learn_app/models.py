from django.db import models

# Create your models here.

class Main(models.Model):
    url = models.URLField(blank=True,max_length=300)
    image = models.ImageField(upload_to='static')
    name = models.TextField(max_length=100)


class AllCourses(models.Model):
    urls = models.URLField(max_length=300)
    name = models.CharField(max_length=20)
    desc = models.TextField(max_length=200)

class VideoLibrarys(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='static')