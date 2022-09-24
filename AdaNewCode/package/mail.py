import imaplib
import email
from engine import Engine
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

class Mail:
    def __init__(self):
        self.username = "tokar.pisti@gmail.com"
        self.password = "cjaqkajgzbvuhtrh"
        self.motor = Engine()

    def SendMail(self, address):
        subject = self.motor.HIO("What should the subject be?")
        if subject == "nothing":
            subject.replace("nothing", "")
        
        body = self.motor.HIO("What should the text be?")
        if subject == "nothing":
            subject.replace("nothing", "")

        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = address
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        correct_data_entry = True
        while correct_data_entry:
            csatolas =  self.motor.HIO('Would you like to send an attachment?')

            if 'yes' in csatolas:

                file_name = self.motor.HIO('Mi a fájl neve?')
                file_name.replace('pont', '').replace(' ', '')

                # search file in data folder
                filename = f"data/{self.motor.HIO('Mi a fájl neve?').replace('dot', '').replace(' ', '')}"
                attachment = open(filename, 'rb')

                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attacment; filename= %s" % filename)
                msg.attach(part)

                correct_data_entry = False

            if 'no' in csatolas:
                correct_data_entry = False

        text = msg.as_string()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.username, self.password)

        server.sendmail(self.username, address, text)
        server.quit()


    def __GetInbox(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(self.username, self.password)
        mail.select("inbox")
        _, search_data = mail.search(None, 'UNSEEN')
        my_message = []
        for num in search_data[0].split():
            email_data = {}
            _, data = mail.fetch(num, '(RFC822)')
            _, b = data[0]
            email_message = email.message_from_bytes(b)
            for header in ['from']:
                self.motor.Output(f"{email_message[header]} received a letter from him.")
                email_data[header] = email_message[header]
            correct_data_entry = True
            while correct_data_entry:
                query = self.motor.Input()
                if 'yes' in query:
                    for part in email_message.walk():
                        if part.get_content_type() == "text/plain":
                            body = part.get_payload(decode=True)
                            email_data['body'] = body.decode()
                            self.motor.Output(email_data['body'])
                        elif part.get_content_type() == "text/html":
                            html_body = part.get_payload(decode=True)
                            email_data['html_body'] = html_body.decode()
                            #engine.beszed(email_data['html_body'])
                    correct_data_entry = False

                elif 'no' in query:
                    correct_data_entry = False

        return my_message

    def MyInbox(self) -> str:
        my_inbox = str(self.__GetInbox())
        if my_inbox == '[]':
            pass
        else:
            return self.motor.Output(my_inbox)

