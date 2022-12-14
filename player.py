# import pygame
# from settings import *
# from support import import_folder

# class Player(pygame.sprite.Sprite):
#     def __init__(self, pos, groups, obstacle_sprites):
#         super().__init__(groups)
#         self.image = pygame.image.load('images/character.png').convert_alpha()
#         self.rect = self.image.get_rect(topleft = pos)
        
#         self.import_player_assets()
#         self.status = 'down'
#         self.frame_index = 0
#         self.animation_speed = 0.15

#         self.direction = pygame.math.Vector2(0,0)
#         self.speed = 5

#         self.obstacle_sprites = obstacle_sprites

#     def import_player_assets(self):
#         character_path = 'images/character/'
#         self.animations = {'up': [],'down': [],'left': [],'right': [],
# 			'right_idle':[],'left_idle':[],'up_idle':[],'down_idle':[]}

#         for animation in self.animations.keys():
#             full_path = character_path + animation
#             self.animations[animation] = import_folder(full_path)

#     def input(self):
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_UP]:
#             self.direction.y = -1
#             self.status = 'up'
#         elif keys[pygame.K_DOWN]:
#             self.direction.y = 1
#             self.status = 'down'
#         else:
#             self.direction.y = 0
            
#         if keys[pygame.K_LEFT]:
#             self.direction.x = -1
#             self.status = 'left'
#         elif keys[pygame.K_RIGHT]:
#             self.direction.x = 1
#             self.status = 'right'
#         else:
#             self.direction.x = 0
#     def get_status(self):
#         if self.direction.x == 0 and self.direction.y == 0:
#             if not 'idle' in self.status:
#                 self.status = self.status + '_idle'
#     def move(self, speed):
#         if self.direction.magnitude() != 0:
#             self.direction = self.direction.normalize()
#         self.rect.x += self.direction.x * speed
#         self.collision('horizontal')
#         self.rect.y += self.direction.y * speed
#         self.collision('vertical')

#     def collision(self,direction):
#         if direction == 'horizontal':
#             for sprite in self.obstacle_sprites:
#                 if sprite.rect.colliderect(self.rect):
#                     if self.direction.x > 0:
#                         self.rect.right = sprite.rect.left
#                     if self.direction.x < 0:
#                         self.rect.left = sprite.rect.right
#         if direction == 'vertical':
#             for sprite in self.obstacle_sprites:
#                 if sprite.rect.colliderect(self.rect):
#                     if self.direction.y > 0:
#                         self.rect.bottom = sprite.rect.top
#                     if self.direction.y < 0:
#                         self.rect.top = sprite.rect.bottom
#     def animate(self):
#         animation = self.animations[self.status]
#         self.frame_index += self.animation_speed
#         if self.frame_index > len(animation):
#             self.frame_index = 0

#         self.image = animation[int(self.frame_index)]
#     def update(self):
#         self.input()
#         self.get_status()
#         self.animate()
#         self.move(self.speed)