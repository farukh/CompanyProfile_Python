import time
import pandas

import streamlit as st
from send_email import send_email
topics = pandas.read_csv('topics.csv')
st.title("Contact Us")
with st.form(key="email_form"):
    user_email = st.text_input("Your Email Address:")
    option = st.selectbox(
        "What topic do you want to discuss?",
        topics)
    raw_message = st.text_area("Your Message: ")

    message = f"""Subject: Company Profile App, {user_email}, {option}\n

        From: {user_email}
        Topic: {option}
        Sent Following Message: 
        {raw_message}
            """
    btn_submit = st.form_submit_button("Submit")
    print(btn_submit)
    if btn_submit:
        msg = st.info("Please wait... \n Email being sent. ")
        send_email(message)
        msg.info("Email Sent Successfully. ")
