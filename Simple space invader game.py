import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Invaders")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Set up the enemy
enemy_size = 50
enemy_speed = 2
enemies = []

# Set up bullets
bullet_size = 5
bullet_speed = 5
bullets = []

# Set up the clock
clock = pygame.time.Clock()

# Set up the font
font = pygame.font.Font(None, 36)

# Function to draw the player
def draw_player(x, y):
    pygame.draw.rect(screen, white, [x, y, player_size, player_size])

# Function to draw an enemy
def draw_enemy(x, y):
    pygame.draw.rect(screen, white, [x, y, enemy_size, enemy_size])

# Function to draw a bullet
def draw_bullet(x, y):
    pygame.draw.rect(screen, white, [x, y, bullet_size, bullet_size])

# Function to display the score
def show_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, [10, 10])

# Game loop
game_over = False
score = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE:
                bullets.append([player_x + player_size // 2, player_y])

    # Move the player
    player_x = max(0, min(player_x, width - player_size))

    # Move the bullets
    bullets = [[bx, by - bullet_speed] for bx, by in bullets]

    # Spawn new enemies
    if random.randint(1, 100) < 2:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = 0
        enemies.append([enemy_x, enemy_y])

    # Move the enemies
    enemies = [[ex, ey + enemy_speed] for ex, ey in enemies]

    # Check for collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if (
                enemy[0] < bullet[0] < enemy[0] + enemy_size
                and enemy[1] < bullet[1] < enemy[1] + enemy_size
            ):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1

    # Remove off-screen bullets and enemies
    bullets = [bullet for bullet in bullets if bullet[1] > 0]
    enemies = [enemy for enemy in enemies if enemy[1] < height]

    # Check for player collision with enemies
    for enemy in enemies:
        if (
            player_x < enemy[0] < player_x + player_size
            and player_y < enemy[1] < player_y + player_size
        ):
            game_over = True

    # Clear the screen
    screen.fill(black)

    # Draw the player
    draw_player(player_x, player_y)

    # Draw the enemies
    for enemy in enemies:
        draw_enemy(enemy[0], enemy[1])

    # Draw the bullets
    for bullet in bullets:
        draw_bullet(bullet[0], bullet[1])

    # Display the score
    show_score(score)

    # Update the display
    pygame.display.update()

    # Set the frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()
