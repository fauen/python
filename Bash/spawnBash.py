import subprocess, sys

# This is Python specific, it will grab the command from the command line arguments.
command = sys.argv[1:]

subprocess.run(command[0], shell = True, executable="/bin/bash")