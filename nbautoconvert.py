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
    output = (subprocess.run(['git', 'diff', '--name-status'], stdout=subprocess.PIPE)).stdout.decode(
        "utf-8").strip()
    file_list = output.split("\n")
    print("file_list has " + str(len(file_list)))
    if len(file_list) == 0:
        exit()
    for line in file_list:
        print("line is " + line)
        if line == '0':
            continue
        try:
            change, filename = line.strip().split('\t')
            if filename.endswith(FILE_EXTENSION_IPYNB) and change != 'D':
                files.append(filename)
        except Exception:
            raise
    return files


def convert(files):
    if len(files) == 0:
        exit()
    file = files[0]
    output_dir = os.getcwd()
    args = ['jupyter', 'nbconvert', '--to', 'markdown', file, '--output',
            output_file_name]
    convert_command = ' '.join(args)
    (subprocess.run(convert_command, stdout=subprocess.PIPE)).stdout.decode("utf-8").strip()
    print(file + " converted through hook")
    exit()


def main():
    files = get_changed_files()
    if len(files) == 0:
        exit()
    convert(files)


if __name__ == "__main__":
    main()
