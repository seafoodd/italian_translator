import sys
import urllib.parse

import requests
from bs4 import BeautifulSoup
from colorama import Fore, init

from .show_translations import show_translations
from .show_examples import show_examples


init(autoreset=True)

def print_help():
    help_text = """
    Usage:
        italian-translator <sentence>

    Options:
        --reverse, -R       Translate from the specified language to Italian.
        --language, -L      Specify the target language (default is English).
        --examples, -E      Number of examples to display (default is 3).
        --help, -h          Show this help message and exit.
    """
    print(help_text)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print_help()
        return

    # PARSE COMMAND LINE ARGUMENTS
    reverse = False
    if '--reverse' in sys.argv or '-R' in sys.argv:
        reverse = True
        sys.argv.remove('--reverse') if '--reverse' in sys.argv else sys.argv.remove('-R')

    language = "english"
    if '--language' in sys.argv or '-L' in sys.argv:
        lang_index = sys.argv.index('--language') if '--language' in sys.argv else sys.argv.index('-L')
        language = sys.argv[lang_index + 1]
        del sys.argv[lang_index:lang_index + 2]

    examples = 3
    if '--examples' in sys.argv or '-E' in sys.argv:
        example_index = sys.argv.index('--examples') if '--examples' in sys.argv else sys.argv.index('-E')
        examples = int(sys.argv[example_index + 1])
        del sys.argv[example_index:example_index + 2]


    # GET THE SOUP
    sentence = ' '.join(sys.argv[1:])

    encoded_sentence = urllib.parse.quote(sentence)
    if reverse:
        url = f"https://context.reverso.net/translation/{language}-italian/{encoded_sentence}"
    else:
        url = f"https://context.reverso.net/translation/italian-{language}/{encoded_sentence}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"{Fore.RED}Failed to retrieve the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # SHOW DISPLAY TERMS
    show_translations(soup, sentence)

    # SHOW EXAMPLES
    show_examples(soup, examples)

if __name__ == "__main__":
    main()