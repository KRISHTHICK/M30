import smtplib
from email.mime.text import MIMEText

def send_email_notification(to_email, subject, message):
    from_email = "your-email@example.com"
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(from_email, "your-email-password")
        server.sendmail(from_email, to_email, msg.as_string())
