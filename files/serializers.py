from rest_framework import serializers
from . import models


class PodcastSerializer(serializers.ModelSerializer):
    participants = 
    class Meta:
        fields = ('id','name','created_at')
        model = models.Podcast

class SongSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Song