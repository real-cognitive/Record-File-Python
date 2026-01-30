import json

import pymysql as sql
import spotipy
import streamlit as st
from spotipy.oauth2 import SpotifyOAuth

scon = sql.connect(user="root", host='localhost', password="mvn123", database="music", autocommit=True) #Connecting sql client

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="76673bbf062648368df5b6dfa9c5837e",
                                               client_secret="5a4059bafd6b4189b67dfeee8030d71f",
                                               redirect_uri="http://127.0.0.1:8000/callback",
                                               scope="user-library-read")) #Connecting Spotify api via spotipy

def mood_genre(mood): #Retrieving Pre-defined genre for moods
    with scon.cursor() as con:
        
        con.execute(f"select * from gen_mood where mood='{mood}'")
        a = [x[0] for x in con]
        return a
@st.cache_data #Caches data for faster reload
def search_by_mood(mood): #Searching songs according to the mood
    gens = mood_genre(mood)
    # print(gens)
    res = sp.search(f"genre:{gens}", type="track", limit=12)['tracks']["items"]
    a = [{"name": x["name"],"id": x["id"], "art": x["album"]["images"][-2]['url']} for x in res]
    return a

@st.cache_data
def search_tracks(q): #Searching Tracks via a query
    res = sp.search(f"{q}", type="track", limit=12)['tracks']["items"]
    a = [{"name": x["name"],"id": x["id"], "art": x["album"]["images"][-2]['url']} for x in res]
    return a


def retrieve_music(ids): #Extra function in case individual music was required [REDUNDANT]
    a = [{"name": x["name"],"id": x["id"], "art": x["album"]["images"][-2]['url']} for x in sp.tracks(tracks=ids)["tracks"]]
    return a

#Entire authentication
def auth(username, password, mode="login"):
    if mode == "login":
        with scon.cursor() as con:
            try:
                con.execute(f"select id from auth where Username = '{username}' and Password  = '{password}'") #Searching for Username and password
                values = con.fetchall()
                if len(values) == 0:
                    raise ValueError("Incorrect username or password") #Rasing error to be handled elsewhere
                else:
                    return values[0][0] #Returning user id
            except Exception as e:
                raise ValueError(e)
                
    elif mode == "signup":
        with scon.cursor() as con:
            try:
                con.execute(f"insert into auth (Username,Password) values('{username}','{password}') ") #Adding User
                return auth(username, password) #Re-executing function to avoid duplicate code
            except Exception as e:
                if e.args[0] == 1062:
                    print("Username Already Exists")
                    raise ValueError("Username Already exists") #Error handling elsewhere

def create_playlist(uid, name, songs = []): #Creating fresh playlist
    with scon.cursor() as con:
        song_json = json.dumps(songs, ensure_ascii=False)
        try:
            con.execute(f"insert into playlist(name, playlist_data, uid) values(%s, %s, %s)", (name, song_json, uid)) #Using arguments to insert json serialised data
        except Exception as e:
            print(e)
def edit_playlist(uid, pid, songs): #Editing Playlist to add or remove songs
    with scon.cursor() as con:
        con.execute(f"update playlist set playlist_data=%s where uid=%s and pid=%s", (json.dumps(songs, ensure_ascii=False),uid,pid))
def get_playlists(uid,): #Fetching all playlsits
    with scon.cursor() as con:
        con.execute(f"select playlist.pid,playlist.name,playlist.playlist_data from auth inner join playlist on auth.id=playlist.uid where playlist.uid = {uid};")
        return [{ "pid": x[0],"name": x[1], "songs": json.loads(x[2])} for x in con.fetchall()]
def get_playlist(uid,pid): #Extra function to fetch single playlist [REDUNDANT]
    with scon.cursor() as con:
        con.execute(f"select playlist.pid,playlist.name,playlist.playlist_data from auth inner join playlist on auth.id=playlist.uid where playlist.uid = {uid} and playlist.pid = {pid};")
        return [{ "pid": x[0],"name": x[1], "songs": json.loads(x[2])} for x in con.fetchall()]
#__main__


'''
Song Data format:
[{"name": '', "id": '', "art": ''}]
'''