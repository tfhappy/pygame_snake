# -*- coding:utf-8 -*-
import sys
import time

import pygame
import random

pygame.init()  # 初始化所有模块
pygame.display.set_caption('贪吃蛇')  # 设置窗口标题
size = width, height = 800, 600

screen = pygame.display.set_mode(size)  # 创建一个窗口

black = 0, 0, 0  # 定义黑色的rgb值

snake_head_color = pygame.Color(220, 220, 220)
snake_head_pos = (10, 10)
snake_head_size = (5, 5)
snake_head = pygame.Rect(snake_head_pos, snake_head_size)  # 创建一个蛇头

food_color = pygame.Color(255, 0, 0)
food_pos_width = random.randint(0, width)
food_pos_height = random.randint(0, height)
food_pos = (food_pos_width, food_pos_height)
food_size = (5, 5)
food = pygame.Rect(food_pos, food_size)  # 创建一个食物

# 移动速度(每次移动的像素值)
speed = 3
# 移动单位
move_right = (speed, 0)
move_left = (-speed, 0)
move_up = (0, -speed)  # 越往上, top值越小
move_down = (0, speed)
# 移动方向
move_to = move_right  # 初始方向为向右


def game_over(screen):
    # pygame.font.Font: 创建一个字体对象
    font = pygame.font.Font(None, 72)
    # pygame.font.Font.render: 画字到一个suface
    font_surface = font.render("GAME OVER!", True, (255, 255, 0), black)
    # pygame.Surface.get_size: 获取suface的尺寸
    font_rect = font_surface.get_rect()
    # 把窗口的中心位置 赋值给suface的中心位置
    font_rect.center = screen.get_rect().center
    # blit: 把suface画到窗口
    screen_rect = screen.blit(font_surface, font_rect)
    # update: 局部更新窗口
    pygame.display.update(screen_rect)
    # 等待游戏退出
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        time.sleep(0.1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:  # 只监听按键按下
            if event.key == pygame.K_UP and move_to != move_down:  # 要排除相反的方向
                move_to = move_up
            if event.key == pygame.K_DOWN and move_to != move_up:
                move_to = move_down
            if event.key == pygame.K_LEFT and move_to != move_right:
                move_to = move_left
            if event.key == pygame.K_RIGHT and move_to != move_left:
                move_to = move_right
    # 越界退出游戏
    if snake_head.left < 0 or snake_head.right > width:
        game_over(screen)
    if snake_head.top < 0 or snake_head.bottom > height:
        game_over(screen)

    screen.fill(black)  # 填充黑色背景

    # 每次循环加上一个移动单位, 生成新的位置
    snake_head = snake_head.move(move_to)
    pygame.draw.rect(screen, snake_head_color, snake_head)  # 画蛇头

    pygame.draw.rect(screen, food_color, food)  # 画食物

    pygame.display.flip()  # 刷新屏幕
