from django.db import models

class formBook(models.Model):
    TIME_CHOICES = (
        ('07:00', "7:00 AM"),
        ('09:00', "9:00 AM"),
        ('11:00', "11:00 AM"),
        ('13:00', "1:00 PM"),
        ('15:00', "3:00 PM"),
        ('17:00', "5:00 PM"),
    )

    ROOM_CHOICES = (
        ('104', 'Room 104'),
        ('201', 'Room 201'),
        ('202', 'Room 202'),
        ('209', 'Room 209'),
        ('210', 'Room 210'),
        ('309', 'Room 309'),
        ('310', 'Room 310'),
        ('404', 'Room 404'),
    )

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    s_id = models.CharField(max_length=9)
    room = models.CharField(max_length=3, choices=ROOM_CHOICES)
    time_in = models.CharField(max_length=5, choices=TIME_CHOICES)
    time_out = models.CharField(max_length=5, choices=TIME_CHOICES)

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.room} from {self.time_in} to {self.time_out}"
