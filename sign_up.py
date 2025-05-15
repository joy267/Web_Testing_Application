import pyrebase
import streamlit as st
from validate_email_address import validate_email


def sign_up():
    # Configuration Key

    # For Firebase JS SDK v7.20.0 and later, measurementId is optional
    config = {
        'apiKey': "AIzaSyCsQVKILoHmcBSMztaptC7zQpSOSiGlc2Y",
        'authDomain': "webtestingapp-64f14.firebaseapp.com",
        'projectId': "webtestingapp-64f14",
        'databaseURL': "https://webtestingapp-64f14-default-rtdb.asia-southeast1.firebasedatabase.app/",
        'storageBucket': "webtestingapp-64f14.firebasestorage.app",
        'messagingSenderId': "883011116295",
        'appId': "1:883011116295:web:1d22ad19fa03827390b9a2",
        'measurementId': "G-5KB2CC6TJ6",
    }

    # Firebase Authentication
    firebase = pyrebase.initialize_app(config)
    auth = firebase.auth()

    # Database Authentication
    db = firebase.database()
    storage = firebase.storage()

    st.title("Welcome to :violet[Web Testing Application]:sunglasses:")

    # Email Validation
    def is_valid_email(email):
        return validate_email(email)

    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False

    # def sign_up():

    with ((st.form(key='signup', clear_on_submit=False))):
        st.header("**:green[Sign Up]**")
        email = st.text_input("Email", key='email', placeholder="Enter your email address")
        username = st.text_input("Username", key='username', placeholder="Enter your username")

        if "show_password" not in st.session_state:
            st.session_state.show_password = False

        password = st.text_input("Password", key='password', placeholder="Enter your password",
                                 type="text" if st.session_state.show_password else "password")
        confirm_password = st.text_input("Confirm Password", key='confirm_password',
                                         placeholder="Confirm your password",
                                         type="text" if st.session_state.show_password else "password")

        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            submit_button = st.form_submit_button("Sign Up")

    try:
        if submit_button:
            if email:
                if is_valid_email(email):
                    if username:
                        if len(username) >= 4:
                            if password:
                                if len(password) >= 8:
                                    if confirm_password:
                                        if password == confirm_password:
                                            user = auth.create_user_with_email_and_password(email, password)
                                            if user:
                                                st.success("Account created successfully !! 🎉🎉🎉")
                                                st.balloons()

                                        else:
                                            st.error(" ❌ Passwords do not match")
                                    else:
                                        st.error(" ⚠️ Confirm Password field is required.")
                                else:
                                    st.error(" ❌ Password must be at least 8 characters long.")
                            else:
                                st.error(" ⚠️ Password field is required.")
                        else:
                            st.error(" ❌ Username is too short")
                    else:
                        st.error(" ⚠️ Username field is required.")
                else:
                    st.error(" ❌ Invalid email address")
            else:
                st.error(" ⚠️ Email field is required.")

    except Exception as e:
        st.error(" ❌  ❌  Account already exists")

    st.markdown("Already have an account?")
    if st.button("Back to Login"):
        st.session_state.show_signup = False
        st.rerun()

    st.markdown("---")
    st.markdown("<center><small>Created by <b>Mrityunjoy Mandal</b> © 2025</small></center>", unsafe_allow_html=True)
