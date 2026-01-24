import time

import streamlit as st
from pages.components import song_container

from Project.proj_backend import search_tracks

# Title of the Page
st.title("Search Songs")

# If user hasn't login, page shifts to login page
if "login" not in st.session_state:
    st.switch_page("pages/account.py")

# To display songs, page updated everytime, so most recent search is saved
if "last_search" not in st.session_state:
    st.session_state.last_search = ""

q = st.text_input("Song Name", key="qsong", label_visibility="hidden") # Text input of song
songs = ""

if q!="":
    if st.session_state.last_search != q:
        with st.spinner(show_time=True): # Timer
            time.sleep(2)
    st.session_state.last_search = q # Setting last search in cache
    songs = search_tracks(q) #Function to get songs
if songs:
    with st.container() :
        for x in songs:
            song_container(song = x, onclick="add")