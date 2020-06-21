#!/usr/bin/env python
import subprocess
import sys
import os

COMMAND_GET_CHANGED_FILES = "git diff --cached --name-status"
FILE_EXTENSION_IPYNB = ".ipynb"
output_file_name = "README"


def get_changed_files():
    # Get ipynb files from 'files to commit' git cache list.
    files = []
    filelist1 = (subprocess.run(['git', 'diff', '--cached', '--name-status'], stdout=subprocess.PIPE)).stdout.decode(
        "utf-8").strip()
    for line in filelist1.split("\n"):
        if line == '0':
            continue
        try:
            change, filename = line.strip().split('\t')
            print(filename)
            if filename.endswith(FILE_EXTENSION_IPYNB) and change != 'D':
                files.append(filename)
        except Exception:
            raise
    return files


def convert(file):
    print("inside convert func")
    output_dir = os.getcwd()
    print("output_dir is " + output_dir)
    args = ['jupyter', 'nbconvert', '--to', 'markdown', file, '--output',
                       output_file_name]
    convert_command = ' '.join(args)
    print("convert command is " + convert_command)
    out = (subprocess.run(convert_command, stdout=subprocess.PIPE)).stdout.decode("utf-8").strip()
    print(file + " converted ")
    print(out)
    exit()


def main():
    files = get_changed_files()
    if len(files) == 0:
        exit()
    convert(files)


if __name__ == "__main__":
    main()
