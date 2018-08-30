import spotipy
import spotipy.util as s_util
from spotipy.oauth2 import SpotifyClientCredentials



class Main():

    def __init__(self):
        self.sp = None
        self.token = None
        self.client_credentials_manager = None
        self.username = "username"
        self.scope = "playlist-modify-public"

    def authenticate(self, username, token, sp, client_credentials_manager):
        username = "0duk4liqfcqi4cd2idc7zr5wq"
        token = s_util.prompt_for_user_token(username=username,
                                             scope=self.scope,
                                             client_id="62bb25a82b3e476181c4f05b78f0f1f1",
                                             client_secret="87cc609ccc1845ab9f9be9f39a18b2a9",
                                             redirect_uri='http://localhost/callback/')

        client_credentials_manager = SpotifyClientCredentials(client_id='ff9386c84fd14571bc4e5a9328ec1c1c',
                                                              client_secret='d8256e4a503f4daeb44d90afc7f1cc72')
        if token:
            self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager, auth=token)
            print('Successfully authorized: ' + self.sp.current_user()['display_name'])
        else:
            print("Something went wrong with the authentication")


    def get_username(self):
        return self.sp.me()["display_name"]

    def search(self, song):
        song = self.sp.search(q=song, limit=2, offset=0, type="track")
        print(song)

    def add_songs(self):
        results = self.sp.user_playlist_add_tracks(self.get_username(), self.get_playlists()[0], self.get_track_ids()[0])
        result_enkel = self.sp.user_playlist_add_tracks(self.get_username(), "spotify:user:0duk4liqfcqi4cd2idc7zr5wq:playlist:7jqEtNN0AhYlaHqzWMTJxW", "spotify:track:4ZpnV0cB73JsrHGnOP0cMQ")
        print(results)


    def get_track_ids(self,):
        """
        Returnerar alla id's som en lista
        """
        playlist_ID = self.get_playlists()[1]
        track_ids = []
        result = self.sp.user_playlist(self.get_username(), playlist_ID, fields="tracks,next")
        len_of_song = len(result["tracks"]["items"])

        for i in range(len_of_song):
            track_ids.append(result["tracks"]["items"][i]["track"]["uri"])

        return track_ids

    def current_playlists(self):
        return self.sp.current_user_playlists(limit=50)

    def get_playlists(self):
        """
        Skapar en lista med uri länkarna till varje spellista för användaren
        """
        href_list = []

        # print(self.current_playlists()["items"][0]["uri"])

        for i in range(len(self.current_playlists()["items"])):
            href_list.append(self.current_playlists()["items"][i]["uri"])

        return href_list


    def backup_account(self,):
        pass
        #Make x amount of new playlists
        # Fill them with the



    def scrape_playlists(self,username=None):
        if username==None:
            username=input("What user do you want to scrape the playlists for.")





if __name__ == "__main__":
        main = Main()
        main.authenticate(main.username, main.token, main.sp, main.client_credentials_manager)
        # main.add_songs()
        songs = main.get_track_ids()
        print(songs[3])
        # print(main.get_playlists())
        # main.get_track_ids()
        # main.get_content_of_playlist("inget")
        # main.search("Run to the hills")
