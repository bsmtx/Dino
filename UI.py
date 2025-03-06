from game import Game, Dino, Cactus
import pygame
class UI:
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.screen = pygame.display.set_mode((800, 400))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Дино!')
        
        self.clock = pygame.time.Clock()
        self.dino_sprite = pygame.image.load('dino.png')
        self.dino_sprite.set_colorkey((255,255,255))
        self.cactus_sprite = pygame.image.load('cactus.png')
        self.cactus_sprite.set_colorkey((255,255,255))
        self.dino_sprite = pygame.transform.scale(self.dino_sprite, (50, 50))
        self.cactus_sprite= pygame.transform.scale(self.cactus_sprite, (50, 50))

    def draw(self):
        name_to_sprite = {"dino": self.dino_sprite, "cactus": self.cactus_sprite}
        print(self.game.dino.get_pos())
        self.screen.blit(self.dino_sprite, self.game.get_dino().get_pos())
        for cactus in self.game.get_cactus():
            self.screen.blit(name_to_sprite['cactus'], cactus.get_pos())
                
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # if event.type == pygame.MOUSEBUTTONUP:
        
            #     x, y = pygame.mouse.get_pos()
            #     x, y = x//self.cell_size[0], y//self.cell_size[0]
            #     print("Вы ввели", x, y, "здесь находится фигура", self.game.get_piece(x, y))
            #     self.game.input(x,y)

    def run(self):
        while True:
            self.input()
            self.draw()
            self.game.update()
            pygame.display.update()
ui = UI()
ui.run()

