import subprocess

def main() -> None:
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

if __name__ == "__main__":
    main()
