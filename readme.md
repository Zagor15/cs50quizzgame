# A SIMPLE GEOGRAPHIC QUIZ GAME
#### Video Demo:  <https://youtu.be/5N7fpCblfLM>
#### Description: 

This is my final project for CS50. I decided to make a game on pygame, the Python library used to create simple games.
I know that there are other programming languages that are more specialized in the creation of a game. But for creating a quiz game, Python with Pygame is enough.
Moreover, this game uses a dictionary which is an important asset of Python.

##### *How the game works for the user/player*

A question related to geography appears on the screen with four answers, each one having a number. The player/user must type the number of the good answer in the input box and press enter.
After all the questions are answered, the player will see the score and the number of good answers on the total of questions.


##### *How the game has been made*
The game is made with three Python files: quiz.py, main.py, and settings.py

The quiz file has all the data needed to create the quiz.
This file has the dictionary in which you find the question and the answer. It is a nested dictionary: each question (the key) has a list (the value) of four answers.
This file has also a list of the good answers: it consists of a list of numbers which are the number of the correct answers. The first value of the list corresponds to the correct answer for the first key of the dictionary. The second value for the second key of the dictionary, etc.
Finally, in this quiz file, the variable score is initialized to zero.
If the quiz needs to be modified (for example a new question), we only need to modify this file (and more precisely the dictionary and the goodanswer list). 

The main file is the one that has the code allowing the game to work. I used the font and the blit function of pygame to create a screen displaying the questions and answers of the dictionary located in the quiz file. I also created an input box allowing the user to tape the answer. Finally, a score screen must be shown at the end.
When the return keyboard key is pressed the program first checks if the input corresponds to the goodanswer list, if yes it adds one to the score. After this (and no matter if the input corresponds to the answer or not) the screen is actualized to print the next question of the dictionary and answers. 
For this, I have created a variable n initialized to zero. Each time the return key is pressed, it adds + 1 to n. If n is less than the size of the question dictionary, it will update the screen with the new question and answers and it will check if the input is equal to the answer stored in the list at the n value. So initially, n = 0 and displays the first question of the dictionary, and when the enter key is pressed the program checks the first number of the list goodanswers (which both start at 0), and after that n has its value rise to 1.
When n becomes equal to the length of the dictionary, it means that there is no further question. So the code will display the score screen and show the score.

The settings file is the file that has the screen resolution values and which stores the color of the background and font. It allows to modify quickly and safely the visual configuration.


#####  *Sources used for help*
creating text element : https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

creating a game over screen : https://www.makeuseof.com/start-menu-and-game-over-screen-with-pygame/

creating input box : https://www.geeksforgeeks.org/how-to-create-a-text-input-box-with-pygame/ and https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame

cs50.ai

Book : Python Crash Course, Eric Matthes
