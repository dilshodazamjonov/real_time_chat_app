from django.db import models

# Create your models here.


class Room(models.Model):
    room_name = models.CharField(max_length=255, verbose_name='Room name')

    def __str__(self):
        return self.room_name

    class Meta:
        verbose_name = 'Rooms'
        verbose_name_plural = 'Room'


class Messages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Room name')
    sender = models.CharField(max_length=255, verbose_name='Sender name')
    message = models.TextField(verbose_name='Message content')

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = 'Messages'
        verbose_name_plural = 'Message'