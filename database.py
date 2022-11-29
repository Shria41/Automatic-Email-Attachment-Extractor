import mysql.connector
import streamlit as st
import pandas as pd
import email
import getpass, imaplib
import os
from imap_tools import MailBox, A

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="SE_email"
)
c = mydb.cursor()


def add_data(username,password):
    #st.success(username)
    #st.success(password)
    c.execute('INSERT INTO details VALUES (%s,%s)',(username,password)) 
    mydb.commit()
    st.success('Successfully added the data!')

def check(username):
    c.execute('select username,password from details where username="{}"'.format(username))
    data=c.fetchall()
    return data

def runp(username,password):
    userName=username
    passwd=password[0][1]
    print(userName)
    print(passwd)
    try:
        imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
        typ, accountDetails = imapSession.login(userName, passwd)
        print('done')

        print(typ,accountDetails)
        imapSession.select('INBOX')
        print('break')
        sub_list=['DBMS','SE','MI','DA','BD']
        for i in range(5):
            typ, data = imapSession.search(None,'HEADER Subject "{}"'.format(sub_list[i]))
            detach_dir = '.'
            if sub_list[i] not in os.listdir(detach_dir):
                os.mkdir(sub_list[i])
            print('done1')
            # Iterating over all emails
            for msgId in data[0].split():
                typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
                emailBody = messageParts[0][1]
                raw_email_string = emailBody.decode('utf-8')
                mail = email.message_from_string(raw_email_string)
                print('emailbody complete ...')
                for part in mail.walk():
                    print(part)
                    fileName = part.get_filename()
                    print(fileName)
                    if bool(fileName):
                        filePath = os.path.join(detach_dir,sub_list[i], fileName)
                        if not os.path.isfile(filePath) :
                            print(fileName)
                            fp = open(filePath, 'wb')
                            fp.write(part.get_payload(decode=True))
                            fp.close()
        imapSession.close()
        imapSession.logout()
        st.success('Run complete!')
    except :
        print('Not able to download all attachments.')
    

def delete_data(username):
    c.execute('DELETE FROM details WHERE username="{}"'.format(username))
    mydb.commit()