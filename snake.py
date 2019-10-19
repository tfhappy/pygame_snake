# -*- coding:utf-8 -*-
import sys
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

# 移动速度(每次移动的像素值)
speed = 3
# 移动单位
move_right = (speed, 0)
move_left = (-speed, 0)
move_up = (0, -speed)  # 越往上, top值越小
move_down = (0, speed)
# 移动方向
move_to = move_right  # 初始方向为向右
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)  # 填充黑色背景

    # 每次循环加上一个移动单位, 生成新的位置
    snake_head = snake_head.move(move_to)
    pygame.draw.rect(screen, snake_head_color, snake_head)  # 画蛇头

    pygame.draw.rect(screen, food_color, food)  # 画食物

    pygame.display.flip()  # 刷新屏幕
