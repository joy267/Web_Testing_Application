import streamlit as st
from streamlit_option_menu import option_menu
from console_logs import console_log
from page_speed_check import page_performance
from practice_automation_code import main_app
from sign_up import sign_up
from login import login

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "show_signup" not in st.session_state:
    st.session_state.show_signup = False

if st.session_state.authenticated:
    with st.sidebar:
        selected = option_menu(
            menu_title="Web Testing",
            options=['Console Logs', 'Page Performance'],
            icons=['circle-fill', 'circle-fill', 'circle-fill', 'circle-fill'],
            menu_icon='display',
            default_index=0,
        )

    if selected == 'Console Logs' and st.session_state.authenticated:
        console_log()

    elif selected == 'Page Performance' and st.session_state.authenticated:
        page_performance()

elif st.session_state.show_signup:
    sign_up()

else:
    login()
