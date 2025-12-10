import requests
from colorama import Fore
from typing import Any

class NoServerResponseException(Exception): # This is a custom exception for no response from server
    pass


def get_questions(url: str)->Any: # get_questions(url: str): It takes url as parameter and returns response data
    try:
        response = requests.get(url)
        if response.status_code == 200:  
            data = response.json()
            return data
        else:
            raise NoServerResponseException

    except requests.RequestException as e:
        print(f"Error in retriving questions: {e}")
    except NoServerResponseException:
        print("No server response. Try connecting to internet.")

def print_quiz_travia(): # print_quiz_travia(): It prints Quiz Travia ASCII Art
    print(Fore.GREEN,"\t\t________        .__         ___________                  .__        ")
    print(Fore.GREEN,"\t\t\\_____  \\  __ __|__|_______ \\__    ___/___________ ___  _|__|____   ")
    print(Fore.GREEN,"\t\t /  / \\  \\|  |  \\  \\___   /   |    |  \\_  __ \\__   \\  \\/ /  \\__  \\  ")
    print(Fore.GREEN,"\t\t/   \\_/.  \\  |  /  |/    /    |    |   |  | \\// __  \\   /|  |/ __ \\_")
    print(Fore.GREEN,"\t\t\\_____\\ \\_/____/|__/_____ \\   |____|   |__|  (____  /\\_/ |__(____  /")
    print(Fore.GREEN,"\t\t       \\__>              \\/                       \\/             \\/ ")