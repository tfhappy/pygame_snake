# -*- coding:utf-8 -*-
import sys, time
import pygame

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

while True:
    for event in pygame.event.get():  # 获取事件
        if event.type == pygame.QUIT: sys.exit()  # 如果是退出事件(点击关闭), 则退出程序
    time.sleep(1)  # 休眠1s, 避免循环太快, 以后会删掉这行代码
