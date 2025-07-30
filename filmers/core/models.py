from django.db import models
from user.models import SuperUser , BaseUser

Ganre_Choices = {
    ('Mystery', 'Mystery'),
    ('Western', 'Western'),
    ('Musical', 'Musical'),
    ('War', 'War'),
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Horror', 'Horror'),
    ('Sci-Fi', 'Sci-Fi'),
    ('Romance', 'Romance'),
    ('Thriller', 'Thriller'),
    ('Documentary', 'Documentary'),
    ('Animation', 'Animation'),
    ('Fantasy', 'Fantasy'),
    ('Other', 'Other'),
}

class Director(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Comment(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0,
                             validators= [
                                 models.MinValuvaeValidator(0.0),
                                 models.MaxValueValidator(10.0)
                             ])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(BaseUser, on_delete=models.CASCADE)

class Movie(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.DateField(models.CharField(max_length=100))
    genre = models.CharField(max_length=10 , choices=Ganre_Choices, default='Other')
    description = models.TextField(blank=True, null=True)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    created_by = models.ForeignKey(SuperUser, on_delete=models.CASCADE)
    #add average rating
    def average_rating(self):
        ratings = self.comments.all().values_list('rate', flat=True)
        if ratings :
            return round(sum(ratings) / len(ratings), 2) 
        else :
            return 0.0
