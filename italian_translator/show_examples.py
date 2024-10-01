import re
from colorama import Fore, Style

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

        cleaned_text_src = re.sub(r'<.*?>', '#', text_src)
        cleaned_text_trg = re.sub(r'<.*?>', '#', text_trg)

        cleaned_text_src = cleaned_text_src.replace('##', '#')
        cleaned_text_trg = cleaned_text_trg.replace('##', '#')
        cleaned_text_src = cleaned_text_src.replace('###', '#')
        cleaned_text_trg = cleaned_text_trg.replace('###', '#')
        cleaned_text_src = cleaned_text_src.replace('####', '#')
        cleaned_text_trg = cleaned_text_trg.replace('####', '#')

        cleaned_text_src = re.sub(r'#(.*?)#', lambda m: f"{Fore.BLUE}{m.group(1)}{Style.RESET_ALL}", cleaned_text_src)
        cleaned_text_trg = re.sub(r'#(.*?)#', lambda m: f"{Fore.BLUE}{m.group(1)}{Style.RESET_ALL}", cleaned_text_trg)

        separated_text_src = '\n'.join(cleaned_text_src.strip().split('\n'))
        separated_text_trg = '\n'.join(cleaned_text_trg.strip().split('\n'))

        print(f' - {separated_text_src}')
        print(f' - {separated_text_trg}')
        print()

