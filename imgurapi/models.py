from django.db import models
import datetime
# Create your models here.

class History(models.Model):
    search = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return self.search

