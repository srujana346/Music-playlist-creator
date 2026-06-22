from django.urls import path
from .views import (
    SongListView,
    SingerListView,
    AlbumListView,
    PodcastListView,
    PodcastEpisodeListView
)

urlpatterns = [
    path('songs/', SongListView.as_view(), name='songs'),
    path('singers/', SingerListView.as_view(), name='singers'),
    path('albums/', AlbumListView.as_view(), name='albums'),
    path('podcasts/', PodcastListView.as_view(), name='podcasts'),
    path('episodes/', PodcastEpisodeListView.as_view(), name='episodes'),
]