from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
admin.site.register(Favorite)
admin.site.register(ListeningHistory)
admin.site.register(Podcast)
admin.site.register(PodcastEpisode)
admin.site.register(SubscriptionPlan)
admin.site.register(UserSubscription)
admin.site.register(Payment)


# Register your models here.
