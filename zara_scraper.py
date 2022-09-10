import sys
import requests
from bs4 import BeautifulSoup
import pickle
from tqdm import tqdm

def main() -> int:
    url = 'http://www.gutenberg.org/files/1998/1998-h/1998-h.htm'

    print('Getting...')
    page = requests.get(url)
    # page = pickle.load(open('bible.p', 'rb'))
    print('Souping...')
    soup = BeautifulSoup(page.content, 'html.parser')
    print('Finding...')
    result = soup.find_all(['h1', 'p'])

    started = False

    zara_file = open(f'data/zara.txt', 'w')

    for tag in tqdm(result):
        if tag.name == 'h1' and tag.text.strip() == 'THUS SPAKE ZARATHUSTRA.':
            started = True

        elif tag.name == 'h1' and tag.text.strip() == 'APPENDIX.':
            zara_file.close()
            break

        elif tag.name == 'p' and 'Chapter' not in tag.text:
            string = tag.text.strip().replace('\r\n      ', ' ')
            string = string.lstrip("—")

            if string.rstrip('.').isnumeric():
                continue

            print(string)
            zara_file.write(string)
            zara_file.write('\n')

    return 0

if __name__ == "__main__":
    sys.exit(main())