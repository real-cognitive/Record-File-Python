import streamlit as st

import Project.proj_backend as bckend


def logout():  #Deletes all stored variables, which means deletes the stored uid as well.
    for x in st.session_state:
        del st.session_state[x]
    print([x for x in st.session_state])


if "login" not in st.session_state: #Adding login variable
    st.session_state.login = True


@st.dialog("Login" if st.session_state.login else "Signup", dismissible=False) #Dialog box
def auth_dialog():
    username = st.text_input("**Username**") #Accepting Username and password
    password = st.text_input("**Password**")
    if "login_err_text" in st.session_state: #Showing the custom errors raised
        st.error(st.session_state.login_err_text)
    with st.container(horizontal=True, horizontal_alignment="distribute"):
        if st.button("Submit"):
            try:
                uid = bckend.auth(username=username, password=password, mode= "login" if st.session_state.login else "signup")
                st.session_state.uid = uid
                st.rerun()
            except ValueError as e:
                st.session_state.login_err_text = e #Storing error in variable
                st.rerun()
        if st.button(f"###### {"Signup" if st.session_state.login else "Login"}", type="tertiary",):
            st.session_state.login = False if st.session_state.login else True
            if "login_err_text" in st.session_state:
                del st.session_state.login_err_text
            st.rerun()


if "uid" not in st.session_state:
    auth_dialog()
    st.session_state.auth_toast = True #Showing the dialog of successful login


st.write("## Account options")
if "uid" in st.session_state:
    if st.session_state.auth_toast:
        st.toast("###### Login Successful!", duration=2)
        st.session_state.auth_toast = False
    st.write(f"**User id**: {st.session_state.uid}")
st.button("**Logout**",type="primary", on_click=logout, key="logout")
