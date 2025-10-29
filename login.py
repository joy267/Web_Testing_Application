import time

import streamlit as st
import pyrebase
import firebase_admin
from streamlit_option_menu import option_menu
from validate_email_address import validate_email


def login():
    # 🔹 Initialize Firebase App (Ensure it's only initialized once)

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

    # 🔐 Initialize authentication session state

    if "form_submitted" not in st.session_state:
        st.session_state.form_submitted = False

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if "user_email" not in st.session_state:
        st.session_state.user_email = None

    if "show_signup" not in st.session_state:
        st.session_state.show_signup = False

    def submit_form():
        st.session_state.form_submitted = True

    def is_valid_email(login_email):
        return validate_email(login_email)

    # 🏠 Login Form
    with st.form(key='login_form', clear_on_submit=True):
        st.header("**:green[Login]**")
        login_email = st.text_input("Email", placeholder="Enter your email address")
        login_password = st.text_input("Password", placeholder="Enter your password", type="password")

        col1, col2, col3, col4, col5 = st.columns(5)
        with col3:
            login_button = st.form_submit_button("Login")

    if login_button:
        if login_email:
            if is_valid_email(login_email):
                if login_password:
                    if len(login_password) >= 8:
                        try:
                            user = auth.sign_in_with_email_and_password(login_email, login_password)
                            if user:
                                st.session_state.authenticated = True
                                st.session_state.user_email = login_email
                                st.success(f"✅ Login Successful! Welcome {login_email} 🎉")
                                time.sleep(1)
                                st.rerun()  # Refresh app to load main_app()
                            else:
                                st.error("❌ Invalid email or password.")
                        except Exception as e:
                            st.error("❌ Invalid email or password.")
                    else:
                        st.error("❌ Password must be at least 8 characters long.")
                else:
                    st.error("⚠️ Password field is required.")
            else:
                st.error("❌ Invalid email address")
        else:
            st.error("⚠️ Email field is required.")

    st.markdown("Don't have an account?")
    if st.button("Sign Up"):
        st.session_state.show_signup = True
        st.rerun()

    st.markdown("---")
    st.markdown("<center><small>Created by <b>Mrityunjoy Mandal</b> © 2025</small></center>", unsafe_allow_html=True)
