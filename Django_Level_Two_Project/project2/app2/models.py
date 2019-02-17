from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=256, unique=True)
    last_name = models.CharField(max_length=256, unique=True)
    email = models.EmailField(max_length=256, unique=True)

    # # def __dict__()
    # def __str__(self):
    #
    #     return str()
