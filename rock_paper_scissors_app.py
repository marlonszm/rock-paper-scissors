import pygame
import random

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rock, Paper, Scissors")

white = (255, 255, 255)
black = (0, 0, 0)

rock_img = pygame.image.load('rock.png')
paper_img = pygame.image.load('paper.png')
scissors_img = pygame.image.load('scissors.png')

rock_img = pygame.transform.scale(rock_img, (200, 200))
paper_img = pygame.transform.scale(paper_img, (200, 200))
scissors_img = pygame.transform.scale(scissors_img, (200, 200))

font = pygame.font.Font(None, 36)

choices_list = ["rock", "paper", "scissors"]

def draw_images():
    screen.blit(rock_img, (50, 200))
    screen.blit(paper_img, (300, 200))
    screen.blit(scissors_img, (550, 200))

def display_result(text):
    result_text = font.render(text, True, black)
    screen.blit(result_text, (width // 2 - result_text.get_width() // 2, 50))

def check_result(user_choice, cpu_choice):
    if user_choice == cpu_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and cpu_choice == "scissors") or \
         (user_choice == "paper" and cpu_choice == "rock") or \
         (user_choice == "scissors" and cpu_choice == "paper"):
        return "You have won!"
    else:
        return "You have lost!"

running = True
user_choice = None
cpu_choice = None
result = None

while running:
    screen.fill(white)
    draw_images()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            
            if 50 < x < 250 and 200 < y < 400:
                user_choice = "rock"
            elif 300 < x < 500 and 200 < y < 400:
                user_choice = "paper"
            elif 550 < x < 750 and 200 < y < 400:
                user_choice = "scissors"
            
            if user_choice:
                cpu_choice = random.choice(choices_list)
                result = check_result(user_choice, cpu_choice)

    if user_choice:
        user_text = font.render(f"Your choice: {user_choice}", True, black)
        screen.blit(user_text, (50, 50))
    
    if cpu_choice:
        cpu_text = font.render(f"CPU choice: {cpu_choice}", True, black)
        screen.blit(cpu_text, (width - cpu_text.get_width() - 50, 50))
    
    if result:
        display_result(result)

    pygame.display.flip()

pygame.quit()
