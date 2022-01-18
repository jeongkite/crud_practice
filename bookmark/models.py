from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=10)
    desc = models.CharField(max_length=100)

    def __str__(self):
        return "["+self.name+"] "+self.desc


class Mark(models.Model):
    name = models.CharField(max_length=20)
    url = models.URLField("Site URL")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return "["+self.category.name+"] "+self.name+" : "+self.url
