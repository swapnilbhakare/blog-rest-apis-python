from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Posts(models.Model):
    _id = models.BigAutoField(primary_key=True)
    blogTitle= models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    auther = models.TextField()
    content = models.TextField()

    def __str__(self):
        return self.blogTitle

