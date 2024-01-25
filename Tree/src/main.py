from directory_tree import display_tree
from sys import argv

if __name__ == "__main__":
    if argv[1:]:
        display_tree(argv[1])
    else:
        display_tree()