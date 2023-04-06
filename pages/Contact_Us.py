import streamlit as sl
from sendemail import send_email

sl.header('send an email')

with sl.form(key='msg'):
    user_email = sl.text_input(label="your email address:")
    message_body = sl.text_area(label='your message:')
    message = f"""\
subject:message from website
from: {user_email}
{message_body}"""
    button = sl.form_submit_button(label='Submit')
    if button:
        send_email(message)
        sl.info("your email was successfully sent!")