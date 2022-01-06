from smtplib import SMTP
from email.message import EmailMessage


def email_alert(to, subject="Alert", body="Alert!"):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = subject
    msg["To"] = to

    user = "mrnotifi@gmail.com"
    msg["From"] = user
    password = "nixqgstknzqcfqig"
    port = int(587)

    with SMTP("smtp.gmail.com", port) as server:
        server.starttls()
        server.login(user, password)

        server.send_message(msg)


if __name__ == "__main__":

    print("test")
    email_alert("broetjem@gmail.com", "hey", "hello world")
