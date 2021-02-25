# -*- coding: utf-8 -*-
# @Time    : 2021-01-23 21:49
# @Author  : XU
# @File    : alien_invasion.py
# @Software: PyCharm
import sys

import pygame
from pygame.sprite import Group
from game.settings import Settings
from game.ship import Ship
from game.alien import Alien
from game.game_stats import GameStats
from game.score_board import Scoreboard
from game.button import Button
import game.game_functions as gf


def run_game():

    # 初始化游戏，创建屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption(ai_setting.game_title)

    play_button = Button(ai_setting, screen, "Play")
    stats = GameStats(ai_setting)
    sb = Scoreboard(ai_setting, screen, stats)

    ship = Ship(ai_setting, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_setting, screen, ship, aliens)

    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_event(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 更新飞船状态
            ship.update()
            # 更新子弹组状态
            gf.update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets)
            # 创建外星人
            # gf.create_fleet(ai_setting, screen, ship, aliens)

        # 每次循环都重绘屏幕
        gf.update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
