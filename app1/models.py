from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ClientUser(User):
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    phone = models.IntegerField()
    mail = models.CharField(null=True,max_length=50)


class Booking(models.Model):
    Game = models.CharField(max_length=100)
    Date_Time = models.DateTimeField()
    Time_Needed = models.CharField(max_length=100)