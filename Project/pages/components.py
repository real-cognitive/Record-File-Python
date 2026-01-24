from typing import Literal

import streamlit as st
from streamlit_product_card import product_card

import Project.proj_backend as backend

# This includes General components for the site

# Setting a cache variable
if "open_action_dialog" not in st.session_state:
    st.session_state.open_action_dialog = False

# Function to display song song data as a card
def song_container(song,onclick = "none", large = True, act = True, playlist = None):
    id,img,name = song["id"], song["art"], song["name"] #data extraction from song dictionary
    c = st.container(border=True) #Creating a bordered box
    cover,title,action = c.columns((1.5 if large else 1,10,1.5 if large else 1), vertical_alignment="center") #Dividing card into columns of relative widths
    cover.image(img, width="stretch") #Cover image
    title.write(f"####{"#" if not large else ""} {name}") #Title of song, changing size on the basis of type of card, using markdown
    
    #If button enabled
    if act:
        #On clicking action button
        if action.button("", width=100, key=id, icon=":material/add:" if onclick == "add" else ":material/delete:" if onclick == "remove" else None, type="primary" if onclick == "remove" else "secondary"):
            st.session_state.open_action_dialog = True #Opening dialog
            if st.session_state.open_action_dialog:
                if onclick == "add": #Adding song to playlist
                    add(song=song)
                    pass
                elif onclick == "remove": #Removing song form playlist
                    remove(song=song, playlist=playlist)
                    pass
                else:
                    pass

@st.dialog("Add to playlist")
def add(song): #Adding song
    l_playlist = backend.get_playlists(uid = st.session_state.uid) # Getting list of all playlists
    playlist_data = st.selectbox(label="Playlists", options=l_playlist, format_func=lambda song: song["name"]) # Chossing a playlist
    st.space(2)
    c= st.container(horizontal=True, horizontal_alignment="distribute") 
    with c:
        if st.button("Add to playlist"):
            playlist_data["songs"].append(song) #adding song to the song data previosuly in the playlist
            backend.edit_playlist(uid=st.session_state.uid, pid=playlist_data["pid"], songs=playlist_data["songs"])
            st.session_state.open_action_dialog = False #Closing Dialog
            st.rerun() #Refresh

def dialogFormat(song): # Method of displaying choices 
    return str(song)+"A"

def remove(song, playlist): #Removing Songs
    playlist["songs"].remove(song)
    backend.edit_playlist(uid = st.session_state.uid, pid=playlist["pid"], songs=playlist["songs"])
    st.rerun()

