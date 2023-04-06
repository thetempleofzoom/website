import streamlit as sl
from sendemail import send_email
import pandas as pd

topics = pd.read_csv('topics.csv')
sl.header('send an email')

#note: break line between subject and from important!!
# as is space after 'from' prompt!
with sl.form(key='msg', clear_on_submit=True):
    user_email = sl.text_input(label="your email address:")
    option = sl.selectbox('pls select topic:', topics['topic'])
    message_body = sl.text_area(label='your message:')
    message = f"""\
subject:message from website

From: {user_email}
Topic: {option}
{message_body}"""
    button = sl.form_submit_button(label='Submit')
    if button:
        send_email(message)
        sl.info("your email was successfully sent!")