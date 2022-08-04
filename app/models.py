from unicodedata import category
from django.db import models
from django.conf import settings


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

class Technician(models.Model):
    full_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.full_name



class Appointment(models.Model):
    """Contains info about appointment"""

    class Meta:
        unique_together = ('technician', 'booking_date', 'timeslot')

    TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )

    username = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician,on_delete = models.CASCADE)
    booking_date = models.DateField(help_text="YYYY-MM-DD")
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)
    created_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
        return '{} {} {}. Patient: {}'.format(self.booking_date, self.timeslot, self.technician, self.username)