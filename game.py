import pygame
from pygame import USEREVENT
from random import randint
from player_game import Player, Fire, AI

pygame.init()
screen_width = 700
screen_height = 550
done = False
is_blue = True

block_width = 25
block_height = 25
player_speed = 6

# num = int(input("how many players? (1-3)"))
# while num not in range(1, 4):
#     print('INPUT VALID NUMBER!')
#     num = int(input("how many players? (1-4)"))

# this is the number of players (1-3)
num_players = 1

# letter = int(input("choose a difficulty: (0,1,2)"))
# while letter not in range(0, 3):
#     print("INVALID INPUT!")
#     letter = input("choose a difficulty: (0, 1, 2)")

# This is the difficulty
difficulty = 2

# decides whether there is a computer ai(True) or not (False)
ai = True
computer = []
if ai is True:
    computer.append(AI(screen_width//2, screen_height//2))

player_list = []
for i in range(num_players):
    player_list.append(Player(screen_width//2, screen_height//2))

bg = pygame.image.load('space.jpg')
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


def fire_ball_settings(difficult: int)-> tuple:
    """
    initialize fire ball settings
    """
    fire_generate = 0
    speed = 0
    if difficult == 0:
        fire_generate = 1
        speed = 5
    elif difficult == 1:
        fire_generate = 2
        speed = 7
    elif difficult == 2:
        fire_generate = 4
        speed = 6
    return fire_generate, speed


fire_nums, fire_speed = fire_ball_settings(difficulty)
radius = 18


def movement(number: int)-> None:
    """
    tells keys to press depending on number of players
    """

    pressed = pygame.key.get_pressed()

    if number == 1:
        if pressed[pygame.K_UP] and player_list[0].y > player_speed:
            player_list[0].y -= player_speed
        if pressed[pygame.K_DOWN] and player_list[0].y < screen_height - block_height - player_speed:
            player_list[0].y += player_speed
        if pressed[pygame.K_LEFT] and player_list[0].x > player_speed:
            player_list[0].x -= player_speed
        if pressed[pygame.K_RIGHT] and player_list[0].x < screen_width - block_width - player_speed:
            player_list[0].x += player_speed
    elif number == 2:
        if pressed[pygame.K_UP] and player_list[0].y > player_speed:
            player_list[0].y -= player_speed
        if pressed[pygame.K_DOWN] and player_list[0].y < screen_height - block_height - player_speed:
            player_list[0].y += player_speed
        if pressed[pygame.K_LEFT] and player_list[0].x > player_speed:
            player_list[0].x -= player_speed
        if pressed[pygame.K_RIGHT] and player_list[0].x < screen_width - block_width - player_speed:
            player_list[0].x += player_speed

        if pressed[pygame.K_w] and player_list[1].y > player_speed:
            player_list[1].y -= player_speed
        if pressed[pygame.K_s] and player_list[1].y < screen_height - block_height - player_speed:
            player_list[1].y += player_speed
        if pressed[pygame.K_a] and player_list[1].x > player_speed:
            player_list[1].x -= player_speed
        if pressed[pygame.K_d] and player_list[1].x < screen_width - block_width - player_speed:
            player_list[1].x += player_speed
    elif number == 3:
        if pressed[pygame.K_UP] and player_list[0].y > player_speed:
            player_list[0].y -= player_speed
        if pressed[pygame.K_DOWN] and player_list[0].y < screen_height - block_height - player_speed:
            player_list[0].y += player_speed
        if pressed[pygame.K_LEFT] and player_list[0].x > player_speed:
            player_list[0].x -= player_speed
        if pressed[pygame.K_RIGHT] and player_list[0].x < screen_width - block_width - player_speed:
            player_list[0].x += player_speed

        if pressed[pygame.K_w] and player_list[1].y > player_speed:
            player_list[1].y -= player_speed
        if pressed[pygame.K_s] and player_list[1].y < screen_height - block_height - player_speed:
            player_list[1].y += player_speed
        if pressed[pygame.K_a] and player_list[1].x > player_speed:
            player_list[1].x -= player_speed
        if pressed[pygame.K_d] and player_list[1].x < screen_width - block_width - player_speed:
            player_list[1].x += player_speed

        if pressed[pygame.K_i] and player_list[2].y > player_speed:
            player_list[2].y -= player_speed
        if pressed[pygame.K_k] and player_list[2].y < screen_height - block_height - player_speed:
            player_list[2].y += player_speed
        if pressed[pygame.K_j] and player_list[2].x > player_speed:
            player_list[2].x -= player_speed
        if pressed[pygame.K_l] and player_list[2].x < screen_width - block_width - player_speed:
            player_list[2].x += player_speed


ball_list = []


def ball_movement()-> None:
    """
    tells the balls to move
    """
    for i in range(fire_nums):
        a = randint(0, 4)
        if a == 0:
            ball_list.append(Fire(randint(0, screen_width),0 - radius , a))
        elif a == 1:
            ball_list.append(Fire(0 - radius, randint(0, screen_height), a))
        elif a == 2:
            ball_list.append(Fire(randint(0, screen_width), screen_height + radius, a))
        elif a == 3:
            ball_list.append(Fire(screen_width + radius, randint(0, screen_height), a))
        elif a == 4:
            ball_list.append(Fire(screen_width + radius, randint(0, screen_height), a))


pygame.time.set_timer(USEREVENT + 1, 1000)
while not done:
    screen.blit(bg, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                done = True
        if event.type == USEREVENT + 1:
            ball_movement()

    new = []
    for ball in ball_list:
        b = pygame.draw.rect(screen, (250, 0, 0), pygame.Rect(ball.x, ball.y,
                                                              radius, radius))
        new.append(b)

    if ai is True:
        comp = pygame.draw.rect(screen, computer[0].colour, pygame.Rect(
            computer[0].x, computer[0].y, block_width, block_height))
        for fire in new:
            if abs(fire.x - comp.x) in range(fire_speed*3) and fire.y in range(comp.y - block_height, comp.y + block_height*2):
                if fire.x > comp.x:
                    if computer[0].x > fire_speed:
                        computer[0].x -= fire_speed
                elif fire.x < comp.x:
                    if computer[0].x < screen_width - block_width - fire_speed:
                        computer[0].x += fire_speed
            if abs(fire.y - comp.y) in range(fire_speed*3) and fire.x in range(comp.x - block_width, comp.x + block_width * 2):
                if fire.y > comp.y:
                    if computer[0].y > fire_speed:
                        computer[0].y -= fire_speed
                elif fire.x < comp.x:
                    if computer[0].y < screen_height - block_height - fire_speed:
                        computer[0].y += fire_speed
            if comp.colliderect(fire):
                done = True

    for player in player_list:
        a = pygame.draw.rect(screen, player.colour, pygame.Rect(player.x,
                                                                player.y,
                                                                block_width,
                                                                block_height))
        for fire_ball in new:
            if a.colliderect(fire_ball):
                if player in player_list:
                    player_list.remove(player)

    for ball in ball_list:
        if ball.speed == 0:
            ball.y += fire_speed
        elif ball.speed == 1:
            ball.x += fire_speed
        elif ball.speed == 2:
            ball.y -= fire_speed
        elif ball.speed == 3:
            ball.x -= fire_speed
        elif ball.speed == 4:
            ball.x -= fire_speed
            ball.y += fire_speed

    if num_players == 1:
        if len(player_list) == 0:
            done = True
            print(f"you lasted {pygame.time.get_ticks()/1000}s")
            break
    else:
        if len(player_list) <= 1:
            done = True
            print(f"Last player standing won!")
            print(f"He lasted{pygame.time.get_ticks()/1000}s")
            break

    movement(num_players)

    pygame.display.update()
    clock.tick(60)
