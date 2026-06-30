from django.urls import path
from .views import (
    SongListView,
    SingerListView,
    AlbumListView,
    PodcastListView,
    PodcastEpisodeListView,
    PlaylistListView,
    FavoriteListView,
    FavoriteCreateView,
    FavoriteDeleteView,
    HistoryListView,
    SubscriptionListView,
    PaymentListView,
)

urlpatterns = [
    path('songs/', SongListView.as_view(), name='songs'),
    path('singers/', SingerListView.as_view(), name='singers'),
    path('albums/', AlbumListView.as_view(), name='albums'),
    path('podcasts/', PodcastListView.as_view(), name='podcasts'),
    path('episodes/', PodcastEpisodeListView.as_view(), name='episodes'),
    path('playlists/', PlaylistListView.as_view(), name='playlists'),
    path('favorites/', FavoriteListView.as_view(), name='favorites'),
    path('favorites/add/', FavoriteCreateView.as_view(), name='favourite-add'),
    path('favorite/delete/<int:pk>/', FavoriteDeleteView.as_view(), name='favourite-delete'),
    path('history/', HistoryListView.as_view(), name='history'),
    path('subscriptions/', SubscriptionListView.as_view(), name='subscriptions'),
    path('payments/', PaymentListView.as_view(), name='payments'),
]