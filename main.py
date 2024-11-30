#   Author:     Pablo Andrade
#   Created:    29/11/2024
#   Version:    0.0.1
#   Objective:  Program to send Mail in a specific time to remind me of stuffs

"""
    TODO:   Conect to a database made in docker
            Create a function to insert values in the database
            A function to delete all records of the database table
            Make the mail send the record of the database
            The mail sender need to execute every day, add to the crontab
"""

import smtplib
import click
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from load_dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.getcwd(), '.env'))

passw = os.getenv("PASSWORD")
mail = os.getenv("EMAIL")
#container = os.getenv("CONTAINER")

if not mail or not passw:
    print(f"> Variables not found.")
    exit(1)

@click.group()
def cli():
    """> Send Mail to remind off stuff."""
    pass

@cli.command(help="> Send Mail.")
@click.argument('body', type=str)
def send(body):
    try:
        message = MIMEMultipart()
        message['Subject'] = "> Lembrete."
        message['From'] = mail
        message['To'] = mail
        message.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(mail, passw)
        s.send_message(message)
        print(f"> Sucess.")
    except Exception as e:
        print(f"> Error: {str(e)}.")
    finally:
        s.quit()

if __name__ == "__main__":
    cli(prog_name='main')