import subprocess

def main() -> None:
    subprocess.run(["brew", "upgrade"])
    subprocess.run(["brew", "search", "neovim"])

if __name__ == "__main__":
    main()
