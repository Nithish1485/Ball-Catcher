import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 600
win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Catch the Ball")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the paddle
paddle_width = 100
paddle_height = 20
paddle_x = (window_width - paddle_width) // 2
paddle_y = window_height - 50
paddle_speed = 5
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
paddle_color = (0, 0, 255)

# Set up the ball
ball_size = 30
ball_x = random.randint(ball_size, window_width - ball_size)
ball_y = 0
ball_speed = 5
ball_color = (255, 0, 0)

# Set up the score
score = 0
score_font = pygame.font.SysFont(None, 30)
score_color = (0, 0, 0)

# Set up the game loop
game_over = False
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.x < window_width - paddle_width:
        paddle.x += paddle_speed

    # Move the ball
    ball_y += ball_speed

    # Check for collision with paddle
    if paddle.collidepoint(ball_x, ball_y + ball_size):
        ball_x = random.randint(ball_size, window_width - ball_size)
        ball_y = 0
        score += 1
        ball_speed += 1

    # Check for collision with ground
    if ball_y > window_height:
        game_over = True

    # Clear the screen
    win.fill((255, 255, 255))

    # Draw the paddle
    pygame.draw.rect(win, paddle_color, paddle)

    # Draw the ball
    pygame.draw.circle(win, ball_color, (ball_x, ball_y), ball_size)

    # Draw the score
    score_text = score_font.render("Score: " + str(score), True, score_color)
    win.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Game over
game_over_text = score_font.render("Game Over! Final Score: " + str(score), True, score_color)
win.blit(game_over_text, ((window_width - game_over_text.get_width()) // 2, (window_height - game_over_text.get_height()) // 2))
pygame.display.update()

# Wait for a key press to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            pygame.quit()
            exit()
