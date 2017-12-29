#!/usr/bin/python
#James Parks
#12-28-17
#Requires you to enable imap in your gmail account
#and enable 'use less secure apps'

#The idea is to run this on a regular basis to check for new emails


import os
import email
import imaplib

VERBOSITY = 1

class MailCheck(object):
    """
    Logs into a gmail account (env AUTO_ADDR, AUTO_PASS) and looks for mails
    that start with 'CMD:' in order to parse that email to find a preformatted 
    command that can be executed.
    """
    def __init__(self):
        self._log(1, 'Initializing MailCheck object')

    def _log(self, priority, msg):
        if priority <= VERBOSITY:
            print(msg)

    def login(self):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(os.environ['AUTO_ADDR'], os.environ['AUTO_PASS'])
        mail.select('inbox')
        self._log(1, 'Logging in as: {}'.format(os.environ['AUTO_ADDR']))
        return mail

    def get_commands(self, mail):
        result, data = mail.uid('search', None, '(HEADER Subject "CMD:")')
        match = data[0].split()[-1]
        result, data = mail.uid('fetch', match, '(RFC822)')
        raw = data[0][1]

        msg = email.message_from_string(raw)
        sender = email.utils.parseaddr(msg['From'][-1]
        if msg['From'] == os.environ['AUTO_FROM']:
            if msg['Subject'].startswith('CMD:'):
                print('From: {}'.format(msg['From']))
                print('Subj: {}'.format(msg['Subject']))
                print('Rcvd: {}'.format(msg['Date']))
                text = self.get_first_text_block(msg)
                print(text)

    def get_first_text_block(self, msg):
        maintype = msg.get_content_maintype()
        if maintype == 'multipart':
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            return msg.get_payload()

    def logout(self, msg):
        msg.close()
        msg.logout()
