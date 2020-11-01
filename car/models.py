from django.db import models
from django.db import models


class Post(models.Model):
    Full_Name= models.CharField(max_length=300, unique=True)
    Car_Model= models.TextField()
    