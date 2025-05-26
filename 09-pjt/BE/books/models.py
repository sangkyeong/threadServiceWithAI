import datetime
from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100, default='default.png')

    def __str__(self):
        return self.name


class Book(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='books'
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=20)
    cover = models.URLField()  
    publisher = models.CharField(max_length=100)
    pub_date = models.DateField()
    author = models.CharField(max_length=100)
    author_info = models.TextField()
    author_photo = models.URLField()  
    customer_review_rank = models.FloatField()
    subTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.title

