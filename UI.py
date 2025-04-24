from game import Game, Dino, Cactus, Dirijabl
import pygame
class UI:
    def __init__(self):
        pygame.init()
        self.game = Game(self)
        self.screen = pygame.display.set_mode((800, 400))
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Дино!')
        
        self.clock = pygame.time.Clock()
        self.screen_dead_sprite = pygame.image.load('screen dead.png')
        self.scene = 'game'
        self.dirijabl_sprite = pygame.image.load('dirijabl.png')
        self.dino_sprite = pygame.image.load('dino.png')
        self.dino_sprite.set_colorkey((255,255,255))
        self.cactus_sprite = pygame.image.load('cactus_1.png')
        self.night_sprite = pygame.image.load('night.png')
        self.cactus_sprite_2 = pygame.image.load("cactus_2.png")
        self.cactus_sprite_3 = pygame.image.load("cactus_3.png")
        self.start_button_rect = pygame.Rect([266, 162],[235, 70])
        self.quit_button_rect = pygame.Rect([266, 264], [235, 70])
        self.cactus_sprite.set_colorkey((255,255,255))
        self.dirijabl_sprite.set_colorkey((255,255,255))
        self.cactus_sprite_2.set_colorkey((255,255,255))
        self.cactus_sprite_3.set_colorkey((255,255,255))
        self.dino_sprite = pygame.transform.scale(self.dino_sprite, (50, 50))
        self.cactus_sprite= pygame.transform.scale(self.cactus_sprite, (50, 50))

    def draw_game(self):
        if self.game.get_score() > 20:
            self.screen.blit(self.night_sprite, (0, 0))
        else:
            self.screen.fill((255, 255, 255))
        name_to_sprite = {"dino": self.dino_sprite, "cactus_1": self.cactus_sprite, "cactus_2": self.cactus_sprite_2, "cactus_3": self.cactus_sprite_3, "dirijabl": self.dirijabl_sprite }
        self.screen.blit(self.dino_sprite, self.game.get_dino().get_pos())
        for obj in self.game.get_objects():
            if type(obj) == Cactus:
                a = obj.get_sprite_id()
                if a == 1:
                    self.screen.blit(name_to_sprite['cactus_1'], obj.get_pos())
                elif a == 2:
                    self.screen.blit(name_to_sprite['cactus_2'], obj.get_pos())
                elif a == 3:
                    self.screen.blit(name_to_sprite['cactus_3'], obj.get_pos())
            elif type(obj) == Dirijabl:
                self.screen.blit(name_to_sprite['dirijabl'], obj.get_pos())
    def draw(self):
        if self.scene == 'dead_screen':
            self.draw_dead_screen()
        elif self.scene == 'game':
            self.draw_game()
    def draw_dead_screen(self):
        self.screen.blit(self.screen_dead_sprite, [0, 0])

        



    

                
    def input_game(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.game.jump()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.jump()
    def input_dead_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.start_button_rect.collidepoint(event.pos):
                    self.scene = 'game'
                    self.game = Game(self)
                if self.quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    quit()
    def input(self):
        if self.scene == 'dead_screen':
            self.input_dead_screen()
        elif self.scene == 'game':
            self.input_game()




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
            pygame.display.flip()
            self.clock.tick(60)

ui = UI()
ui.run()

