#!/usr/bin/python
import argparse
import sys
import os
import glob
import getpass
from xnatum import Xnat, util

def main():
    parser = argparse.ArgumentParser(description='Download session')
    parser.add_argument('-project', required=True, help='Project ID')
    parser.add_argument('-server', help='Server for XNAT connection', required=True)
    parser.add_argument('-username', help='Username for XNAT connection', required=True)
    parser.add_argument('-password', help='Password for XNAT connection', required=True)
    args = parser.parse_args()

    # Creating connection and load experiment object
    xnat = Xnat(args.server, args.username, args.password)
    xnat_sessions = xnat.download_project_sessions(args.project)
    print(xnat_sessions)

# init
if __name__ == '__main__':
    main()