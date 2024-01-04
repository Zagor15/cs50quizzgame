
import pygame
from settings import *
from quiz import *


pygame.init()
n = 0


# create the screen
display_surface = pygame.display.set_mode((screenresolution))

# set the pygame window name
pygame.display.set_caption("Quiz")

# create a text object
font = pygame.font.Font("freesansbold.ttf", 32)

# create a text surface object
first_question = list(questions.keys())[n]
question1 = font.render(first_question, True, textcolor, backgroundcolor)
answers = questions[first_question]
first_answer = answers[0]
answer1 = font.render(first_answer, True, textcolor, backgroundcolor)
second_answer = answers[1]
answer2 = font.render(second_answer, True, textcolor, backgroundcolor)
third_answer = answers[2]
answer3 = font.render(third_answer, True, textcolor, backgroundcolor)
fourth_answer = answers[3]
answer4 = font.render(fourth_answer, True, textcolor, backgroundcolor)
response = font.render(
    "Enter the answer: 1, 2, 3, 4 and press enter", True, textcolor, backgroundcolor
)

# create the input box for the answer
input_box = pygame.Rect(300, 400, 200, 50)
color_inactive = pygame.Color("lightskyblue3")
color_active = pygame.Color("dodgerblue2")
color = color_inactive
active = False
input1 = ""


def display_elements():
    # display the background
    display_surface.fill(backgroundcolor)

    # display the differents elements
    display_surface.blit(question1, (40, 80))
    display_surface.blit(answer1, (40, 150))
    display_surface.blit(answer2, (400, 150))
    display_surface.blit(answer3, (40, 200))
    display_surface.blit(answer4, (400, 200))
    display_surface.blit(response, (40, 350))


# create the score screen (game over screen)
def scorescreen():
    display_surface.fill(backgroundcolor)
    textscore = font.render(
        f" Your final Score is {str(score)}", True, textcolor, backgroundcolor
    )
    textscore1 = font.render(
        f" You have {str(score)} good answers on {len(goodanswers)}",
        True,
        textcolor,
        backgroundcolor,
    )
    text_rect = textscore.get_rect(center=(X / 2, Y / 2))
    text_rect1 = textscore1.get_rect(center=(X / 2, Y / 2 + 50))
    display_surface.blit(textscore, text_rect)
    display_surface.blit(textscore1, text_rect1)
    pygame.display.flip()


while True:
    display_elements()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # create a input box
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    # actualize the score
                    if int(input1) == int(goodanswers[n]):
                        score += 1
                    n += 1

                    if n < len(questions):
                        # Update and redraw the question and the answers for the next question
                        first_question = list(questions.keys())[n]
                        question1 = font.render(
                            first_question, True, textcolor, backgroundcolor
                        )
                        answers = questions[first_question]
                        first_answer = answers[0]
                        answer1 = font.render(
                            first_answer, True, textcolor, backgroundcolor
                        )
                        second_answer = answers[1]
                        answer2 = font.render(
                            second_answer, True, textcolor, backgroundcolor
                        )
                        third_answer = answers[2]
                        answer3 = font.render(
                            third_answer, True, textcolor, backgroundcolor
                        )
                        fourth_answer = answers[3]
                        answer4 = font.render(
                            fourth_answer, True, textcolor, backgroundcolor
                        )

                elif event.key == pygame.K_BACKSPACE:
                    input1 = input1[:-1]

                else:
                    input1 += event.unicode

    txt_surface = font.render(input1, True, color)
    display_surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(display_surface, color, input_box, 2)

    # load the score screen when there is no more questions
    if n == len(questions):
        scorescreen()

    pygame.display.flip()
