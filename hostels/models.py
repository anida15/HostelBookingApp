from tkinter import CASCADE
from xml.parsers.expat import model
from django.db import models
from django.conf import settings

# Create your models here.
class Booking(model.model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'