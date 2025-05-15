import random
import time

import openpyxl
import pandas as pd

from Page_Objects.page_speed import Page_Speed
import streamlit as st


def page_performance():
    page_speed = Page_Speed()

    st.title("Website Page Speed Performance")

    st.markdown("--------------------------------")

    with st.form("my_form", clear_on_submit=False):
        test_url = st.text_input("**Enter Your Test URL** : ", "", placeholder="Please enter your test URL")

        col1, col2, col3, col4 = st.columns([1, 2, 3, 1])
        with col4:
            submit_button = st.form_submit_button("Submit")

    if test_url != "":
        with st.status("**Analysing Test URL**", expanded=True) as status:
            st.write("Loading PageSpeed Insights ...")

            time.sleep(1)

            page_speed.open_webdriver()

            page_speed.implicit_wait(10)

            page_speed.open_pagespeed_insights("https://pagespeed.web.dev/")

            page_speed.accept_cookies()

            page_speed.delete_all_cache()

            # # First iteration

            st.write("First iteration is starting ...")

            keyword_1 = test_url + str("/?keyword=tracking_check_") + str(random.randint(0, 100000))

            page_speed.test_page_url(keyword_1)

            time.sleep(1)

            page_speed.click_analyze_button()

            time.sleep(1)

            page_speed.explicit_wait(90)

            first_iteration_performance = page_speed.get_mobile_site_performance()

            first_iteration_accessibility = page_speed.get_mobile_accessibility()

            first_iteration_best_practices = page_speed.get_mobile_best_practices()

            first_iteration_seo = page_speed.get_mobile_seo()

            first_iteration_first_contentful_paint = page_speed.get_mobile_first_contentful_paint()

            first_iteration_largest_contentful_paint = page_speed.get_mobile_largest_contentful_paint()

            first_iteration_total_blocking_time = page_speed.get_mobile_total_blocking_time()

            first_iteration_cumulative_layout_shift = page_speed.get_mobile_cumulative_layout_shift()

            first_iteration_speed_index = page_speed.get_mobile_speed_index()

            time.sleep(1)

            page_speed.close_window()

            st.write("First iteration has completed.")

            time.sleep(1)

            # # Second iteration

            st.write("Second iteration is starting ...")

            page_speed.open_webdriver()

            page_speed.implicit_wait(10)

            page_speed.open_pagespeed_insights("https://pagespeed.web.dev/")

            page_speed.accept_cookies()

            page_speed.delete_all_cache()

            keyword_2 = test_url + str("/?keyword=tracking_check_") + str(random.randint(0, 100000))

            page_speed.test_page_url(keyword_2)

            time.sleep(1)

            page_speed.click_analyze_button()

            time.sleep(1)

            page_speed.explicit_wait(90)

            second_iteration_performance = page_speed.get_mobile_site_performance()

            second_iteration_accessibility = page_speed.get_mobile_accessibility()

            second_iteration_best_practices = page_speed.get_mobile_best_practices()

            second_iteration_seo = page_speed.get_mobile_seo()

            second_iteration_first_contentful_paint = page_speed.get_mobile_first_contentful_paint()

            second_iteration_largest_contentful_paint = page_speed.get_mobile_largest_contentful_paint()

            second_iteration_total_blocking_time = page_speed.get_mobile_total_blocking_time()

            second_iteration_cumulative_layout_shift = page_speed.get_mobile_cumulative_layout_shift()

            second_iteration_speed_index = page_speed.get_mobile_speed_index()

            time.sleep(1)

            page_speed.close_window()

            st.write("Second iteration has completed.")

            time.sleep(1)

            # # Third iteration

            st.write("Third iteration is starting ...")

            page_speed.open_webdriver()

            page_speed.implicit_wait(10)

            page_speed.open_pagespeed_insights("https://pagespeed.web.dev/")

            page_speed.accept_cookies()

            page_speed.delete_all_cache()

            keyword_3 = test_url + str("/?keyword=tracking_check_") + str(random.randint(0, 100000))

            page_speed.test_page_url(keyword_3)

            time.sleep(1)

            page_speed.click_analyze_button()

            time.sleep(1)

            page_speed.explicit_wait(90)

            third_iteration_performance = page_speed.get_mobile_site_performance()

            third_iteration_accessibility = page_speed.get_mobile_accessibility()

            third_iteration_best_practices = page_speed.get_mobile_best_practices()

            third_iteration_seo = page_speed.get_mobile_seo()

            third_iteration_first_contentful_paint = page_speed.get_mobile_first_contentful_paint()

            third_iteration_largest_contentful_paint = page_speed.get_mobile_largest_contentful_paint()

            third_iteration_total_blocking_time = page_speed.get_mobile_total_blocking_time()

            third_iteration_cumulative_layout_shift = page_speed.get_mobile_cumulative_layout_shift()

            third_iteration_speed_index = page_speed.get_mobile_speed_index()

            time.sleep(1)

            page_speed.close_window()

            st.write("Third iteration has completed.")

            time.sleep(1)

            # # Generating Excel file

            st.write("Generating Excel file...")

            time.sleep(1)

            status.update(state="complete")
            status.update(label="Excel file has been generated!", state="complete", expanded=False)

        col1, col2, col3, col4 = st.columns([1, 2, 3, 1])
        with col4:
            st.button("Rerun")

        st.divider()

        time.sleep(1)

        df = pd.DataFrame({
            "Iterations": [1, 2, 3],
            "Keywords": [keyword_1, keyword_2, keyword_3],
            "Performance": [first_iteration_performance,
                            second_iteration_performance,
                            third_iteration_performance],
            "Accessibility": [first_iteration_accessibility,
                              second_iteration_accessibility,
                              third_iteration_accessibility],
            "Best Practices": [first_iteration_best_practices,
                               second_iteration_best_practices,
                               third_iteration_best_practices],
            "SEO": [first_iteration_seo,
                    second_iteration_seo,
                    third_iteration_seo],
            "First Contentful Paint (FCP)": [first_iteration_first_contentful_paint,
                                             second_iteration_first_contentful_paint,
                                             third_iteration_first_contentful_paint],
            "Largest Contentful Paint (LCP)": [first_iteration_largest_contentful_paint,
                                               second_iteration_largest_contentful_paint,
                                               third_iteration_largest_contentful_paint],
            "Total Blocking Time (TBT)": [first_iteration_total_blocking_time,
                                          second_iteration_total_blocking_time,
                                          third_iteration_total_blocking_time],
            "Cumulative Layout Shift (CLS)": [first_iteration_cumulative_layout_shift,
                                              second_iteration_cumulative_layout_shift,
                                              third_iteration_cumulative_layout_shift],
            "Speed Index (SI)": [first_iteration_speed_index,
                                 second_iteration_speed_index,
                                 third_iteration_speed_index]

        })

        st.dataframe(df, use_container_width=True)

        page_speed.close_window()

    st.markdown("---")
    st.markdown("<center><small>Created by <b>Mrityunjoy Mandal</b> © 2025</small></center>", unsafe_allow_html=True)