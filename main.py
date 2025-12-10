# Project Dependencies
import os
from colorama import Fore
from MCQ_classes import MCQs
from CustomException import print_quiz_travia, get_questions

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