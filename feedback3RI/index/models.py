from django.db import models

class visitor(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_number = models.IntegerField()
    Message = models.TextField(max_length=20)

class user(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Rating = models.IntegerField()
    Message = models.TextField(max_length=20)




# Create your models here.
