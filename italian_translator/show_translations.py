from colorama import Fore

def show_translations(soup, sentence):
    display_terms = soup.find_all('span', class_='display-term')

    if display_terms:
        print(f"{Fore.GREEN}Display terms for '{sentence}':")
        for term in display_terms:
            print(f"{Fore.YELLOW} - {term.get_text(strip=True)}")
    else:
        mt_box = soup.find(id='mt-box')
        if not mt_box:
            print(f"{Fore.RED}No translation found.")
            return

        text_spans = mt_box.find_all(class_='trg ltr')
        if len(text_spans) < 2:
            print(f"{Fore.RED}No translation found.")
            return

        translation = text_spans[1].get_text(strip=True)
        print(f"{Fore.GREEN}Translation for '{sentence}': {Fore.YELLOW}{translation}")
    print()