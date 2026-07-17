from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=100)
    marks = models.DecimalField(max_digits=6, decimal_places=2)
    age = models.IntegerField(default=18)
    


    def __str__(self):
        return self.name