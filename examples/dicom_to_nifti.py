#!/usr/bin/python
import argparse
import sys
import os
import glob
import getpass
from xnatum import Xnat, util

def main():
    parser = argparse.ArgumentParser(description='Convert DICOM to Nifti session')
    parser.add_argument('-input', help='DICOM folder', required=True)
    parser.add_argument('-output', help='Output Folder', required=True)
    parser.add_argument('-server', help='Server for XNAT connection', required=True)
    parser.add_argument('-username', help='Username for XNAT connection', required=True)
    parser.add_argument('-password', help='Password for XNAT connection', required=True)
    args = parser.parse_args()

    xnat = Xnat(args.server, args.username, args.password)

    xnat.convert_dicom_nifti(args.input, args.output)

    print('File converted.')

# init
if __name__ == '__main__':
    main()