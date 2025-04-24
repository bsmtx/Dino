import pygame
import random

pygame.init()

with open("best_score.txt", 'r', encoding = "UTF-8") as file:
    best_score = int(file.read())

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Дино!")

pygame.mixer.music.load("Chime, Teminite - Duckstep [NCS Release].mp3")
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1, 0.0)

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

dino_img = pygame.image.load("dino.png")
dino_img = pygame.transform.scale(dino_img, (50, 50))

cactus_img = pygame.image.load("cactus_1.png")
cactus_img = pygame.transform.scale(cactus_img, (50, 50))

clock = pygame.time.Clock()
FPS = 60 

dino_rect = pygame.Rect(50, height - 100, 50, 50)
dino_y_velocity = 0
gravity = 1
is_jumping = False

cactus_list = []
cactus_timer = 0
cactus_spawn_time = 1500

game_speed = 10

score = 0
font = pygame.font.SysFont("Arial", 24)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                dino_y_velocity = -15
                is_jumping = True

    dino_rect.y += dino_y_velocity
    dino_y_velocity += gravity
    if dino_rect.y >= height - 100:
        dino_rect.y = height - 100
        is_jumping = False

    cactus_timer += clock.get_time()
    if cactus_timer > cactus_spawn_time:
        cactus_timer = 0
        new_cactus = pygame.Rect(width, height - 100, 50, 50)      
        cactus_list.append(new_cactus)

    for cactus in cactus_list[:]:
        cactus.x -= game_speed
        if cactus.x + cactus.width < 0:
            cactus_list.remove(cactus)
            score += 1
    for cactus in cactus_list:
        if dino_rect.colliderect(cactus):
  #          running = False
            best_score = max(best_score, score)
            with open("best_score.txt", 'w', encoding = "UTF-8") as file:
                file.write(str(best_score))
            score = 0
            cactus_list = []
            cactus_timer = 0
            dino_y_velocity = 0
            is_jumping = False
            pygame.mixer.music.play(-1, 0.0)

    screen.fill(white)
    pygame.draw.line(screen, gray, (0, height - 50), (width, height - 50))
    screen.blit(dino_img, dino_rect.topleft)
    for cactus in cactus_list:
        screen.blit(cactus_img, cactus.topleft)

    score_text = font.render(f"Score: {score}", True, black)
    screen.blit(score_text, (10,10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()