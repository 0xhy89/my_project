# -*- coding: utf-8 -*-
# @Time    : 2021-01-24 23:48
# @Author  : XU
# @File    : alien.py
# @Software: PyCharm
import os
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_setting, screen):
        super().__init__()
        self.screen = screen
        self.ai_setting = ai_setting

        self.image = pygame.image.load(os.path.dirname(__file__) + '/images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitem(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """如果外星人在屏幕边缘，则返回True"""
        screen_rect = self.screen.get_rect()
        return True if self.rect.right >= screen_rect.right or self.rect.left <= 0 else False
