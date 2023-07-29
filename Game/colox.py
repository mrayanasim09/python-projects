# This code is made by MRayan Asim
# Packages needed:
# pip install pygame
import pygame
import random

# initialize the constructor
pygame.init()
res = (800, 600)  # Decreased screen size to 800x600

# randomly assigns a value to variables
# ranging from lower limit to upper
c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
color_list = [red, green, blue]
colox_c1 = 0
colox_c2 = 0
colox_c3 = 254
colox_c4 = 254

# randomly assigns a colour from color_list
# to player
player_c = blue

# light shade of menu buttons
startl = (169, 169, 169)

# dark shade of menu buttons
startd = (100, 100, 100)
white = (255, 255, 255)
start = (255, 255, 255)
width = screen.get_width()
height = screen.get_height()

# initial X position of player
lead_x = 40

# initial y position of player
lead_y = height // 2
x = 300  # Adjusted x position of buttons
y = 200
width1 = 200  # Decreased width of buttons to 200
height1 = 80  # Decreased height of buttons to 80
enemy_size = 50

# defining a font
smallfont = pygame.font.SysFont("Corbel", 35)

# texts to be rendered on screen
text = smallfont.render("Start", True, white)
text1 = smallfont.render("Options", True, white)
exit1 = smallfont.render("Exit", True, white)

# game title
colox = smallfont.render("Colox", True, (c3, c2, c1))
x1 = random.randint(width // 2, width)
y1 = random.randint(100, height // 2)
x2 = 40
y2 = 40
speed = 15

# score of the player
count = 0
rgb = random.choice(color_list)

# enemy position
e_p = [width, random.randint(50, height - 50)]
e1_p = [random.randint(width, width + 100), random.randint(50, height - 100)]


# function for game_over
def game_over():
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (
                    100 < mouse_pos[0] < 140
                    and height - 100 < mouse_pos[1] < height - 80
                ):
                    pygame.quit()
                if (
                    width - 180 < mouse_pos[0] < width - 100
                    and height - 100 < mouse_pos[1] < height - 80
                ):
                    game(lead_y, lead_x, speed, count)

        screen.fill((65, 25, 64))
        smallfont = pygame.font.SysFont("Corbel", 60)
        smallfont1 = pygame.font.SysFont("Corbel", 25)
        game_over_text = smallfont.render("GAME OVER", True, white)
        game_exit = smallfont1.render("Exit", True, white)
        restart = smallfont1.render("Restart", True, white)
        mouse_pos = pygame.mouse.get_pos()

        if 100 < mouse_pos[0] < 140 and height - 100 < mouse_pos[1] < height - 80:
            pygame.draw.rect(screen, startl, [100, height - 100, 40, 20])
        else:
            pygame.draw.rect(screen, startd, [100, height - 100, 40, 20])

        if (
            width - 180 < mouse_pos[0] < width - 100
            and height - 100 < mouse_pos[1] < height - 80
        ):
            pygame.draw.rect(screen, startl, [width - 180, height - 100, 80, 20])
        else:
            pygame.draw.rect(screen, startd, [width - 180, height - 100, 80, 20])

        screen.blit(game_exit, (100, height - 100))
        screen.blit(restart, (width - 180, height - 100))
        screen.blit(game_over_text, (width // 2 - 150, 295))
        pygame.display.update()


pygame.draw.rect(screen, startd, [100, height - 100, 40, 20])
pygame.draw.rect(screen, startd, [width - 180, height - 100, 40, 50])


# function for body of the game
def game(lead_y, lead_X, speed, count):
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if lead_y > 40:  # Prevent going beyond top boundary
                lead_y -= 10
        if keys[pygame.K_DOWN]:
            if lead_y < height - 80:  # Prevent going beyond bottom boundary
                lead_y += 10
        screen.fill((65, 25, 64))
        clock.tick(speed)

        rect = pygame.draw.rect(screen, player_c, [lead_x, lead_y, 40, 40])
        pygame.draw.rect(screen, (c1, c2, c3), [0, 0, width, 40])
        pygame.draw.rect(screen, (c3, c2, c1), [0, height - 40, width, 40])
        pygame.draw.rect(screen, startd, [width - 100, 0, 100, 40])
        smallfont = pygame.font.SysFont("Corbel", 35)
        exit2 = smallfont.render("Exit", True, white)

        mouse_pos = pygame.mouse.get_pos()
        if width - 100 < mouse_pos[0] < width and 0 < mouse_pos[1] < 40:
            pygame.draw.rect(screen, startl, [width - 100, 0, 100, 40])
        else:
            pygame.draw.rect(screen, startd, [width - 100, 0, 100, 40])
        if width - 100 < mouse_pos[0] < width and 0 < mouse_pos[1] < 40:
            if ev.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()

        if e_p[0] > 0 and e_p[0] <= width:
            e_p[0] -= 10
        else:
            if (
                e_p[1] <= 40 or e_p[1] >= height - 80
            ):  # Prevent appearing on top and bottom color banners
                e_p[1] = random.randint(40, height - 80)
            if (
                e1_p[1] <= 40 or e1_p[1] >= height - 80
            ):  # Prevent appearing on top and bottom color banners
                e1_p[1] = random.randint(40, height - 80)
            e_p[1] = random.randint(enemy_size, height - enemy_size)
            e_p[0] = width

        if lead_x <= e_p[0] <= lead_x + 40 and lead_y >= e_p[1] >= lead_y - 40:
            game_over()

        if (
            lead_y <= e_p[1] + enemy_size <= lead_y + 40
            and lead_x <= e_p[0] <= lead_x + 40
        ):
            game_over()

        pygame.draw.rect(screen, red, [e_p[0], e_p[1], enemy_size, enemy_size])
        if e1_p[0] > 0 and e1_p[0] <= width + 100:
            e1_p[0] -= 10
        else:
            if (
                e1_p[1] <= 40 or e1_p[1] >= height - 80
            ):  # Prevent appearing on top and bottom color banners
                e1_p[1] = random.randint(40, height - 80)
            e1_p[1] = random.randint(enemy_size, height - 40)
            e1_p[0] = width + 100

        if lead_x <= e1_p[0] <= lead_x + 40 and e1_p[1] <= lead_y <= e1_p[1] + 40:
            e1_p[0] = width + 100
            e1_p[1] = random.randint(40, height - 40)
            count += 1
            speed += 1

        if (
            lead_y <= e1_p[1] + enemy_size <= lead_y + 40
            and lead_x <= e1_p[0] <= lead_x + 40
        ):
            e1_p[0] = width + 100
            e1_p[1] = random.randint(40, height - 40)
            count += 1
            speed += 1

            if count >= 45:
                speed = 60

        if (
            lead_y <= 40 or lead_y >= height - 80
        ):  # Prevent going beyond top and bottom boundaries
            game_over()
        if e1_p[0] <= 0:
            game_over()

        pygame.draw.rect(screen, blue, [e1_p[0], e1_p[1], enemy_size, enemy_size])
        score1 = smallfont.render("Score: " + str(count), True, white)
        screen.blit(score1, (width - 120, height - 40))
        screen.blit(exit2, (width - 80, 0))
        pygame.display.update()


# intro
def intro(colox_c1, colox_c2, colox, exit1, text1, text):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if x < mouse_pos[0] < x + width1 and y < mouse_pos[1] < y + height1:
                    game(lead_y, lead_x, speed, count)
                if (
                    x < mouse_pos[0] < x + width1 + 40
                    and y + 70 < mouse_pos[1] < y + 70 + height1
                ):
                    pygame.quit()
                if (
                    x < mouse_pos[0] < width1 + x
                    and y + 140 < mouse_pos[1] < y + 140 + height1
                ):
                    pygame.quit()

        screen.fill((65, 25, 64))
        mouse_pos = pygame.mouse.get_pos()

        if x < mouse_pos[0] < x + width1 and y < mouse_pos[1] < y + height1:
            pygame.draw.rect(screen, startl, [x, y, width1, height1])
        else:
            pygame.draw.rect(screen, startd, [x, y, width1, height1])

        if (
            x < mouse_pos[0] < x + width1 + 40
            and y + 70 < mouse_pos[1] < y + 70 + height1
        ):
            pygame.draw.rect(screen, startl, [x, y + 70, width1 + 40, height1])
        else:
            pygame.draw.rect(screen, startd, [x, y + 70, width1 + 40, height1])

        if x < mouse_pos[0] < width1 + x and y + 140 < mouse_pos[1] < y + 140 + height1:
            pygame.draw.rect(screen, startl, [x, y + 140, width1, height1])
        else:
            pygame.draw.rect(screen, startd, [x, y + 140, width1, height1])

        screen.blit(colox, (300, 50))
        screen.blit(text, (340, 220))
        screen.blit(text1, (305, 300))
        screen.blit(exit1, (355, 380))
        pygame.display.update()


intro(colox_c1, colox_c2, colox, exit1, text1, text)
