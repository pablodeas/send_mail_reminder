#   Author:     Pablo Andrade
#   Created:    29/11/2024
#   Version:    0.0.2
#   Objective:  Program to send Mail in a specific time to remind me of stuffs

"""
    TODO:   
"""

import smtplib
import click
import os
import psycopg2
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from load_dotenv import load_dotenv

load_dotenv()

passw = os.getenv("PASSWORD")
mail = os.getenv("EMAIL")
database = os.getenv("DATABASE")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_container = os.getenv("DB_CONTAINER")
db_host = os.getenv("HOST")
db_port = os.getenv("PORT")

if not mail or not passw:
    print(f"> Variables not found.")
    exit(1)

def connect_db(cur, conn):
    conn = psycopg2.connect(dbname=database, user=db_user, password=db_password, host=db_host, port=int(db_port))
    cur = conn.cursor()
    return cur, conn

@click.group()
def cli():
    """> Send Mail to remind off stuff."""
    pass

@cli.command(help="> List reminders.")
def list():
    try:
        cur, conn = connect_db(None, None)
        cur.execute("select Id, Message, TO_CHAR(Creation_Date, 'dd/mm') from public.reminder order by Message asc")
        rows = cur.fetchall()

        for i in rows:
            #print(f"> Id: {i[0]} | Message: {i[1]} | Date: {i[2]}")
            print(f"> Id: {i[0]} | Message: {i[1]}")
                
        conn.commit()

    except Exception as e:
        print(f"> An error occurred: {e}")

@cli.command(help="> Insert a new reminder")
@click.argument('message', type=str)
def insert(message):
    try:
        cur, conn = connect_db(None, None)
        message = message.strip()
        cur.execute("""
            insert into public.reminder (message)
            VALUES (%s);
            """,
            (message,))
        conn.commit()
        print(f"> Reminder > {message} < inserted.")
                
    except Exception as e:
        print(f"> An error occurred: {e}")

@cli.command(help="> Delete an item reminders.")
@click.argument('id', type=float)
def delete(id):
    try:
        cur, conn = connect_db(None, None)
        cur.execute("""
            DELETE FROM public.reminder where Id = %s;
            """,
            (id,))
        conn.commit()
        print(f"> Reminder > {id} < deleted.")

    except Exception as e:
        print(f"> An error occurred: {e}")

@cli.command(help="> Delete all reminders.")
def clear():
    try:
        cur, conn = connect_db(None, None)
        cur.execute("""
            DELETE FROM public.reminder;
            """,
            )
        conn.commit()
        print(f"> Table cleared.")

    except Exception as e:
        print(f"> An error occurred: {e}")

@cli.command(help="> Send Mail.")
def send():
    def list_reminders():
        try:
            cur, conn = connect_db(None, None)
            cur.execute("SELECT Message, TO_CHAR(Creation_Date, 'dd/mm/YYYY') FROM public.reminder ORDER BY Id ASC")
            reminders = cur.fetchall()
            conn.commit()
            return reminders
        except Exception as e:
            print(f"> Error listing reminders: {e}")
            return []
        
    try:
        reminders = list_reminders()
        if not reminders:
            print("> There is no reminders to send.")
            return
        
        message = MIMEMultipart()
        message['Subject'] = "### LEMBRETES ###"
        message['From'] = mail
        message['To'] = mail
        #body = "\n".join([f"> {r[0]} - Data: {r[1]}" for r in reminders])
        body = "\n".join([f"> {r[0]}" for r in reminders])
        message.attach(MIMEText(body, 'plain'))

        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(mail, passw)
        s.send_message(message)
        print(f"> Sucess. Mail send: {body}")
    except Exception as e:
        print(f"> Error: {str(e)}.")
    finally:
        if 's' in locals():
            s.quit()

if __name__ == "__main__":
    cli(prog_name='main')