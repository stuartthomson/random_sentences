import sys
import requests
from bs4 import BeautifulSoup
import pickle
from tqdm import tqdm


def main() -> int:
    url = 'https://www.gutenberg.org/files/10900/10900-h/10900-h.htm'

    print('Getting...')
    page = requests.get(url)
    # page = pickle.load(open('bible.p', 'rb'))
    print('Souping...')
    soup = BeautifulSoup(page.content, 'html.parser')
    print('Finding...')
    result = soup.find_all(['h1', 'p'])

    started = False

    for tag in tqdm(result):
        if tag.name == 'h1' and 'Gutenberg' not in tag.text:
            book_name = tag.text.strip()
            book_file = open(f'data/bible/{book_name}.txt', 'w')
            started = True
        elif tag.name == 'p' and 'Chapter' not in tag.text and started:
            string = tag.text.strip().replace('\r\n      ', ' ')
            try:
                string = string.split(' ', 1)[1]
            except IndexError:
                pass

            book_file.write(string)
            book_file.write('\n')

    return 0

if __name__ == "__main__":
    sys.exit(main())