
    
#!/usr/bin/python
import argparse
import sys
import os
import getpass
from xnatum import Xnat

def main():
    parser = argparse.ArgumentParser(description='XNAT sender')
    parser.add_argument('-project', help='Project ID', required=True)
    parser.add_argument('-subject', help='Subject ID', required=True)
    parser.add_argument('-studydir', help='Study directory with all sequences', required=True)
    parser.add_argument('-sequences', nargs='+', help='List of sequences to be uploaded [if not defined, all sequences]')
    parser.add_argument('-session', help='Session', default='1')
    parser.add_argument('-server', help='Server for XNAT connection', required=True)
    parser.add_argument('-username', help='Username for XNAT connection', required=True)
    parser.add_argument('-password', help='Password for XNAT connection', required=True)
    args = parser.parse_args()

    xnat = Xnat(args.server, args.username, args.password)
    
    sequences = os.listdir(args.studydir) if not args.sequences else args.sequences
    xnat.send_session(args.project, args.subject, args.studydir, sequences, session=args.session)

# init
if __name__ == '__main__':
    main()