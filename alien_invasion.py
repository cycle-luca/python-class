"""
Author:  shangxianjiang@gmail.com
Date: 2024-06-20 21:05:16
LastEditors:  shangxianjiang@gmail.com
LastEditTime: 2024-06-20 21:05:20
FilePath: /python-class/alien_invasion.py
Description: import pygame

Copyright (c) 2024 by shangxianjiang@gmail.com, All Rights Reserved. 
"""

import sys
import pygame


from settings import settings


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并且创建游戏资源"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.seetings = settings()
        self.screen = pygame.display.set_mode(
            (self.seetings.screen_width, self.seetings.screen_height)
        )
        pygame.display.set_caption("外星人入侵")

    def run_game(self):
        """开始游戏住循环"""
        while True:
            # 侦听键盘和鼠标时间
            for event in pygame.event.get():
                if event.type == pygame.quit:
                    sys.exit()
            # 每次循环都重绘屏幕
            self.screen.fill(self.seetings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    # 创建游戏实例
    ai = AlienInvasion()
    ai.run_game()
