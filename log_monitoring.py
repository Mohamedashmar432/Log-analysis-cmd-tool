import time
import re
import argparse
import os
import smtplib

parser = argparse.ArgumentParser(description="Advanced Log Monitoring Program")

parser.add_argument(
    "-s", "--specific-words",
    type=str,
    help="Specific words to search for in the log file",
)
parser.add_argument(
    "-a", "--alert",
    type=str,
    choices=["DEFAULT","E-MAIL","NONE"],
    default="NONE",
    help="Set an alert type: email, sms, or none (default: none)",

)

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"
TO_EMAIL = "recipient_email@gmail.com"

args = parser.parse_args()
specific_words = args.specific_words
alert_type = args.alert
file_log = 'log_file.txt'
specific_words = args.specific_words
match_pattern = fr"(FAILURE|WARNING|failure|warning).*{specific_words}"

def play_beep():
    """Play a system beep sound."""
    print('\a') 

def send_email(subject, message):
    """Send an email alert."""
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(EMAIL_ADDRESS, TO_EMAIL, email_message)
            print("Email alert sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


with open(file_log,'r') as file:
    print("""     
               _                                     _ _             
              | | ___   __ _   _ __ ___   ___  _ __ (_) |_ ___  _ __ 
              | |/ _ \ / _` | | '_ ` _ \ / _ \| '_ \| | __/ _ \| '__|
              | | (_) | (_| | | | | | | | (_) | | | | | || (_) | |   
              |_|\___/ \__, | |_| |_| |_|\___/|_| |_|_|\__\___/|_|   
                       |___/                                         
                                                                
              - > A tool to monitor application log.
                                                                 -Ashmar """)
    print(f"Monitoring for words: {specific_words}")
    print(f"Alert type set to: {alert_type}")
    file.seek(0,2)    
    while True:
        line = file.readline()

        if not line:
            time.sleep(1)
            continue
            
        if re.search(match_pattern,line):
            print(line)    

            if alert_type =="E_MAIL":
                print("Sending alert to mail...\n")
                print("Add your credential for mail alert")
            elif alert_type =="DEFAULT":
                print("sending alert \n")
                play_beep()    


