import sys


def setup():
	print("Setting up...")
	# We need to create pre-commit hook 
    src = '../../nb_auto_convert'
    dst = '.git/hooks/pre-commit'
    try:
        os.symlink(src, dst)
        print("Creating symbolic link from %s to %s" % (src, dst))
    except OSError as e:
        if 'File exists' in e.strerror:
            print('Err... Pre-commit hook file already exists.')
        else:
            raise e
    exit()


def main():
	# get list of all changed files
	# if ipynp file is changed, then execute the command
	


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "setup":
            setup()
    main()
