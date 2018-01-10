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
import imp
import inspect

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
        self.modules = {}
        self.load_commands()

    def _log(self, priority, msg):
        if priority <= VERBOSITY:
            print(msg)

    def run(self):
        """
        The login, get_commands, logout, process_commands sequence
        """
        M = self.login()
        c = self.get_commands(M)
        self._log(1, c)
        self.logout(M)
        self.process_commands(c)

    def login(self):
        """
        login to the auto.email account using imaplib.
        Returns: an IMAP4_SSL object
        """
        try:
            mail = imaplib.IMAP4_SSL('imap.gmail.com')
            mail.login(os.environ['AUTO_ADDR'], os.environ['AUTO_PASS'])
            mail.select('inbox')
            self._log(1, 'Logging in as: {}'.format(os.environ['AUTO_ADDR']))
            return mail
        except:
            self._log(1, 'error logging in')

    def get_commands(self, mail):
        """
        Open up the auto.email account and read unread messages 
        that start with the env(AUTO_PREFIX)
        Returns: the text of the message
        """
        result, data = mail.uid('search', None, '(HEADER Subject "{}")'.format(os.environ['AUTO_PREFIX']))
        match = data[0].split()[-1]
        result, data = mail.uid('fetch', match, '(RFC822)')
        raw = data[0][1]

        msg = email.message_from_string(raw)
        sender = email.utils.parseaddr(msg['From'])[-1]
        self._log(1, 'Sender: {}'.format(sender))
        if sender == os.environ['AUTO_FROM']:
            self._log(6, 'passed sender test')
            if msg['Subject'].startswith(os.environ['AUTO_PREFIX']):
                self._log(6, 'passed subject test')
                print('From: {}'.format(msg['From']))
                print('Subj: {}'.format(msg['Subject']))
                print('Rcvd: {}'.format(msg['Date']))
                text = self.get_first_text_block(msg)
                #print(text)
                return text.strip()

    def load_commands(self):
        """
        Search the 'commands' directory and find any command 'plugin'
        python files. Do some simple checking and 'register' them
        with the class
        """
        cmd_dir = os.path.join(os.getcwd(), 'commands')
        all_files = os.listdir(cmd_dir)
        self._log(6, all_files)
        py_files = []
        for tf in all_files:
            tf_path = os.path.join(cmd_dir, tf)
            self._log(6, os.path.isfile(tf_path))
            if os.path.isfile(tf_path) and tf_path.endswith('.py'):
                py_files.append(tf_path)
                self._log(6, tf_path)

        pysource = None
        for srctype in imp.get_suffixes():
            if srctype[0] == '.py':
                pysource = srctype

        loaded_func_names = []
        for tf in py_files:
            py_name = os.path.splitext(os.path.basename(tf))[0]
            self._log(6, py_name)
            with open(tf, 'r') as fp:
                module = imp.load_module(py_name, fp, tf, pysource)
                self._log(6, module)
            for (name, obj) in module.__dict__.items():
                self._log(6, 'is func: {}'.format(inspect.isfunction(obj)))
                self._log(6, 'name: {}\npyname: {}'.format(name, py_name))
                if inspect.isfunction(obj) and name == py_name:
                    self._log(6, name)
                    if name not in loaded_func_names:
                        self.modules[name] = obj
                        self._log(1, 'loaded command: {}'.format(name))
                        loaded_func_names.append(name)

    def process_commands(self, cmd):
        """
        We previously grabbed our commands from email. Here is where 
        we determing if the email refers to a command that this computer
        can execute. If it can, it will
        """
        self._log(1, 'here is where we process our commands')
        if len(cmd):
            action, arg_string = cmd.split('%')
            arg_list = arg_string.strip().split(',')
            if action.lower() in self.modules:
                self.modules[action.lower()](*arg_list)

    def get_first_text_block(self, msg):
        """
        Get the first text block in a potentially multipart email message
        """
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
        """
        logout of the auto.email account
        """
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
    mc.run()
