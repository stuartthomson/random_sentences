import sys
from typing import List

def main() -> int:

    with open('./data/zara.txt', 'r', encoding='utf-8') as infile:
        ls = infile.readlines()

    # Remove empty and trim
    ls: List[str] = [l for l in ls if len(l) > 0]

    ls = [l.replace('”', '"').replace('“', '"') for l in ls]

    with open('./data/zara_fixed.txt', 'w', encoding='utf-8') as outfile:
        outfile.writelines(ls)

    return 0

if __name__ == "__main__":
    sys.exit(main())