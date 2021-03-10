from rest_framework import generics
from rest_framework import viewsets

from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import Podcast, Song, Audiobook
from .serializers import PodcastSerializer, SongSerializer, AudiobookSerializer

# class PodcastList(generics.ListAPIView):
#     queryset = Podcast.objects.all()
#     serializer_class = PodcastSerializer
class SongList(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PodcastList(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

# class PodcastDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Podcast.objects.all()
#     serializer_class = PodcastSerializer

class AudiobookList(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer

# class AudiobookDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Audiobook.objects.all()
#     serializer_class = AudiobookSerializer


class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Podcast.objects.all(), 'serializer_class': PodcastSerializer},
        {'queryset': Song.objects.all(), 'serializer_class': SongSerializer},
        {'queryset': Audiobook.objects.all(), 'serializer_class': AudiobookSerializer},
    ]
    # filter_backends = (filters.SearchFilter,)
    # search_fields = 'title'