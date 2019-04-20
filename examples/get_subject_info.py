import argparse
import sys
import os
import glob
import getpass
from xnatum import Xnat, util
from pprint import pprint

def main():
    parser = argparse.ArgumentParser(description='Get Subject Info')
    parser.add_argument('-subject', required=True, help='Subject ID')
    parser.add_argument('-project', required=True, help='Project ID')
    parser.add_argument('-server', help='Server for XNAT connection', required=True)
    parser.add_argument('-username', help='Username for XNAT connection', required=True)
    parser.add_argument('-password', help='Password for XNAT connection', required=True)
    args = parser.parse_args()

    # Creating connection and load experiment object
    xnat = Xnat(args.server, args.username, args.password)
    pprint(xnat.get_subject_info(args.project, args.subject))

# init
if __name__ == '__main__':
    main()