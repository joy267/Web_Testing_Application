import time
import random

import pandas as pd
import Page_Objects.console_logs
from Page_Objects.console_logs import Console_Logs
import streamlit as st


def console_log():
    st.title("Website Console Logs")

    st.markdown("--------------------------------")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    with st.form("my_form", clear_on_submit=True):
        test_url = st.text_input("**Enter Your Test URL** :", "", placeholder="Please enter your test URL")
        keyword = test_url + str("/?keyword=console_log_checking_") + str(random.randint(0, 100000)) + str(
            "&enableconsole")

        col1, col2, col3, col4 = st.columns([1, 2, 3, 1])
        with col4:
            submit_button = st.form_submit_button("Submit")
        if test_url != "":
            st.write(f"The Test URL is : ", keyword)

    if test_url != "":

        with st.status("Collecting Console Logs...", expanded=True) as status:

            st.write("Searching for console logs...")

            time.sleep(1)

            console_logs = Console_Logs()

            Page_Objects.console_logs.configure_chrome_options_for_logging()

            console_logs.open_webdriver()

            time.sleep(1)

            console_logs.implicit_wait(10)

            time.sleep(1)

            console_logs.open_website(keyword)

            time.sleep(1)

            console_logs.scroll_website()

            time.sleep(2)

            st.write("Downloading console logs...")

            time.sleep(1)

            logs = console_logs.fetch_console_logs()

            level = []
            for entry in logs:
                level.append({
                    'level': entry['level'],
                    'message': entry['message'],
                    'source': entry['source'],
                    'timestamp': entry['timestamp']
                })
            try:
                status.update(state="complete")
                status.update(label="Excel file has been generated!", state="complete", expanded=False)

            except status.update(state="error"):
                st.button("Rerun")

            time.sleep(1)

        df = pd.DataFrame(level)

        st.dataframe(df)

    st.markdown("---")
    st.markdown("<center><small>Created by <b>Mrityunjoy Mandal</b> © 2025</small></center>", unsafe_allow_html=True)