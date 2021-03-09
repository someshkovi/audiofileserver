from rest_framework import generics
from rest_framework import viewsets

from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import Podcast, Song
from .serializers import PodcastSerializer, SongSerializer

# class PodcastList(generics.ListAPIView):
#     queryset = Podcast.objects.all()
#     serializer_class = PodcastSerializer

class PodcastList(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class SongList(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class PodcastDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class TextAPIView(ObjectMultipleModelAPIView):
    querylist = [
        {'queryset': Podcast.objects.all(), 'serializer_class': PodcastSerializer},
        {'queryset': Song.objects.all(), 'serializer_class': SongSerializer},
    ]
    # filter_backends = (filters.SearchFilter,)
    # search_fields = 'title'