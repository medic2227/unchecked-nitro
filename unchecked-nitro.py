import random
import string
import os

try:
    from colorama import Fore, Style, init
except ImportError:
    os.system('pip install colorama')
    from colorama import Fore, Style, init

try:
    from art import text2art
except ImportError:
    os.system('pip install art')
    from art import text2art

init()

def generate_discord_gift_link():
    base_url = "https://discord.gift/"
    random_code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return base_url + random_code

def main():
    os.system('clear')
    print(Fore.GREEN + text2art("Unchecked  Nitro\nGenerator"))
    try:
        print(' ')
        num_links = int(input(Fore.YELLOW + "[?] How many links do you want to generate: "))
        print(' ')
        generated_links = [generate_discord_gift_link() for _ in range(num_links)]
        for link in generated_links:
            print(Fore.GREEN + link)

    except ValueError:
        print(' ')
        print(Fore.RED + "[!] Enter a valid number!")
        print(' ')

if __name__ == "__main__":
    main()
