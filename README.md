Music Playlist Creator
Project Overview
Music Playlist Creator is a Django-based music streaming and playlist management system. The project provides database management, REST APIs, playlist creation, favorites tracking, listening history, podcast management, subscriptions, and payment tracking.

Database Tables
User
Stores user account information.

Singer
Stores singer/artist details.

Album
Stores album information.

Song
Stores song details including audio files.

Playlist
Stores playlists created by users.

PlaylistSong
Links songs with playlists.

Favorite
Stores user favorite songs.

ListeningHistory
Stores songs played by users.

Podcast
Stores podcast information.

PodcastEpisode
Stores episodes belonging to podcasts.

SubscriptionPlan
Stores available subscription plans.

UserSubscription
Stores user subscription details.

Payment
Stores payment transaction details.

Relationships
One Singer can have many Albums.
One Singer can have many Songs.
One Album can contain many Songs.
One User can create many Playlists.
One Playlist can contain many Songs.
One User can have many Favorite Songs.
One User can have many Listening History records.
One Podcast can have many Podcast Episodes.
One User can have many Subscriptions.
One Subscription can have many Payments.
Available APIs
Music APIs
/api/songs/
/api/singers/
/api/albums/
Podcast APIs
/api/podcasts/
/api/episodes/
Playlist APIs
/api/playlists/
Favorites APIs
/api/favorites/
History APIs
/api/history/
Subscription APIs
/api/subscriptions/
Payment APIs
/api/payments/
Technologies Used
Python
Django
Django REST Framework
SQLite
Git & GitHub
Team Contribution
Database Design
Django Models
REST API Development
Admin Panel Configuration
GitHub Collaboration
Progress Update (30 June 2026)
Completed
Implemented the Library Backend module.

APIs Developed
GET /api/library/
POST /api/library/create-playlist/
POST /api/library/add-song/
DELETE /api/library/remove-song/
POST /api/library/like-song/
DELETE /api/library/unlike-song/
POST /api/library/history/add/
DELETE /api/library/history/clear/
Files Added
music/library_views.py
music/library_serializers.py
Files Modified
music/urls.py
Testing
Successfully tested all APIs using Thunder Client.
Future Work
Integrate authentication (request.user)
Replace temporary user_id = 2
Add validation for duplicate songs and favorites
Integrate with frontend
Improve API error handling# Favorites Backend Feature

## Progress Update (Favorites Backend)

### Overview
Implemented the backend APIs for the **Favorites** feature using Django REST Framework. The current implementation supports listing, adding, and deleting favorite songs. Authentication with the login system has not yet been integrated and will be completed in a later phase.

### Features Completed

- Developed the Favorites backend module.
- Created REST APIs for managing favorite songs.
- Configured serializers for the Favorite model.
- Implemented API views using Django REST Framework generic views.
- Configured URL routing for Favorites APIs.
- Tested the APIs using the Django REST Framework Browsable API.

### APIs Implemented

#### Get All Favorite Songs
**GET**
```
/api/favorites/
```

Returns the list of favorite songs.

#### Add Song to Favorites
**POST**
```
/api/favorites/add/
```

Adds a selected song to the favorites list.

#### Remove Song from Favorites
**DELETE**
```
/api/favorites/delete/<id>/
```

Removes a song from the favorites list.

### Files Modified

- `music/views.py`
- `music/serializers.py`
- `music/urls.py`

### Testing

Successfully verified:

- Listing favorite songs.
- Adding songs to favorites.
- Deleting songs from favorites.
- API functionality using the Django REST Framework Browsable API.
- Data verification through the Django Admin panel.

### Current Limitation

- User authentication is **not yet integrated** with the Favorites APIs.
- Currently, favorite records are created using the selected user from the API form.
- Integration with the login/authentication module will be completed after the authentication feature is implemented.

### Future Enhancements

- Integrate authenticated users using `request.user`.
- Restrict users to view only their own favorites.
- Prevent duplicate favorite entries.
- Connect the Favorites APIs with the frontend.
- Improve validation and error handling.

**Siri**
