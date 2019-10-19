# -*- coding:utf-8 -*-
import sys, time
import pygame
import random

# 初始化所有模块，当你不知道需要用到哪些模块的时候，可以这样做
# 初始化就是做一些准备工作，你可以认为是固定用法，想用pygame， 就得先调用这个init()函数
pygame.init()

# 连续赋值写法
# 等价下面三行代码:
# size = (800,600) # 这里是元组类型，你可以认为是列表
# width = 800
# height = 600
size = width, height = 800, 600

# 创建一个窗口
screen = pygame.display.set_mode(size)

# 定义黑色的rgb值，这里black的类型是元组。你可以认为是一个列表
# 等价 black = (0, 0, 0)
# 我们用一个元组来描述了黑色的rgb值
# 颜色对应rgb值是什么可以在http://tool.oschina.net/commons?type=3 查到
black = 0, 0, 0

# 定义蛇头的颜色
snake_head_color = pygame.Color(220, 220, 220)
# 定义蛇头初始位置(坐标原点在左上角)
snake_head_pos = (10, 10)
# 定义蛇头大小（宽,高）
snake_head_size = (5, 5)
# 创建一个蛇头
snake_head = pygame.Rect(snake_head_pos, snake_head_size)

# 定义食物的颜色
food_color = pygame.Color(255, 0, 0)
# 定义食物位置
food_pos_width = random.randint(0, width)  # 随机生成横坐标
food_pos_height = random.randint(0, height)  # 随机生成纵坐标
food_pos = (food_pos_width, food_pos_height)
# 定义食物大小
food_size = (5, 5)
# 创建一个食物
food = pygame.Rect(food_pos, food_size)

while True:
    for event in pygame.event.get():  # 获取事件
        if event.type == pygame.QUIT: sys.exit()  # 如果是退出事件(点击关闭), 则退出程序

    # 额...这里参数一开始就应该是black, 而不是写死的(0,0,0) 忽略这里的改动
    screen.fill(black)  # 填充黑色背景, (0,0,0)

    # 画蛇头到屏幕中
    pygame.draw.rect(screen, snake_head_color, snake_head)

    # 画食物到食物中
    pygame.draw.rect(screen, food_color, food)

    pygame.display.flip()  # 刷新整个窗口, 如果不刷新，那对屏幕的改动无法生效

    time.sleep(1)  # 休眠1s, 避免循环太快, 以后会删掉这行代码
