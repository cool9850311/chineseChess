import pygame


# 定義棋子類別
class PieceSprite(pygame.sprite.Sprite):

    def __init__(self, image, position):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.unselected_image = self.image.copy()
        self.selected_image = self.image.copy()
        self.selected_image.fill((255, 255, 255, 192),
                                 special_flags=pygame.BLEND_RGBA_MULT)
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

    def select(self):
        self.image = self.selected_image

    def unselect(self):
        self.image = self.unselected_image

    def move(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_position(self):
        return (self.rect.x, self.rect.y)
