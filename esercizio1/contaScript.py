import os
import sys

def count_script(folder):
    """
    Count the number of scripts in a folder and its subfolders. Then group by shebang
    and return the result as a dictionary.
    :param folder: the folder to scan
    :return: a dictionary with the shebang as key and the number of scripts as value
    """

    counter = dict()

    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".sh"):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    first_line = f.readline().strip()

                if first_line.startswith("#!"):
                    counter[first_line] = counter.get(first_line, 0) + 1

    return counter

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python contaScript.py <folder>")
        sys.exit(1)

    if not os.path.isdir(sys.argv[1]):
        print(f"{sys.argv[1]} is not a folder")
        print("Usage: python contaScript.py <folder>")
        sys.exit(1)

    folder = sys.argv[1]
    counter = count_script(folder)
    for script, count in counter.items():
        print(f"{script}: {count}")