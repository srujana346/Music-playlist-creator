from rest_framework import serializers
from .models import Playlist, PlaylistSong


class CreatePlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name', 'description', 'cover_image']


class AddSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistSong
        fields = ['playlist', 'song']