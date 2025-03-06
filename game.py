import pygame
from pygame import Rect


class Dino:
    def __init__(self, game):
        self.game = game
        self.dino_rect = Rect(50, self.game.get_height() - 100, 50, 50)
        self.dino_y_velocity = 0
        self.is_jumping = False
    def jump(self):
        if self.is_jumping == False:
            self.dino_y_velocity = -15
            self.is_jumping = True
            
    def update(self):
        self.dino_rect.y += self.dino_y_velocity
        self.dino_y_velocity += self.game.get_gravity()
        if self.dino_rect.y >= self.game.get_height() - 100:
            self.dino_rect.y = self.game.get_height() - 100
            self.is_jumping = False
    def get_pos(self):
        return self.dino_rect.topleft
    





class Cactus:
    def __init__(self, game):
        self.game = game
        self.cactus_timer = 0
        self.rect = Rect(self.game.get_width(), self.game.get_height() - 100, 50, 50)
    def update(self):
        self.rect.x -= self.game.game_speed
        if self.rect.x + self.rect.width < 0:
            self.game.remove_cactus(self)
        if self.game.dino.dino_rect.colliderect(self.rect):
            self.game.restart()
    def get_pos(self):
        return self.rect.topleft
            
    




class Game:
    def __init__(self):
        pygame.mixer.music.load("Chime, Teminite - Duckstep [NCS Release].mp3")
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play(-1, 0.0)
        self.width, self.height = 800, 400
        with open("best_score.txt", 'r', encoding = "UTF-8") as file:
            self.best_score = int(file.read())
        self.cactus = [Cactus(self)]
        self.dino = Dino(self)
        self.gravity = 1    
        self.game_speed = 10
        self.score = 0
    def get_height(self):
        return self.height
    def get_width(self):
        return self.width
    def get_gravity(self):
        return self.gravity
    def jump(self):
        self.dino.jump()

    def update_dino(self):
        self.dino.update()
    def remove_cactus(self, cactus):
        self.cactus.remove(cactus)
        self.score += 1
        self.cactus.append(Cactus(self))
    def update_cactus(self):
        for cactus in self.cactus:
            cactus.update()

    def restart(self):
        self.best_score = max(self.best_score, self.score)
        with open("best_score.txt", 'w', encoding = "UTF-8") as file:
            file.write(str(self.best_score))
        self.cactus = [Cactus(self)]
        self.dino = Dino(self)
        self.score = 0
        pygame.mixer.music.play(-1, 0.0)
    def get_cactus(self):
        return self.cactus
    def get_dino(self):
        return self.dino

    def update(self):
        self.update_cactus()
        self.update_dino()
