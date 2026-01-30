import streamlit as st

#Defining the structure of the webpage, That is how the page hiearchy would appear on sidebar
pages = {
    "Songs": [
        st.Page("./pages/home.py", title="Search new songs!"),
        st.Page("./pages/mood_songs.py", title = "Songs for your mood")
    ],
    "Profile": [
        st.Page("./pages/playlists.py", title= "Your playlists"),
        st.Page("./pages/account.py", title = "Manage your account"),
    ]

}

pg = st.navigation(pages) #Using the defined structure to create a page with navigation
pg.run() #Running the first page of the entire structure