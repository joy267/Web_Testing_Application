import time
import random
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def console_logs():
    # st.set_page_config(page_title="Console Logs", layout="wide")

    st.title("Website Console Logs")

    st.markdown("--------------------------------")

    # if "authenticated" not in st.session_state:
    #     st.session_state.authenticated = False

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

        options = Options()
        options.add_argument('--headless')
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

        # --- Launch Browser ---
        service = Service(
            "C:\\Projects\\Web_Testing_Application\\Webdrivers\\chromedriver.exe")  # or full path if needed
        driver = webdriver.Chrome(service=service, options=options)

        driver.get(keyword)
        driver.maximize_window()
        time.sleep(2)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)

        # --- Fetch Console Logs ---
        logs = driver.get_log("browser")

        st.subheader("Console Logs:")
        for entry in logs:
            level = entry["level"]
            message = entry["message"]
            if level == "SEVERE":
                st.error(f"[{level}] {message}")
            elif level == "WARNING":
                st.warning(f"[{level}] {message}")
            elif level == "INFO":
                st.info(f"[{level}] {message}")

        driver.quit()

    st.markdown("---")
    st.markdown("<center><small>Created by <b>Mrityunjoy Mandal</b> © 2025</small></center>", unsafe_allow_html=True)
