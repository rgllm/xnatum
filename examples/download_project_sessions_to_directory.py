#!/usr/bin/python
import argparse
import sys
import os
import glob
import getpass
import tempfile
import shutil
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
    dirpath = tempfile.mkdtemp()
    lregex = '[A-Z]{2}[0-9]{4}[A-Z]_REST[1-2]'
    xnat_sessions = xnat.download_project_sessions_to_directory(args.project, dirpath, lregex)
    print(xnat_sessions)
    shutil.rmtree(dirpath)

# init
if __name__ == '__main__':
    main()
