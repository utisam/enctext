import sys
import os
import argparse
from getpass import getpass
import enctext

parser = argparse.ArgumentParser()
parser.add_argument('filename')


def main():
    args = parser.parse_args()

    raw_password = getpass()

    if os.path.exists(args.filename):
        with open(args.filename, 'rb') as f:
            decrypted_string = enctext.decrypt(raw_password, f.read())
            print(decrypted_string.decode('utf-8'), end="",flush=True)

    return 0

if __name__ == '__main__':
    sys.exit(main())
