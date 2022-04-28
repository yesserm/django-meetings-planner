from datetime import time
from django.db import models


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    floor_number = models.IntegerField(default=1)
    room_number = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}: sala {self.room_number} en el piso {self.floor_number}"


class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} a las {self.start_time} el {self.date}"
