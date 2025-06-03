import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv
import os

load_dotenv()

smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_sender = os.getenv('EMAIL_SENDER')
email_password = os.getenv('EMAIL_PASSWORD')

email_file_path = 'send_resume/mail_ids/mail_id.txt'

resume_path = 'send_resume/resume/Resume.pdf'

def load_email_addresses(filename):
    email_data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = [part.strip() for part in line.split(',')]
            if len(parts) == 2:
                email_data.append({
                    'company': parts[0],
                    'email': parts[1]
                })
    return email_data

email_receivers = load_email_addresses(email_file_path)

subject = os.getenv('EMAIL_SUBJECT')
body_template = os.getenv('EMAIL_BODY_TEMPLATE').replace('\\n', '<br>')

if not os.path.exists(resume_path):
    print(f"Resume file not found at {resume_path}")
else:
    for receiver_data in email_receivers:
        receiver = receiver_data['email']
        company = receiver_data['company']

        body = body_template.format(company=company)


        message = MIMEMultipart()
        message['From'] = email_sender
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(body, 'html'))

        with open(resume_path, 'rb') as file:
            resume_attachment = MIMEApplication(file.read(), _subtype="pdf")
            resume_attachment.add_header(
                'Content-Disposition',
                'attachment',
                filename=os.path.basename(resume_path)
            )
            message.attach(resume_attachment)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(email_sender, email_password)
            server.sendmail(email_sender, receiver, message.as_string())
            print(f'Email sent successfully to {receiver}')
        except Exception as e:
            print(f'Failed to send email to {receiver}: {e}')
        finally:
            server.quit()