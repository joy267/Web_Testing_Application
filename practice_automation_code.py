import streamlit as st
from streamlit_option_menu import option_menu

from Page_Objects.test_page_object import Tracking
from console_logs import console_log
from page_speed_check import page_performance

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False


def main_app():
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
