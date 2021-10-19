from django.db import models
from django.dispatch import receiver

# # Create your models here.


class Image(models.Model):
    file = models.ImageField(upload_to="files")
