#!/usr/bin/env python
import os
import subprocess
COMMAND_GET_CHANGED_FILES = "git diff --cached --name-status"
files = []

def system(*args, **kwargs):
    """Run system command."""
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out

filelist = system('git', 'diff', '--cached', '--name-status').strip()
print(filelist)
for line in filelist.split('\n'):
    if line == '':
        continue
    try:
        action, filename = line.strip().split('\t')
        print(filename)
        if filename.endswith('.py') and action != 'D':
            files.append(filename)
    except Exception:
        raise
print(files)