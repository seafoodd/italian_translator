import re
from colorama import Fore, Style

def clean_text(text):
    text = re.sub(r'<.*?>', '#', text)
    for i in range(2, 5):
        text = text.replace('#' * i, '#')
    text = re.sub(r'#(.*?)#', lambda m: f"{Fore.BLUE}{m.group(1)}{Style.RESET_ALL}", text)
    return '\n'.join(text.strip().split('\n'))

def show_examples(soup, num_examples):
    examples_content = soup.find('section', id='examples-content')

    if not examples_content:
        print("No examples-content div found.")
        return

    examples = examples_content.find_all('div', class_='example')
    print(f"{Fore.GREEN}Examples:")

    for example in examples[:num_examples]:
        src_div = example.find('div', class_='src')
        trg_div = example.find('div', class_='trg')
        text_src = src_div.find('span', class_='text').decode_contents()
        text_trg = trg_div.find('span', class_='text').decode_contents()

        cleaned_text_src = clean_text(text_src)
        cleaned_text_trg = clean_text(text_trg)

        print(f' - {cleaned_text_src}')
        print(f' - {cleaned_text_trg}')
        print()

