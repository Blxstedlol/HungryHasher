import requests
import hashlib
import time
from colorama import Fore
alg = input('Enter Algorithm: ').lower()
goal = input('Enter Hash to crack: ')
file = input('Enter Password List Path: ')

          
lines_counter = 0
start_time = time.time()
        
try:
    with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                    line = line.strip()
                    if line:
                            plaintext = line
                    if alg == 'sha256':
                                    hashed = hashlib.sha256(plaintext.encode('utf-8')).hexdigest()
                                    if hashed == goal:
                                            lines_counter += 1
                                            current_time = time.time()  # Get the current time
                                            total_elapsed = current_time - start_time
                                            
                                            print(f'{Fore.GREEN}PASSWORD FOUND!!!\n {goal} : {plaintext}\n [Line: {lines_counter}\n Time: {total_elapsed}\n Algorithm: {alg}] {Fore.RESET}')
                                            
                                            exit()
                                    print(hashed)
                                    lines_counter += 1
                    if alg == 'sha512':
                                    hashed = hashlib.sha512(plaintext.encode('utf-8')).hexdigest()
                                    if hashed == goal:
                                            lines_counter += 1
                                            current_time = time.time()  # Get the current time
                                            total_elapsed = current_time - start_time
                                            
                                            print(f'{Fore.GREEN}PASSWORD FOUND!!!\n {goal} : {plaintext}\n [Line: {lines_counter}\n Time: {total_elapsed}\n Algorithm: {alg}] {Fore.RESET}')
                                            exit()
                                    print(hashed)
                                    lines_counter += 1
                    if alg == 'sha224':
                                    hashed = hashlib.sha224(plaintext.encode('utf-8')).hexdigest()
                                    if hashed == goal:
                                            lines_counter += 1
                                            current_time = time.time()  # Get the current time
                                            total_elapsed = current_time - start_time
                                            
                                            print(f'{Fore.GREEN}PASSWORD FOUND!!!\n {goal} : {plaintext}\n [Line: {lines_counter}\n Time: {total_elapsed}\n Algorithm: {alg}] {Fore.RESET}')
                                            exit()
                                    print(hashed)
                                    lines_counter += 1
                    if alg == 'sha1':
                                    hashed = hashlib.sha1(plaintext.encode('utf-8')).hexdigest()
                                    if hashed == goal:
                                            lines_counter += 1
                                            current_time = time.time()  # Get the current time
                                            total_elapsed = current_time - start_time
                                            
                                            print(f'{Fore.GREEN}PASSWORD FOUND!!!\n {goal} : {plaintext}\n [Line: {lines_counter}\n Time: {total_elapsed}\n Algorithm: {alg}] {Fore.RESET}')
                                            exit()
                                    print(hashed)
                                    lines_counter += 1
                    if alg == 'md5':
                                    hashed = hashlib.md5(plaintext.encode('utf-8')).hexdigest()
                                    if hashed == goal:
                                            lines_counter += 1
                                            current_time = time.time()  # Get the current time
                                            total_elapsed = current_time - start_time
                                            
                                            print(f'{Fore.GREEN}PASSWORD FOUND!!!\n {goal} : {plaintext}\n [Line: {lines_counter}\n Time: {total_elapsed}\n Algorithm: {alg}] {Fore.RESET}')
                                            exit()
                                    print(hashed)
                                    lines_counter += 1
except FileNotFoundError as e:
        y_n = input('Do you want to install a password list? Y/N: ').lower()
        if y_n == 'y':
            with open('passwords.txt', 'w') as file:
                url = 'https://raw.githubusercontent.com/berandal666/Passwords/master/10_million_password_list_top_1000000.txt'
                response = requests.get(url)
                content = response.content.decode('utf-8') # Decode content to a string
                print('Downloading Password List...')  
                for line in content.splitlines():  # Split the content into lines
                    file.write(f'{line}\n')
        if y_n == 'n':
                print('Alright, Thanks for using HungryHasher!')
        else:
                print(y_n, 'Is Invalid, please choose Y/N')
if __name__ == '__main__':    
    hash(alg)