import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st

client_id = ""
client_secret = ""
client_credentials_manager = SpotifyClientCredentials(client_id = client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_recommendations(track_name):
    results = sp.search(q=track_name, type='track')
    track_uri = results['tracks']['items'][0]['uri']

    recommendations = sp.recommendations(seed_tracks=[track_uri])['tracks']
    return recommendations

st.title("Music Recommendation System")
track_name = st.text_input("Enter a song name:")

if track_name:
    recommendations = get_recommendations(track_name)
    print(recommendations)
    st.write("Recommendations songs: ")
    for track in recommendations:
        st.write(track['name'])
        st.image(track['album']['images'][0]['url'])

