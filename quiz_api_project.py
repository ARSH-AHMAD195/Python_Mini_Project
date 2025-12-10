# Project Dependencies
import requests
import random
import os
from colorama import Fore
from typing import Any
from abc import ABC, abstractmethod

# Question abstract class
class Question(ABC):
    @abstractmethod
    def display(self) -> str:
        pass

    @abstractmethod
    def check_answer(self, answer: str)->bool:
        pass

# MCQs sub-class of Question for handling MCQs
class MCQs(Question):
    def __init__(self, ques: str, correct_ans: str, incorrect_ans: Any):
        self._question = ques
        self._correct_answer = correct_ans

        self._options = [opt for opt in incorrect_ans]
        self._options.append(correct_ans)

    def display(self) -> str: # display(self): It displays the MCQ and takes answer and returns answer 
        print(f"\t\tQ. {self._question}")
        ch = 'A'
        options = self._options
        random.shuffle(options)
        print("\t\t", end="")
        for i,opt in enumerate(options):
            ch = chr(ord(ch)+i)
            print(f"{ch}) {opt}", end="     ")

        answer = input("\n\t\tEnter answer: ")
        return answer

    def check_answer(self, answer: str): # check_answer(self, answer: str): It takes answer as parameter and return true if correct else false
        return answer.lower() == self._correct_answer.lower()
    
    def get_correct_answer(self): # get_correct_answer(self): It returns correct answer
        return self._correct_answer
        
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



# Main Application
def app():    
    score = 0
    loop = 'y'
    while ((loop == 'y' or loop == 'Y') and (loop != 'n' or loop != 'N')):
        os.system("cls")
        print_quiz_travia()
        print(Fore.RESET)
        choice = int(input("\t\tPress 1 to Start Quiz\n\t\tPress 2 to Quit\n\n\t\tEnter Your choice: "))
        
        if(choice == 1): # The quiz starts if user press 1
            topics = {1:{"title":"General Knowledge","code":9},
                      2:{"title":"Entertainment: Books","code":10},
                      3:{"title":"Entertainment: Film","code":11},
                      4:{"title":"Entertainment: Music","code":12},
                      5:{"title":"Entertainment: Musicals & Theaters","code":13},
                      6:{"title":"Entertainment: Television","code":14},
                      7:{"title":"Entertainment: Video Games","code":15},
                      8:{"title":"Entertainment: Board Games","code":16},
                      9:{"title":"Science & Nature","code":17},
                      10:{"title":"Science: Computers","code":18},
                      11:{"title":"Science: Mathematics","code":19}
                      }
            
            os.system("cls")
            print_quiz_travia()
            print(Fore.RESET)

            print("\t\tQuiz Topics\n\t\t=========================\n")
            for idx in range(len(topics)):
                print(f"\t\tPRESS {idx+1} for {topics[idx+1]["title"]}")
            
            category = int(input("\t\tChoose Category: "))
            no_of_questions = int(input("\t\tEnter number of questions you want: "))
            
            url = f"https://opentdb.com/api.php?amount={no_of_questions}&category={topics[category]["code"]}&type=multiple"
            response = get_questions(url)
            questions = response["results"]
            MCQ = []
            for idx in range(len(questions)):
                if(questions[idx].get("type") == "multiple"):
                    q = questions[idx].get("question")
                    ca = questions[idx].get("correct_answer")
                    ia = questions[idx].get("incorrect_answers")

                    q = q.replace("&#039;", "'")
                    q = q.replace("&quot;", "\"")

                    ca = ca.replace("&#039;", "'")
                    ca = ca.replace("&quot;", "\"") 
                    
                    incorrect_ans = []
                    for opt in ia:
                        opt.replace("&#039;", "'")
                        opt.replace("&quot;", "\"")

                        incorrect_ans.append(opt)

                    mcq = MCQs(q, ca, incorrect_ans)
                    MCQ.append(mcq)
            score = 0
            for mcq in MCQ:
                os.system("cls")
                print_quiz_travia()
                print(Fore.RESET)
                print(f"\t\tTOPIC: {topics[category]["title"]}")
                if mcq.check_answer(mcq.display().strip()):
                    score+=10
                print()

            # Final Score Output Screen
            os.system("cls")
            print_quiz_travia()
            print(Fore.RESET)
            print(f"\t\tTOPIC: {topics[category]["title"]}")
            print(f"\t\tCORRECT: {int(score/10)}")
            print(f"\t\tINCORRECT: {int(no_of_questions - (score/10))}")
            print(f"\t\tFINAL SCORE: {int(score/10)} out of {no_of_questions}")
            print("\n\t\t------------- X -------------\n\t\t\tCorrect Answers\n\t\t------------- X -------------")
            for idx, ca in enumerate(MCQ):
                print(f"\t\tQ{idx+1}. {ca.get_correct_answer()}")
            loop = input("\t\tDo you want to continue? [y/N]: ")

        elif(choice == 2): 
            break
        else:
            print("\n\t\tInvalid input try again!")
    
app()