from typing import List

def fix_file(
    filename,
    outfilename,
    filter_predicate=None,
    apply_predicate=None
) -> None:
    with open(filename, 'r', encoding='utf-8') as infile:
        ls = infile.readlines()

    # Remove empty and trim
    ls: List[str] = [l for l in ls if len(l.strip()) > 0]

    # 'Fix' punctuation
    ls = [
        l.replace('”', '"') \
         .replace('“', '"') \
         .replace('‘', "'") \
         .replace('’', "'") \
        for l in ls
    ]

    if filter_predicate:
        ls = [l for l in ls if filter_predicate(l)]

    if apply_predicate:
        ls = [apply_predicate(l) for l in ls]

    with open(outfilename, 'w', encoding='utf-8') as outfile:
        outfile.writelines(ls)


if __name__ == '__main__':
    fix_file('./data/zara.txt', './data/fixed/zara.txt')
    fix_file(
        './data/bible/Genesis.txt', './data/fixed/Genesis.txt',
        filter_predicate=lambda x: 'begat' not in x
    )
    fix_file('./data/bible/Revelation.txt', './data/fixed/Revelation.txt')
