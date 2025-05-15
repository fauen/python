import subprocess
from getpass import getpass as gp

def main() -> None:
    sudo_pw = gp("Input sudo password: ")
    sudo_command = "sudo apt update; sudo apt upgrade -y"
    subprocess.run(sudo_command,
                   shell = True,
                   input = sudo_pw + "\n",
                   text = True)

if __name__ == "__main__":
    main()
