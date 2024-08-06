from django.db import models
from django.shortcuts import reverse

class User(models.Model):
    username= models.CharField(max_length=120)
    name= models.CharField(max_length=120)
    pic = models.ImageField(upload_to='users', default='no_picture.jpg')
    description= models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
