from django.db import models
from django.utils import timezone
# Fix results to be HH:MM:SS not time 
# Fix the state to be a state 

class raceDetail(models.Model):
    state = models.CharField(max_length=2)
    runnerName = models.ForeignKey('auth.User')
    raceName = models.CharField(max_length=200)
    raceDate = models.DateTimeField(default=timezone.now,blank=True, null=True)
    raceLink = models.URLField(blank=True, null=True)
    results = models.TimeField(blank=True, null=True)
    meta = models.TextField(blank=True, null=True)
   

    def publish(self):
        self.raceDate = timezone.now()
        print("This is in publish")
        self.save()

    def __str__(self):
        print("This is in __str__")
        return self.raceName