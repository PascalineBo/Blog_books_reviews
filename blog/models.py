from django.db import models
from django.conf import settings


class Ticket(models.Model):  # ticket model
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=2048)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):  # ticket model
    ticket = models.ForeignKey(to=Ticket,on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(max_length=1024,
                                              validators=[ MinValueValidator(0),
                                                           MaxValueValidator(5)])
    content = models.CharField(max_length=5000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length = 8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

