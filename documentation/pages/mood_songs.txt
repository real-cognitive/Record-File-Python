#mood_songs.py


import time

import streamlit as st
from pages.components import song_container

import Project.proj_backend as bckend

st.title("Search by mood") #Title
if "login" not in st.session_state:
    st.switch_page("pages/account.py")
if "last_mood" not in st.session_state: #Adding the cached variable
    st.session_state.last_mood = ""



mood = st.selectbox("Mood",
             ["","Sad", "Calm", "Angry", "Happy", "Romantic", "Energetic", "Varied"],
             label_visibility= "hidden",
             placeholder="Choose mood"
             ) #Making user choose a mood


if mood!="":
    if st.session_state.last_mood != mood:
        with st.spinner(show_time=True): #Loader
            time.sleep(2)
    st.session_state.last_mood = mood
    songs = bckend.search_by_mood(mood)
    if songs:
        with st.container() :
            for x in songs:
                song_container(song = x, onclick="add") #Display
