from colorama import Fore

def show_translations(translations):
    if translations:
        for t in translations:
            print(f"{Fore.YELLOW} - {t}")
    else:
        print(f"{Fore.RED}No translation found.")