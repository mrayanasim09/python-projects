# This code is made by MRayan Asim
import time
import random

x = "\nhello we welcome you to our snake game hope you will like this 😊"
print(x.upper())
time.sleep(6.5)
# Window dimensions
window_width = 800
window_height = 600

# Snake segment size
segment_size = 20

# Colors
background_color = (30, 30, 30)
snake_color = (46, 139, 87)
food_color = (255, 99, 71)
score_color = (255, 255, 255)
game_over_color = (255, 0, 0)
text_color = (255, 255, 255)

pygame.init()

# Create the game window
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Fonts
font_large = pygame.font.Font(pygame.font.get_default_font(), 64)
font_medium = pygame.font.Font(pygame.font.get_default_font(), 36)
font_small = pygame.font.Font(pygame.font.get_default_font(), 24)

# Load game sounds
eat_sound = pygame.mixer.Sound(
    "C:/Users/Muhammad Asim Hanif/Downloads/snake-hissing-6092.wav"
)

# Snake's head position and initial movement direction
snake_head_x = window_width / 2
snake_head_y = window_height / 2
snake_head_dx = 0
snake_head_dy = 0

# Store the snake's body segments
snake_segments = []

# Initial length of the snake
snake_length = 1

# Spawn the first food
food_x = round(random.randrange(0, window_width - segment_size) / 20.0) * 20.0
food_y = round(random.randrange(0, window_height - segment_size) / 20.0) * 20.0

# Game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_head_dx != segment_size:
                snake_head_dx = -segment_size
                snake_head_dy = 0
            elif event.key == pygame.K_RIGHT and snake_head_dx != -segment_size:
                snake_head_dx = segment_size
                snake_head_dy = 0
            elif event.key == pygame.K_UP and snake_head_dy != segment_size:
                snake_head_dy = -segment_size
                snake_head_dx = 0
            elif event.key == pygame.K_DOWN and snake_head_dy != -segment_size:
                snake_head_dy = segment_size
                snake_head_dx = 0

    # Update the snake's head position
    snake_head_x += snake_head_dx
    snake_head_y += snake_head_dy

    # Check for collision with the food
    if snake_head_x == food_x and snake_head_y == food_y:
        # Increase the snake's length
        snake_length += 1
        # Play eat sound effect
        eat_sound.play()
        # Spawn new food
        food_x = round(random.randrange(0, window_width - segment_size) / 20.0) * 20.0
        food_y = round(random.randrange(0, window_height - segment_size) / 20.0) * 20.0

    # Create new segment and add to snake's body
    snake_segments.append((snake_head_x, snake_head_y))

    # Remove extra segments if the snake is longer than its length
    if len(snake_segments) > snake_length:
        del snake_segments[0]

    # Check for snake's collision with itself
    if (snake_head_x, snake_head_y) in snake_segments[:-1]:
        game_over = True

    # Check for snake's collision with the walls
    if (
        snake_head_x < 0
        or snake_head_x >= window_width
        or snake_head_y < 0
        or snake_head_y >= window_height
    ):
        game_over = True

    # Clear the game window
    window.fill(background_color)

    # Draw the snake's body
    for segment in snake_segments:
        pygame.draw.rect(
            window, snake_color, (segment[0], segment[1], segment_size, segment_size)
        )

    # Draw the food
    pygame.draw.rect(window, food_color, (food_x, food_y, segment_size, segment_size))

    # Draw score
    score_text = font_small.render(f"Score: {snake_length - 1}", True, score_color)
    window.blit(score_text, (20, 20))

    # Update the game display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(10)

# Game over message
game_over_text = font_large.render("Game Over", True, game_over_color)
game_over_rect = game_over_text.get_rect(
    center=(window_width / 2, window_height / 2 - 50)
)
window.blit(game_over_text, game_over_rect)

# Final score
final_score_text = font_medium.render(
    f"Final Score: {snake_length - 1}", True, text_color
)
final_score_rect = final_score_text.get_rect(
    center=(window_width / 2, window_height / 2 + 10)
)
window.blit(final_score_text, final_score_rect)

# Instructions to restart
restart_text = font_small.render("Press SPACEBAR to play again", True, text_color)
restart_rect = restart_text.get_rect(center=(window_width / 2, window_height / 2 + 70))
window.blit(restart_text, restart_rect)

# Update the game display
pygame.display.update()


# Wait for SPACEBAR to restart or close the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Reset snake variables
                snake_head_x = window_width / 2
                snake_head_y = window_height / 2
                snake_head_dx = 0
                snake_head_dy = 0
                snake_segments.clear()
                snake_length = 1
                # Spawn new food
                food_x = (
                    round(random.randrange(0, window_width - segment_size) / 20.0)
                    * 20.0
                )
                food_y = (
                    round(random.randrange(0, window_height - segment_size) / 20.0)
                    * 20.0
                )
                game_over = False
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    if not game_over:
        break

    clock.tick(10)

# Close the game window
pygame.quit()
