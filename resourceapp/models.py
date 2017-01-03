from django.db import models
from django.utils import timezone


class Resource(models.Model):
    author = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    rate = models.DecimalField(max_digits=6, decimal_places=2)
    created_date = models.DateTimeField(
            default=timezone.now)

    #def publish(self):
        #self.published_date = timezone.now()
        #self.save()

    #def __str__(self):
        #return self.title
