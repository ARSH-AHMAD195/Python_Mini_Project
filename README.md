# 🎯 Quiz Travia

A terminal-based interactive quiz application built in Python.
It fetches live multiple-choice questions from the Open Trivia Database API and evaluates user performance with scoring, ASCII visuals, and colored output.

# 🖼️ Example Output
```
                ________        .__         ___________                  .__        
                \_____  \  __ __|__|_______ \__    ___/___________ ___  _|__|____   
                 /  / \  \|  |  \  \___   /   |    |  \_  __ \__   \  \/ /  \__  \  
                /   \_/.  \  |  /  |/    /    |    |   |  | \// __  \   /|  |/ __ \_
                \_____\ \_/____/|__/_____ \   |____|   |__|  (____  /\_/ |__(____  /
                       \__>              \/                       \/             \/ 

                Press 1 to Start Quiz
                Press 2 to Quit

                Enter Your choice:
```
```
                ________        .__         ___________                  .__        
                \_____  \  __ __|__|_______ \__    ___/___________ ___  _|__|____   
                 /  / \  \|  |  \  \___   /   |    |  \_  __ \__   \  \/ /  \__  \  
                /   \_/.  \  |  /  |/    /    |    |   |  | \// __  \   /|  |/ __ \_
                \_____\ \_/____/|__/_____ \   |____|   |__|  (____  /\_/ |__(____  /
                       \__>              \/                       \/             \/ 

                Quiz Topics
                =========================

                PRESS 1 for General Knowledge
                PRESS 2 for Entertainment: Books
                PRESS 3 for Entertainment: Film
                PRESS 4 for Entertainment: Music
                PRESS 5 for Entertainment: Musicals & Theaters
                PRESS 6 for Entertainment: Television
                PRESS 7 for Entertainment: Video Games
                PRESS 8 for Entertainment: Board Games
                PRESS 9 for Science & Nature
                PRESS 10 for Science: Computers
                PRESS 11 for Science: Mathematics
                Choose Category: 10
                Enter number of questions you want: 1
```

```
                ________        .__         ___________                  .__        
                \_____  \  __ __|__|_______ \__    ___/___________ ___  _|__|____   
                 /  / \  \|  |  \  \___   /   |    |  \_  __ \__   \  \/ /  \__  \  
                /   \_/.  \  |  /  |/    /    |    |   |  | \// __  \   /|  |/ __ \_
                \_____\ \_/____/|__/_____ \   |____|   |__|  (____  /\_/ |__(____  /
                       \__>              \/                       \/             \/ 

                TOPIC: Science: Computers
                Q. In computing, what does MIDI stand for?
                A) Musical Instrument Digital Interface     B) Musical Interface of Digital Instruments     D) Musical Instrument Data Interface     G) Modular Interface of Digital Instruments     
                Enter answer: Musical Instrument Digital Interface
```
```
                ________        .__         ___________                  .__        
                \_____  \  __ __|__|_______ \__    ___/___________ ___  _|__|____   
                 /  / \  \|  |  \  \___   /   |    |  \_  __ \__   \  \/ /  \__  \  
                /   \_/.  \  |  /  |/    /    |    |   |  | \// __  \   /|  |/ __ \_
                \_____\ \_/____/|__/_____ \   |____|   |__|  (____  /\_/ |__(____  /
                       \__>              \/                       \/             \/ 

                TOPIC: Science: Computers
                CORRECT: 1
                INCORRECT: 0
                FINAL SCORE: 1 out of 1

                ------------- X -------------
                        Correct Answers
                ------------- X -------------
                Q1. Musical Instrument Digital Interface
                Do you want to continue? [y/N]:
```

# 🚀 Features

## ✔️ Interactive Terminal Quiz

<ul>
  <li>Simple, menu-based interface</li>
  <li>Supports replaying multiple quiz rounds</li>
</ul>

## ✔️ Multiple Categories

Choose from trivia categories such as:

<ul>
  <li>General Knowledge</li>
  <li>Books</li>
  <li>Films</li>
  <li>Music</li>
  <li>Video Games</li>
  <li>Board Games</li>
  <li>Science & Nature</li>
  <li>Computers</li>
  <li>Mathematics</li>
</ul>

…and more.

## ✔️ MCQ Object-Oriented Design

Question — abstract base class

MCQs — concrete implementation for multiple-choice questions

Supports answer validation, display logic, and shuffling options

## ✔️ Live API Integration

Uses the Open Trivia Database API:
https://opentdb.com/api.php

Fetches dynamic questions

Handles missing server responses via custom exception

Automatic decoding of HTML entities (", ', etc.)

## ✔️ Clean Output & Enhanced UX

Colorized console UI using colorama

Custom ASCII title banner

Clear score summary with breakdown of correct and incorrect answers

## 🧩 Project File Structure

```
├── main.py                # Main application logic
├── MCQs class             # Question handling and MCQ system
├── Custom exception       # NoServerResponseException
└── README.md
```
## 📦 Dependencies

Your project requires the following Python packages:
```
pip install requests colorama
```

It also uses standard libraries:
<ul>
  <li>os</li>
  <li>random</li>
  <li>typing</li>
  <li>abc</li>
</ul>

## 🛠️ How It Works
<ol>
  <li>The user selects a topic and number of questions.</li>
  <li>The program makes an API request to retrieve quiz data.</li>
  <li>Each question is displayed with shuffled MCQ options.</li>
  <li>User answers are validated in real-time.</li>
  <li>Final score and correct answers are shown at the end.</li>
</ol>

## ▶️ Running the Application

Simply execute:
```
python main.py
```
Requirements:
```
1) Python 3.8+
2) Internet connection (for API requests)
```
## 🌐 API Used

This project uses the Open Trivia Database (free and public API):
https://opentdb.com/

## 🧠 Key Classes
Question (abstract)

Defines the interface for:

<ul>
  <li>Displaying a question</li>
  <li>Checking an answer</li>
</ul>

MCQs (concrete class)

Handles:
<ul>
    <li>MCQ display</li>
    <li>Option randomization</li>
    <li>Answer checking</li>
    <li>HTML entity decoding</li>
</ul>

## 🧩 Custom Exceptions
NoServerResponseException

Raised when:
<ul>
    <li>API returns invalid status code</li>
    <li>No response is received</li>
    <li>Helps in reliable error handling</li>
</ul>

## 💡 Future Enhancements (Suggestions)

<ol>
  <li>Add difficulty level selection</li>
  <li>Add timer mode</li>
  <li>Save scores locally</li>
  <li>Add GUI version (Tkinter / PyQt)</li>
  <li>Export quiz results as file</li>
</ol>

## 🤝 Contributing

Pull requests and suggestions are welcome! <br>
Feel free to open an issue for bugs, improvements, or new features.

## 📄 License

This project is distributed under the MIT License. <br>
You are free to use, modify, and distribute it.
