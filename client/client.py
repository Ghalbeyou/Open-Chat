import json
import os
from time import sleep
import requests
sv_ip = "127.0.0.1"
sv_port = 8300
def send_message(user):
    m = input('Your Message > ')
    r = requests.post(f'http://{sv_ip}:{sv_port}/sendMessages', {
        'author': user,
        'message': m
    })
    responses = r.json()
    if responses["message"] == "Message sent!":
        fetch_msg(user)
    else:
        if responses["message"] == "Empty message":
            print("Your're Message is empty! try again in 3 seconds!")
            sleep(3)
            fetch_msg(user)
        if responses["message"] == "Empty name":
            print("You're username is empty! try again in 3 seconds!")
            sleep(3)
            main()
        if responses["message"] == "Bad Words/Illegial Words":
            print("You're message don't send because you're message contains illegial/bad words. try again in 2 seconds!")
            sleep(2)
            fetch_msg(user)
        print(f"Error: {responses['message']}\nPress any key to reload...")
        os.system('pause > nul')
        fetch_msg(user)
def fetch_msg(user):
    os.system('cls')
    r = requests.get(f'http://{sv_ip}:{sv_port}/getMessages')
    msg = r.json()
    if msg:
        for i in msg:
            print(f'[{i["time"]}] {i["author"]} > {i["message"]}\n')
    else:
        print(" No Messages!\n")
    send_message(user)
def main():
    print("Welcome to open chat!\nWith this app, you can chat without socket or ...\n")
    user = input('Username > ')
    sv_ip = input('Server IP > ')
    sv_port = input('Server Port > ')
    os.system('cls')
    print(f'Connecting to {sv_ip}:{sv_port}')
    r = requests.get(f'http://{sv_ip}:{sv_port}/getUsers')
    if r.status_code == 200:
        print(f'Successfully connected!\nFetching messages ...')
        fetch_msg(user)
    else:
        print(f'Faild to connect or server/client is outdated.\nUpdate => https://github.com/ghalbeyou/open-chat')
if __name__ == '__main__':
    main()