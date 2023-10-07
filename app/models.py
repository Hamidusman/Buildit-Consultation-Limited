from django.db import models
import os
import datetime
# Create your models here.
class image(models.Model):
    name =models.CharField(max_length=30)
    image =models.ImageField(upload_to='img%y')

    def __str__(self):
        return self.name