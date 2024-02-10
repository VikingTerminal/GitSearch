import requests
import time

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
LIGHT_RED = "\033[101m"
RESET = "\033[0m"

def github_search(query):
    github_api_url = f"https://api.github.com/search/repositories?q={query}"
    response = requests.get(github_api_url)
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        print(f"{RED}Si è verificato un problema con la ricerca su GitHub.{RESET}")
        return []

def print_with_typing_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.02)  
    print()

def main():
    save_to_file = input(f"{CYAN}Vuoi salvare la ricerca in un file 'ricerchegit.txt'? (yes/no): {RESET}")

    if save_to_file.lower() == 'yes':
        file = open("ricerchegit.txt", "w")
    else:
        file = None

    while True:
        user_input = input(f"{CYAN}Inserisci la query di ricerca per GitHub (o 'exit' per uscire): {RESET}")
        
        if user_input.lower() == 'exit':
            if file:
                file.close()
            print_with_typing_effect(f"{GREEN}Grazie per aver usato questo tool. Creato da t.me/VikingTerminal{RESET}")
            break
        
        if user_input.strip() == '':
            print_with_typing_effect(f"{YELLOW}Per favore, inserisci una query valida.{RESET}")
            continue

        print_with_typing_effect("Ricerca in corso...")
        results = github_search(user_input)
        if results:
            for result in results[:15]:   
                repo_name = result.get('full_name', 'N/A')
                repo_url = result.get('html_url', 'N/A')
                output = f"{GREEN}Repository: {repo_name}\nURL: {repo_url}\n{RESET}"
                print_with_typing_effect(output)
                if file:
                    file.write(output)
        else:
            print_with_typing_effect(f"{LIGHT_RED}Nessun risultato trovato per la tua ricerca.{RESET}")

if __name__ == '__main__':
    main()
