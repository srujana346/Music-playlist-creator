from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from .models import (
    Singer,
    Album,
    Song,
    Podcast,
    PodcastEpisode,
    Playlist,
    Favorite,
    ListeningHistory,
    UserSubscription,
    Payment
)

from .serializers import (
    SingerSerializer,
    AlbumSerializer,
    SongSerializer,
    PodcastSerializer,
    PodcastEpisodeSerializer,
    PlaylistSerializer,
    FavoriteSerializer,
    ListeningHistorySerializer,
    UserSubscriptionSerializer,
    PaymentSerializer
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


class PlaylistListView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class FavoriteListView(ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteCreateView(CreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteDeleteView(DestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class HistoryListView(ListAPIView):
    queryset = ListeningHistory.objects.all()
    serializer_class = ListeningHistorySerializer


class SubscriptionListView(ListAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer