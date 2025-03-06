import requests
from colorama import Fore, Style, init

init(autoreset=True)

def check_onion_status(onion_url):
    try:
        proxies = {
            "http": "socks5h://127.0.0.1:9050",
            "https": "socks5h://127.0.0.1:9050"
        }
        response = requests.get(onion_url, proxies=proxies, timeout=10)
        if response.status_code == 200:
            print(Fore.GREEN + f"\n🟢 {onion_url} is Active")
        else:
            print(Fore.RED + f"\n🔴 {onion_url} is Inactive or Unreachable")
    except requests.RequestException:
        print(Fore.RED + f"\n🔴 {onion_url} is Inactive or Unreachable")

def main():
    while True:
        onion_domain = input(Fore.CYAN + "\n🔵 Enter the .onion domain or full URL to check: ")
        if not onion_domain.endswith(".onion"):
            print(Fore.YELLOW + "\n🟡 [WARNING] Invalid .onion domain. Please enter a valid .onion address.")
            continue
        
        onion_url = f"http://{onion_domain}" if not onion_domain.startswith("http") else onion_domain
        check_onion_status(onion_url)
        
        choice = input(Fore.MAGENTA + "\n🔵 Do you want to check another site? (yes/no): ").strip().lower()
        while choice not in ['yes', 'no']:
            print(Fore.RED + "\n[ERROR] Invalid input! Please enter 'yes' or 'no'.")
            choice = input(Fore.MAGENTA + "\n🔵 Do you want to check another site? (yes/no): ").strip().lower()
        
        if choice == 'no':
            print(Fore.CYAN + "\nExiting the program. Stay safe!")
            break

if __name__ == "__main__":
    main()
