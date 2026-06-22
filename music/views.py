from rest_framework.generics import ListAPIView

from .models import (
    Singer,
    Album,
    Song,
    Podcast,
    PodcastEpisode
)

from .serializers import (
    SingerSerializer,
    AlbumSerializer,
    SongSerializer,
    PodcastSerializer,
    PodcastEpisodeSerializer
)


class SongListView(ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SingerListView(ListAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class AlbumListView(ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PodcastListView(ListAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer


class PodcastEpisodeListView(ListAPIView):
    queryset = PodcastEpisode.objects.all()
    serializer_class = PodcastEpisodeSerializer