from django.db import models

# Create your models here.


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=2048)
