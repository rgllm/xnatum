#!/usr/bin/python
import argparse
import sys
import os
import glob
import getpass
from xnatum import Xnat, util

def main():
    parser = argparse.ArgumentParser(description='Get List of Subjects')
    parser.add_argument('-project', required=True, help='Project ID')
    parser.add_argument('-server', help='Server for XNAT connection', required=True)
    parser.add_argument('-username', help='Username for XNAT connection', required=True)
    parser.add_argument('-password', help='Password for XNAT connection', required=True)
    args = parser.parse_args()

    xnat = Xnat(args.server, args.username, args.password)
    print(xnat.get_list_subjects(args.project))

# init
if __name__ == '__main__':
    main()