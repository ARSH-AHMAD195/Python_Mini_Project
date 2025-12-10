import random
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