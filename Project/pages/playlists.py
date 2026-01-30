import time

import streamlit as st
from pages.components import song_container

import Project.proj_backend as bckend

if "login" not in st.session_state: #Login check
    st.switch_page("pages/account.py")

    
@st.dialog("Create Playlist") #Dialog box named "Create playlist"
def create_playlist_dialog(songs = []):
    name = st.text_input("Name of playlist")
    if st.button("Submit", type="primary"):
        if name!="":
            bckend.create_playlist(songs=songs, uid = st.session_state.uid, name = name)
            st.session_state.close_dialog = True
            print(st.session_state.close_dialog)
            st.rerun()
        else:
            st.warning("Empty name")
if "close_dialog" not in st.session_state:
    
    st.session_state.close_dialog = False

# __main__

st.title("Your Playlists") #Title of page
st.space(2)

if st.button("Create Playlist",):
    st.session_state.close_dialog = False
    if not st.session_state.close_dialog:
        create_playlist_dialog()

st.space(1)
for x in bckend.get_playlists(st.session_state.uid):
    playlist_con = st.expander(label=x["name"]) # A widget which expands revealing contents
    with playlist_con:
        if len(x["songs"])!=0:
            for s in x["songs"]:
                song_container(song = s, large = False, onclick="remove", playlist=x)
        else:
            st.write("Nothing to see here!! Keep adding songs.")