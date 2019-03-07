import setup_test, sys, getpass
from xnatum import Xnat

username = raw_input('Username: ')
password = raw_input('Password: ')
x = Xnat('XNAT_ADDRESS', username, password)

project   = raw_input('Project: ')
subject   = raw_input('Subject: ')
sess_path = raw_input('Session: ')
x.send_session(project, subject, sess_path)