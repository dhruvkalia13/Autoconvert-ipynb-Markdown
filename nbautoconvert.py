#!/usr/bin/env python
import subprocess

COMMAND_GET_CHANGED_FILES = "git diff --cached --name-status"
FILE_EXTENSION_IPYNB = ".ipynb"
output_file_name = "README"
commit_message = "AutoCommit:" + output_file_name + ".md dated"

def get_changed_files(file_extension):
    # Get ipynb files from 'files to commit' git cache list.
    files = []
    output = (subprocess.run(['git', 'diff', '--name-status'], stdout=subprocess.PIPE)).stdout.decode(
        "utf-8").strip()
    file_list = output.split("\n")
    if len(file_list) == 0:
        exit()
    for line in file_list:
        if line == '0' or line == '':
            continue
        try:
            change, filename = line.strip().split('\t')
            if filename.endswith(file_extension) and change != 'D':
                files.append(filename)
        except Exception:
            raise
    return files


def git_add(file):
    args = ['git', 'add', output_file_name + ".md"]
    convert_command = ' '.join(args)
    (subprocess.run(convert_command, stdout=subprocess.PIPE)).stdout.decode("utf-8").strip()
    args = ['git', 'add', file]
    convert_command = ' '.join(args)
    (subprocess.run(convert_command, stdout=subprocess.PIPE)).stdout.decode("utf-8").strip()
    exit()

def convert(files):
    if len(files) == 0:
        exit()
    file = files[0]
    args = ['jupyter', 'nbconvert', '--to', 'markdown', file, '--output',
            output_file_name]
    convert_command = ' '.join(args)
    (subprocess.run(convert_command, stdout=subprocess.PIPE)).stdout.decode("utf-8").strip()
    print(file + " converted through hook")
    git_add(file)
    exit()


def main():
    files = get_changed_files(FILE_EXTENSION_IPYNB)
    if len(files) == 0:
        exit()
    convert(files)


if __name__ == "__main__":
    main()
