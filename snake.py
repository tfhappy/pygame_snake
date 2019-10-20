# -*- coding:utf-8 -*-
import sys
import time

import pygame
import random

# 颜色
black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (220, 220, 220)
white = (255, 255, 255)
red = (255, 0, 0)

# 尺寸
cell_length = 10  # 单位长度
rows, columns = 100, 50  # 行数, 列数

# 初始位置相关
snake_head_pos = (10, 10)
food_pos = (30, 30)

# 速度
re_frame = 1  # 每个动作重复多少帧, 数字越大移动越慢, 最小为1

screen_width = rows * cell_length
screen_height = columns * cell_length
screen_size = (screen_width, screen_height)
cell_size = (cell_length, cell_length)

pygame.init()  # 初始化所有模块
pygame.display.set_caption('贪吃蛇')  # 设置窗口标题
screen = pygame.display.set_mode(screen_size)  # 创建一个窗口

# 蛇头
snake_head_color = pygame.Color(*gray)
snake_head = pygame.Rect(snake_head_pos, cell_size)

# 蛇身
snake_body_color = pygame.Color(*white)
snake_body = []


def collide(snake_head, snake_body, food):
    if snake_head.colliderect(food):
        return True
    if snake_head.collidelist(snake_body) != -1:
        return True
    if food.collidelist(snake_body) != -1:
        return True

    return False


def create_food(snake_head, snake_body):
    snake_lens = len(snake_body) + 1
    cell_num = rows * columns
    if snake_lens < int(cell_num / 2):
        # 蛇的长度小于屏幕的一半, 随机生成
        while True:
            food_pos_left = random.randrange(0, rows, 1)
            food_pos_top = random.randrange(0, columns, 1)
            food_pos = (food_pos_left * cell_length,
                        food_pos_top * cell_length)
            food = pygame.Rect(food_pos, cell_size)
            if not collide(snake_head, snake_body, food):
                break
    else:
        select_point = []
        for top in range(columns):
            for left in range(rows):
                left_s = left * cell_length
                top_s = top * cell_length
                if snake_head.collidepoint(left_s, top_s):
                    continue
                is_collide = False
                for body_item in snake_body:
                    if body_item.collidepoint(left_s, top_s):
                        is_collide = True
                        break
                if not is_collide:
                    select_point.append((left_s, top_s))
        if len(select_point) == 0:
            print("没有空余的地方生成食物了,你赢了")
            game_over()
        food_pos = select_point[random.randint(0, len(select_point) - 1)]
        food = pygame.Rect(food_pos, cell_size)
    return food


food_color = pygame.Color(*red)
food = pygame.Rect(food_pos, cell_size)

# 移动单位
move_right = (cell_length, 0)
move_left = (-cell_length, 0)
move_up = (0, -cell_length)  # 越往上, top值越小
move_down = (0, cell_length)
# 移动方向
move_to = move_right  # 初始方向为向右


def game_over():
    # pygame.font.Font: 创建一个字体对象
    font = pygame.font.Font(None, 72)
    # pygame.font.Font.render: 画字到一个suface
    font_surface = font.render("GAME OVER!", True, yellow, black)
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
        event = pygame.event.wait()
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q: sys.exit()


def new_view(snake_head, snake_body, food):
    # 越界退出游戏
    if snake_head.left < 0 or snake_head.right > screen_width:
        game_over()
    if snake_head.top < 0 or snake_head.bottom > screen_height:
        game_over()

    screen.fill(black)  # 填充黑色背景

    need_create_food = False
    # 记录原始头的块
    snake_head_origin = snake_head.copy()
    # 每次循环加上一个移动单位, 生成新的位置
    snake_head = snake_head.move(move_to)

    snake_body.append(snake_head_origin)  # 蛇头放一个
    if snake_head.colliderect(food):  # 吃到食物
        need_create_food = True
    else:
        snake_body = snake_body[1:]  # 移除尾巴; 尾巴放列表前面

    if snake_head.collidelist(snake_body) != -1:
        game_over()
    if need_create_food:
        food = create_food(snake_head, snake_body)

    return snake_head, snake_body, food


count = 0
while True:
    if count < re_frame:
        count += 1
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:  # 只监听按键按下
                if event.key == pygame.K_UP and move_to != move_down:  # 要排除相反的方向
                    move_to = move_up
                    break
                if event.key == pygame.K_DOWN and move_to != move_up:
                    move_to = move_down
                    break
                if event.key == pygame.K_LEFT and move_to != move_right:
                    move_to = move_left
                    break
                if event.key == pygame.K_RIGHT and move_to != move_left:
                    move_to = move_right
                    break
                if event.key == pygame.K_q:
                    sys.exit()
        snake_head, snake_body, food = new_view(snake_head, snake_body, food)
        count = 0

    # 画身子
    for body_item in snake_body:
        pygame.draw.rect(screen, snake_body_color, body_item)

    pygame.draw.rect(screen, snake_head_color, snake_head)  # 画蛇头
    pygame.draw.rect(screen, food_color, food)  # 画食物

    pygame.display.flip()  # 刷新屏幕