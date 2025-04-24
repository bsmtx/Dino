import pygame
import random
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
        self.sprite_id = random.randrange(1, 4)
        self.game = game
        self.rect = Rect(self.game.get_width(), self.game.get_height() - 100, 50, 50)
    def update(self):
        self.rect.x -= self.game.game_speed
        if self.rect.x + self.rect.width < 0:
            self.game.remove_cactus(self)
        if self.game.dino.dino_rect.colliderect(self.rect):
            self.game.restart()
    def get_pos(self):
        return self.rect.topleft
    def get_sprite_id(self):
        return self.sprite_id
        
            
    




class Dirijabl:
    def __init__(self, game):
        self.game = game
        self.rect = Rect(self.game.get_width(), self.game.get_height() - 200, 120, 60)
    def update(self):
        self.rect.x -= self.game.game_speed
        if self.rect.x + self.rect.width < 0:
            self.game.remove_dirijabl(self)
        if self.game.dino.dino_rect.colliderect(self.rect):
            self.game.restart()
    def get_pos(self):
        return self.rect.topleft



class Game:
    def __init__(self, ui):
        self.ui = ui
        pygame.mixer.music.load("Chime, Teminite - Duckstep [NCS Release].mp3")
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play(-1, 0.0)
        self.width, self.height = 800, 400
        with open("best_score.txt", 'r', encoding = "UTF-8") as file:
            self.best_score = int(file.read())
        self.objects = [Cactus(self)]
        self.dino = Dino(self)
        self.gravity = 1    
        self.game_speed = 12
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
        self.objects.remove(cactus)
        self.score += 1
    def update_cactus(self):
        v = self.objects[-1].get_pos()
        if v[0] < 400:
            self.add_object()
        for cactus in self.objects:
            cactus.update()

    def restart(self):
        self.best_score = max(self.best_score, self.score)
        with open("best_score.txt", 'w', encoding = "UTF-8") as file:
            file.write(str(self.best_score))
        self.ui.scene = 'dead_screen'
        pygame.mixer.music.stop()
    def get_objects(self):
        return self.objects
    def get_dino(self):
        return self.dino

    def update(self):
        self.update_cactus()
        self.update_dino()
    def get_score(self):
        return self.score
    def remove_dirijabl(self, dirijabl):
        self.objects.remove(dirijabl)
        self.score += 1
    def add_object(self):
        x = random.choice([Cactus(self), Dirijabl(self)])
        self.objects.append(x)
    
