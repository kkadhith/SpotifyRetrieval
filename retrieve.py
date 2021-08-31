import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

f1 = open("songs.txt", "w", encoding='utf-8')
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='', client_secret=''))

# 'results' returns a dictionary w/ the playlist information
results = spotify.user_playlist(user='', playlist_id='', fields=None, market=None)

'''Since it's a dictionary, elements can only be accessed through keys : std::unordered_map<T, T>
Iterating through results would give us info about the playlist, like description, owner, name, followers, tracks, etc.
Since we're interested in the names & artists, we need to access 'tracks', which is another dictionary.
Within 'tracks', there is different keys like href, items, limit, next, etc.
We're interested in the items of the track, so we need to access that using ['items']
We then get a list of dictionaries (each element in the list has a dictionary) and these dicts contain info about each track.
For instance, where it's avaliable, images, height, artists, name, etc.
the key 'name' just results in a string (name of song), but the key 'artists' results in a list of dictionaries that contain info
about each artists. We are only interested in the main artist, so access the [0]th element in the list and retrieve the 'name'. '''

plinfo = results['tracks']['items']
for item in plinfo:
    f1.write(item['track']['name'] + ' - ' + item['track']['artists'][0]['name'])
    f1.write('\n')
f1.close()
