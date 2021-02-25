# -*- coding: utf-8 -*-
# @Time    : 2021-01-23 23:08
# @Author  : XU
# @File    : game_functions.py
# @Software: PyCharm
import sys
from time import sleep
import pygame
from game.bullet import Bullet
from game.alien import Alien


def check_down_event(event, ai_setting, screen, stats, sb, ship, aliens, bullets):
    """识别下按按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        play_game(ai_setting, screen, stats, sb, ship, aliens, bullets)


def check_up_event(event, ship):
    """识别上抬按键事件"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_event(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets):
    """检查按键事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_down_event(event, ai_setting, screen, stats, sb, ship, aliens, bullets)
        elif event.type == pygame.KEYUP:
            check_up_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def play_game(ai_setting, screen, stats, sb, ship, aliens, bullets):
    # 隐藏光标
    pygame.mouse.set_visible(False)
    stats.reset_stats()
    stats.game_active = True

    # 重置记分牌图像
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()

    aliens.empty()
    bullets.empty()

    create_fleet(ai_setting, screen, ship, aliens)
    ship.center_ship()


def check_play_button(ai_setting, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        # 重置游戏设置
        ai_setting.initialize_dynamic_setting()
        play_game(ai_setting, screen, stats, sb, ship, aliens, bullets)


def update_screen(ai_setting, screen, stats, sb, ship, aliens, bullets, play_button):
    """刷新主屏幕"""
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_botton()
    pygame.display.flip()


def update_bullets(ai_setting, screen, stats, sb, ship, aliens, bullets):
    """更新子弹位置，删除屏幕外子弹"""
    # 更新子弹组内各子弹位置，调用组的update方法，将自动调用组内精灵的update方法
    bullets.update()
    # 删除屏幕外的子弹（降低资源消耗）
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_setting, screen, stats, sb, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_setting, screen, stats, sb, ship, aliens, bullets):
    """
    检测是否有子弹集中外星人
    如果集中，则删除对应子弹和被击中外星人
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()

        # 提高等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_setting, screen, ship, aliens)


def fire_bullet(ai_setting, screen, ship, bullets):
    """发射子弹"""
    if len(bullets) <= ai_setting.bullet_allow:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)


def get_number_rows(ai_setting, alien_height, ship_height):
    available_space_y = ai_setting.screen_height - alien_height * 3 - ship_height
    number_rows = int(available_space_y / (alien_height * 2))
    return number_rows


def get_number_alien_x(ai_setting, alien_width):
    available_space_x = ai_setting.screen_width - alien_width * 2
    number_alien_x = int(available_space_x / (alien_width * 2))
    return number_alien_x


def create_alien(ai_setting, screen, aliens, alien_number, row_number):
    alien = Alien(ai_setting, screen)
    alien.rect.x = alien.rect.width + 2 * alien.rect.width * alien_number     # 乘以1.7是为了这行外星人居中
    alien.rect.y = alien.rect.height + 2 * alien.rect.height + row_number
    aliens.add(alien)


def create_fleet(ai_setting, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_setting, screen)
    # 计算一行可容纳的外星人数
    alien_width = alien.rect.width
    number_alien_x = get_number_alien_x(ai_setting, alien_width)
    number_rows = get_number_rows(ai_setting, alien.rect.height, ship.rect.height)
    # 创建一行外星人
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_setting, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_setting, aliens):
    """检测外星人是否到达屏幕边缘，并采取相应措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            check_fleet_direction(ai_setting, aliens)


def check_fleet_direction(ai_setting, aliens):
    """将整行外星人下移，并改变运动方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1


def ship_hit(ai_setting, stats, sb, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ship_left > 0:
        # ship_left 减1
        stats.ship_left -= 1

        # 更新记分牌
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船在底部重置
        create_fleet(ai_setting, screen, ship, aliens)
        ship.center_ship()

        # 暂停0.5秒
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_setting, stats, sb, screen, ship, aliens, bullets):
    # 检查外星人是否到达屏幕边缘，并更新外星人位置
    check_fleet_edges(ai_setting, aliens)
    aliens.update()

    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_setting, stats, sb, screen, ship, aliens, bullets)
        print("Ship hit!!!")

        check_alien_bottom(ai_setting, stats, sb, screen, ship, aliens, bullets)


def check_alien_bottom(ai_setting, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting, stats, sb, screen, ship, aliens, bullets)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
