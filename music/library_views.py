from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import (
    Playlist,
    Favorite,
    ListeningHistory,
    PlaylistSong,
)

from .serializers import (
    PlaylistSerializer,
    FavoriteSerializer,
    ListeningHistorySerializer,
)

from .library_serializers import (
    CreatePlaylistSerializer,
    AddSongSerializer,
)


class LibraryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        playlists = Playlist.objects.filter(user=user)
        favorites = Favorite.objects.filter(user=user)
        history = ListeningHistory.objects.filter(user=user)

        return Response({
            "playlists": PlaylistSerializer(playlists, many=True).data,
            "liked_songs": FavoriteSerializer(favorites, many=True).data,
            "recently_played": ListeningHistorySerializer(history, many=True).data,
        })


class CreatePlaylistView(APIView):

    def post(self, request):
        serializer = CreatePlaylistSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user_id=2)   # Temporary until authentication is ready
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddSongToPlaylistView(APIView):

    def post(self, request):
        serializer = AddSongSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class RemoveSongFromPlaylistView(APIView):

    def delete(self, request):
        playlist_id = request.data.get("playlist")
        song_id = request.data.get("song")

        try:
            playlist_song = PlaylistSong.objects.get(
                playlist_id=playlist_id,
                song_id=song_id
            )

            playlist_song.delete()

            return Response(
                {"message": "Song removed successfully"},
                status=status.HTTP_200_OK
            )

        except PlaylistSong.DoesNotExist:
            return Response(
                {"error": "Song not found in playlist"},
                status=status.HTTP_404_NOT_FOUND
            )
class LikeSongView(APIView):

    def post(self, request):
        user_id = 2   # Temporary until authentication is ready
        song_id = request.data.get("song")

        favorite = Favorite.objects.create(
            user_id=user_id,
            song_id=song_id
        )

        return Response(
            {
                "id": favorite.id,
                "message": "Song added to favorites"
            },
            status=status.HTTP_201_CREATED
        )
class UnlikeSongView(APIView):

    def delete(self, request):
        user_id = 2      # Temporary until authentication
        song_id = request.data.get("song")

        try:
            favorite = Favorite.objects.get(
                user_id=user_id,
                song_id=song_id
            )

            favorite.delete()

            return Response(
                {"message": "Song removed from favorites"},
                status=status.HTTP_200_OK
            )

        except Favorite.DoesNotExist:
            return Response(
                {"error": "Favorite not found"},
                status=status.HTTP_404_NOT_FOUND
            )   


class AddToHistoryView(APIView):

    def post(self, request):
        user_id = 2      # Temporary until authentication
        song_id = request.data.get("song")

        history = ListeningHistory.objects.create(
            user_id=user_id,
            song_id=song_id
        )

        return Response(
            {
                "id": history.id,
                "message": "Song added to history"
            },
            status=status.HTTP_201_CREATED
        ) 
class ClearHistoryView(APIView):

    def delete(self, request):
        user_id = 2      # Temporary until authentication

        ListeningHistory.objects.filter(user_id=user_id).delete()

        return Response(
            {"message": "Listening history cleared successfully"},
            status=status.HTTP_200_OK
        )            