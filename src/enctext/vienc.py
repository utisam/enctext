import sys
import os
import argparse
import subprocess
from getpass import getpass
import enctext

parser = argparse.ArgumentParser()
parser.add_argument('filename')


def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    for path in os.environ["PATH"].split(os.pathsep):
        path = path.strip('"')
        exe_file = os.path.join(path, program)
        if is_exe(exe_file):
            return exe_file

    return None


def main():
    args = parser.parse_args()

    vipe_path = which('vipe')
    if vipe_path is None:
        print("Error: cannot find 'vipe'", file=sys.stderr)
        return -1

    raw_password = getpass()

    vipe_process = subprocess.Popen([vipe_path],
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE)

    if os.path.exists(args.filename):
        with open(args.filename, 'rb') as f:
            encrypted_text = enctext.decrypt(raw_password, f.read())
    else:
        encrypted_text = None
    stdoutdata, _ = vipe_process.communicate(encrypted_text)

    if vipe_process.returncode == 0:
        with open(args.filename, 'wb') as f:
            f.write(enctext.encrypt(raw_password, stdoutdata))
    else:
        print('Error: vipe failed; You must check the temporary directory')
        return vipe_process.returncode

    return 0

if __name__ == '__main__':
    sys.exit(main())
