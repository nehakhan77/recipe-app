from django.db import models

class Recipe(models.Model):
    name= models.CharField(max_length=120)
    cooking_time= models.IntegerField(help_text="In minutes", default=0)
    ingredients= models.CharField(max_length=225, help_text="Separate each ingredient by a comma")
    description= models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.name)
