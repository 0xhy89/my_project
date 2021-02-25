# -*- coding: utf-8 -*-
# @Time    : 2021-01-24 22:47
# @Author  : XU
# @File    : bullet.py
# @Software: PyCharm
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_setting, screen, ship):
        super().__init__()
        self.screen = screen

        # 子弹在(0, 0)坐标创建
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width, ai_setting.bullet_height)
        # 从飞机的头部位置出现（发射）
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor

    def update(self):
        """更新子弹位置「子弹向上移动」"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)




