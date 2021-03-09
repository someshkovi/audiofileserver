from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField

# Create your models here.

class Podcast(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    # participants = models.CharField(max_length=200*5, blank=True, null=True)
    participants = ListCharField(
        base_field = CharField(max_length=10),
        size =10,
        max_length=(10*11), #character nominals, plus commas
        blank = True,
        null=True
        )

    def __str__(self):
        return self.name

class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

        
    