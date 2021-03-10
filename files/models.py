from django.db import models
from django.db.models import CharField
from django_mysql.models import ListCharField
from django.core.exceptions import ValidationError
from django.utils import timezone
# from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_date_gte_now(date):
    if date < timezone.now():
        raise ValidationError('Date cannot be in the past')

class CommonFileInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    duration = models.PositiveIntegerField()
    uploadTime = models.DateTimeField(validators=[validate_date_gte_now])

    class Meta:
        abstract = True

class Song(CommonFileInfo):

    def __str__(self):
        return self.name

class Podcast(CommonFileInfo):
    host = models.CharField(max_length=100)
    # participants = models.CharField(max_length=200*5, blank=True, null=True)
    participants = ListCharField(
        base_field = CharField(max_length=100),
        size =10,
        max_length=(100*11), #character nominals, plus commas
        blank = True,
        null=True
        )

    def __str__(self):
        return self.name



class Audiobook(CommonFileInfo):
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name