import time
import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# --- Locator Mapping ---
locator_map = {
    "ID": By.ID,
    "Name": By.NAME,
    "Class Name": By.CLASS_NAME,
    "Tag Name": By.TAG_NAME,
    "Link Text": By.LINK_TEXT,
    "Partial Link Text": By.PARTIAL_LINK_TEXT,
    "CSS Selector": By.CSS_SELECTOR,
    "XPath": By.XPATH,
}


def test_case_builder():
    # st.set_page_config(page_title="Streamlit Test Builder", layout="wide")

    st.title("🧩 Automated Test Case Builder & Runner")

    # --- Test Meta Info ---
    test_title = st.text_input("**Enter your test title**", "", placeholder="Enter your test title")
    test_url = st.text_input("**Enter your test URL**", "", placeholder="Enter your test URL")

    st.divider()

    # --- WebDriver Setup Section ---
    st.subheader("🌐 WebDriver Configuration")

    driver_path = "C:\\Projects\\Web_Testing_Application\\Webdrivers\\chromedriver.exe"

    headless_mode = st.checkbox("Run in headless mode?", value=True)
    # capture_logs = st.checkbox("Capture browser console logs?", value=True)

    st.divider()

    # --- Test Step Builder ---
    st.subheader("🧱 Build Your Test Steps")

    if "test_steps" not in st.session_state:
        st.session_state.test_steps = []

    for step in st.session_state.test_steps:
        for key in ["action", "web_elements", "locators", "locators_value", "input_value"]:
            if key not in step:
                step[key] = ""

    if not st.session_state.test_steps:
        st.session_state.test_steps.append({
            "action": "",
            "web_elements": None,
            "locators": None,
            "locators_value": "",
            "input_value": ""
        })

    def add_test_step():
        st.session_state.test_steps.append({
            "action": "",
            "web_elements": None,
            "locators": None,
            "locators_value": "",
            "input_value": ""
        })

    def remove_test_step(index):
        st.session_state.test_steps.pop(index)

    for i, step in enumerate(st.session_state.test_steps):
        with st.expander(f"🧱 Test Step {i + 1}", expanded=True):
            st.session_state.test_steps[i]["action"] = st.text_input(
                f"Step Name / Action ({i + 1})",
                step["action"],
                placeholder="e.g., Click Login Button / Enter Username",
                key=f"action_{i}"
            )

            col1, col2, col3 = st.columns([1, 1, 1.5])

            with col1:
                st.session_state.test_steps[i]["web_elements"] = st.selectbox(
                    f"Web Element ({i + 1})",
                    ("Input Box", "Button"),
                    index=None,
                    placeholder="Select web element",
                    key=f"web_element_{i}"
                )

            with col2:
                st.session_state.test_steps[i]["locators"] = st.selectbox(
                    f"Locator Type ({i + 1})",
                    ("ID", "Name", "Class Name", "Tag Name", "Link Text",
                     "Partial Link Text", "CSS Selector", "XPath"),
                    index=None,
                    placeholder="Select locator",
                    key=f"locator_{i}"
                )

            with col3:
                st.session_state.test_steps[i]["locators_value"] = st.text_input(
                    f"Locator Value ({i + 1})",
                    step["locators_value"],
                    placeholder="Enter locator value",
                    key=f"locator_value_{i}"
                )

            if step["web_elements"] == "Input Box":
                st.session_state.test_steps[i]["input_value"] = st.text_input(
                    f"Input Value ({i + 1})",
                    step["input_value"],
                    placeholder="e.g., testuser, password123",
                    key=f"input_value_{i}"
                )

            if len(st.session_state.test_steps) > 1:
                st.button("🗑️ Remove This Step", key=f"remove_{i}", on_click=remove_test_step, args=(i,))

    st.button("➕ Add Another Test Step", on_click=add_test_step)
    st.divider()

    # --- Function: Run Test ---
    def execute_test_case(test_url, steps, driver_path, locator_map):
        st.write("🚀 Starting automated test...")

        # --- Setup WebDriver ---
        global progress_text, driver
        options = Options()
        if headless_mode:
            options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.set_capability("goog:loggingPrefs", {"browser": "ALL"})

        try:
            service = Service(driver_path)
            driver = webdriver.Chrome(service=service, options=options)
            driver.get(test_url)
            driver.maximize_window()
            st.info(f"🌐 Navigated to {test_url}")
            time.sleep(2)

            total_steps = len(steps)
            progress_bar = st.progress(0)
            progress_text = st.empty()

            # --- Execute all test steps ---
            for i, step in enumerate(steps):
                step_name = step.get("action", f"Step {i + 1}")
                element_type = step.get("web_elements")
                locator_type = locator_map.get(step.get("locators"))
                locator_value = step.get("locators_value", "")
                input_value = step.get("input_value", "")

                # Update progress bar
                progress = int(((i) / total_steps) * 100)
                progress_bar.progress(progress)
                progress_text.text(f"🚀 Executing Step {i + 1} of {total_steps} — {step_name}")

                # Validation
                if not locator_type or not locator_value:
                    st.warning(f"⚠️ Step {i + 1} skipped — missing locator info.")
                    continue

                try:
                    element = driver.find_element(locator_type, locator_value)

                    if element_type == "Button" or "click" in step_name.lower():
                        element.click()
                        st.info(f"🖱️ Step {i + 1} Passed — Clicked element.")
                    elif element_type == "Input Box" or "enter" in step_name.lower():
                        element.send_keys(input_value)
                        st.info(f"⌨️ Step {i + 1} Passed — Entered text: '{input_value}'.")
                    else:
                        st.info(f"ℹ️ Step {i + 1} Passed — Element found, no specific action taken.")

                    time.sleep(1)

                except Exception as e:
                    st.error(f"❌ Error at Step {i + 1} ({step_name}): {e}")
                    raise  # Stop test immediately on failure

            # ✅ Final progress update
            progress_bar.progress(100)
            progress_text.text("✅ All test steps executed successfully.")
            st.success("🎉 Test execution completed successfully!")
            driver.quit()

        except Exception:
            st.error(" ❌ Test Stop")
            driver.quit()

    # --- Buttons ---
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⚙️ Generate Selenium Code"):
            from selenium.webdriver.common.by import By

            selenium_code = []
            selenium_code.append("from selenium import webdriver")
            selenium_code.append("from selenium.webdriver.common.by import By")
            selenium_code.append("from selenium.webdriver.chrome.service import Service")
            selenium_code.append("from selenium.webdriver.chrome.options import Options")
            selenium_code.append("import time")
            selenium_code.append("")
            selenium_code.append("options = Options()")
            if headless_mode:
                selenium_code.append("options.add_argument('--headless')")
            selenium_code.append(f"service = Service(r'{driver_path}')")
            selenium_code.append("driver = webdriver.Chrome(service=service, options=options)")
            selenium_code.append(f"driver.get('{test_url}')")
            selenium_code.append("time.sleep(2)")
            for i, step in enumerate(st.session_state.test_steps):
                locator = step.get("locators")
                locator_value = step.get("locators_value")
                input_value = step.get("input_value", "")
                action = step.get("action", "")
                if locator and locator_value:
                    if "click" in action.lower() or step.get("web_elements") == "Button":
                        selenium_code.append(
                            f"driver.find_element(By.{locator.upper().replace(' ', '_')}, '{locator_value}').click()")
                    elif "enter" in action.lower() or step.get("web_elements") == "Input Box":
                        selenium_code.append(
                            f"driver.find_element(By.{locator.upper().replace(' ', '_')}, '{locator_value}').send_keys('{input_value}')")
            selenium_code.append("driver.quit()")
            st.code("\n".join(selenium_code), language="python")

    with col2:
        if st.button("▶ Run Test"):
            execute_test_case(test_url, st.session_state.test_steps, driver_path, locator_map)

    st.markdown("---")
    st.markdown("<center><small>Created by <b>Mrityunjoy Mandal</b> © 2025</small></center>", unsafe_allow_html=True)
