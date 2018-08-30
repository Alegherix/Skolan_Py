import spotipy
import spotipy.util as util

url = "http://localhost:8888/callback/"
url = "https://www.google.se/"
username = "alfapsycho935"
scope = 'user-library-read'

#Promptar user token
util.prompt_for_user_token(username,scope,
                           client_id='62bb25a82b3e476181c4f05b78f0f1f1',
                           client_secret='87cc609ccc1845ab9f9be9f39a18b2a9',
                           redirect_uri=url)

# import spotipy
#
# spotify = spotipy.Spotify()
# results = spotify.search(q='artist:' + name, type='artist')
# print(results)