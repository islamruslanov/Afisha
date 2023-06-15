from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(null=True,blank=True)
    duration = models.FloatField()
    director = models.ForeignKey(Director,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.director.name} - {self.title}'

class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.movie.title} - {self.text}'
