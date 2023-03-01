from django.db import models

# Create your models here.

class Posts(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    
