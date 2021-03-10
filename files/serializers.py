from rest_framework import serializers
from . import models


class SongSerializer(serializers.ModelSerializer):
 
    class Meta:
        fields = '__all__'
        model = models.Song

class PodcastSerializer(serializers.ModelSerializer):
    participants = serializers.CharField(max_length=100*11)

    def validate_participants(self, value):
        p = value.split(',')
        for v in range(0,len(p)):
            if len(p[v])>100:
                raise serializers.ValidationError(f'participant name at position {v} is of length >100')
        return value     

    class Meta:
        fields = '__all__'
        model = models.Podcast

class AudiobookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Audiobook
