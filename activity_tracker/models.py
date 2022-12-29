import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Athlete(models.Model):
    username=models.CharField(max_length=200)
    creation_date=models.DateTimeField('Account creation', default=timezone.now)

    def __str__(self):
        return f"<User {self.id} - {self.username}>"

class Activity(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    sport = models.IntegerField(default=0)
    distance = models.IntegerField(default=0)
    start_date=models.DateTimeField('Activity date', default=timezone.now)

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.start_date <= now