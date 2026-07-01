# Favorites Backend Feature

## Overview
Implemented the backend functionality for the **Favorites** feature in the Music Playlist Creator project using Django and Django REST Framework.

## Features Implemented

- Created API to list all favorite songs.
- Created API to add a song to favorites.
- Created API to remove a song from favorites.
- Connected the Favorite model with User and Song models.
- Used Django REST Framework serializers for JSON serialization.
- Configured URL routing for Favorites APIs.

## APIs

### Get All Favorites

**GET**
```
/api/favorites/
```

Returns the list of all favorite songs.

---

### Add a Favorite

**POST**
```
/api/favorites/add/
```

Example Request Body:

```json
{
    "user": 1,
    "song": 1
}
```

Creates a new favorite record.

---

### Delete a Favorite

**DELETE**
```
/api/favorite/delete/<id>/
```

Deletes the favorite record using its ID.

---

## Files Modified

- `music/models.py`
- `music/serializers.py`
- `music/views.py`
- `music/urls.py`

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite

## Testing

The APIs were tested using the Django REST Framework Browsable API.

Verified:
- Song records are retrieved successfully.
- Favorite records can be created.
- Favorite records can be listed.
- Favorite records can be deleted.

## Author

**Siri**
