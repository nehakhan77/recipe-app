from django.db import models

class User(models.Model):
    username= models.CharField(max_length=120)
    name= models.CharField(max_length=120)

    def __str__(self):
        return str(self.name)
