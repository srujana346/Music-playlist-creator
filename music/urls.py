from django.urls import path

from .views import (
    SongListView,
    SingerListView,
    AlbumListView,
    PodcastListView,
    PodcastEpisodeListView,
    PlaylistListView,
    FavoriteListView,
    HistoryListView,
    SubscriptionListView,
    PaymentListView,
)

from .library_views import (
    LibraryView,
    CreatePlaylistView,
    AddSongToPlaylistView,
    RemoveSongFromPlaylistView,
    LikeSongView,
    UnlikeSongView,
    AddToHistoryView,
    ClearHistoryView,
)

urlpatterns = [
    path('songs/', SongListView.as_view(), name='songs'),
    path('singers/', SingerListView.as_view(), name='singers'),
    path('albums/', AlbumListView.as_view(), name='albums'),
    path('podcasts/', PodcastListView.as_view(), name='podcasts'),
    path('episodes/', PodcastEpisodeListView.as_view(), name='episodes'),
    path('playlists/', PlaylistListView.as_view(), name='playlists'),
    path('favorites/', FavoriteListView.as_view(), name='favorites'),
    path('history/', HistoryListView.as_view(), name='history'),
    path('subscriptions/', SubscriptionListView.as_view(), name='subscriptions'),
    path('payments/', PaymentListView.as_view(), name='payments'),

    path('library/', LibraryView.as_view(), name='library'),
    path('library/create-playlist/', CreatePlaylistView.as_view(), name='create-playlist'),
    path('library/add-song/', AddSongToPlaylistView.as_view(), name='add-song'),
    path(
    'library/remove-song/',
    RemoveSongFromPlaylistView.as_view(),
    name='remove-song',
),
path(
    'library/like-song/',
    LikeSongView.as_view(),
    name='like-song',
),
path(
    'library/unlike-song/',
    UnlikeSongView.as_view(),
    name='unlike-song',
),
path(
    'library/history/add/',
    AddToHistoryView.as_view(),
    name='add-history',
),
path(
    'library/history/clear/',
    ClearHistoryView.as_view(),
    name='clear-history',
),

]