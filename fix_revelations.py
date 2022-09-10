import sys
from typing import List

def main() -> int:

    with open('./data/bible/Revelation.txt', 'r', encoding='utf-8') as infile:
        ls = infile.readlines()

    # Remove empty and trim
    ls: List[str] = [l for l in ls if len(l.strip()) > 0]

    ls = [l.replace('”', '"').replace('“', '"') for l in ls]

    with open('./data/revelation_fixed.txt', 'w', encoding='utf-8') as outfile:
        outfile.writelines(ls)

    return 0

if __name__ == "__main__":
    sys.exit(main())