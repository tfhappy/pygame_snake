# -*- coding:utf-8 -*-
import sys, time
import pygame
import random

pygame.init()  # 初始化所有模块
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

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)  # 填充黑色背景

    pygame.draw.rect(screen, snake_head_color, snake_head)  # 画蛇头
    pygame.draw.rect(screen, food_color, food)  # 画食物

    pygame.display.flip()  # 刷新屏幕
    time.sleep(1)
