#!/usr/bin/python
#James Parks
#12-28-17
#Requires you to enable imap in your gmail account
#and enable 'use less secure apps'

#The idea is to run this on a regular basis to check for new emails


import os
import email
import imaplib
import datetime

VERBOSITY = 1


class MailCheck(object):
    """
    Logs into a gmail account (env AUTO_ADDR, AUTO_PASS) and looks for mails
    that start with 'CMD:' in order to parse that email to find a preformatted 
    command that can be executed.
    """
    def __init__(self):
        self._log(1, 'Initializing MailCheck object')
        self.date_of_last = datetime.datetime.now()
    def _log(self, priority, msg):
        if priority <= VERBOSITY:
            print(msg)

    def login(self):
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(os.environ['AUTO_ADDR'], os.environ['AUTO_PASS'])
            mail.select('inbox')
            self._log(1, 'Logging in as: {}'.format(os.environ['AUTO_ADDR']))
            return mail
        except:
            self._log(1, 'error logging in')

    def get_commands(self, mail):
        result, data = mail.uid('search', None, '(HEADER Subject "CMD:")')
        match = data[0].split()[-1]
        result, data = mail.uid('fetch', match, '(RFC822)')
        raw = data[0][1]

        msg = email.message_from_string(raw)
        sender = email.utils.parseaddr(msg['From'][-1]
        if sender == os.environ['AUTO_FROM']:
            self._log(6, 'passed sender test')
            if msg['Subject'].startswith(os.environ['AUTO_PREFIX']):
                self._log(6, 'passed subject test')
                print('From: {}'.format(msg['From']))
                print('Subj: {}'.format(msg['Subject']))
                print('Rcvd: {}'.format(msg['Date']))
                text = self.get_first_text_block(msg)
                print(text)
                return text

    def process_commands(self, cmd):
        self._log(1, 'here is where we process our commands')
        if cmd.startswith('print:')
            string = cmd.split(':')
            print('print cmd: {}'.format(string))

    def get_first_text_block(self, msg):
        maintype = msg.get_content_maintype()
        if maintype == 'multipart':
            self._log(6, 'multipart email')
            for part in msg.get_payload():
                if part.get_content_maintype() == 'text':
                    return part.get_payload()
        elif maintype == 'text':
            self._log(6, 'text email')
            return msg.get_payload()

    def logout(self, msg):
        try:
            msg.close()
            msg.logout()
        except:
            self._log(1, 'error logging out')

if __name__ == '__main__':
    os.environ['AUTO_ADDR'] = '<email>.auto@gmail.com'
    os.environ['AUTO_PASS'] = '<password>'
    os.environ['AUTO_FROM'] = '<email>@gmail.com'
    os.environ['AUTO_PREFIX'] = 'CMD:'
    mc = MailCheck()
    M = mc.login()
    c = mc.get_commands(M)
    mc.logout(M)
    mc.process_commands(c)
