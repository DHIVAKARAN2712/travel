from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class TravelPlace(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class VisitSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(TravelPlace, on_delete=models.CASCADE)
    reason = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} wants to visit {self.place.title}"
