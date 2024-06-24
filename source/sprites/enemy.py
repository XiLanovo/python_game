# import pygame
#
#
# class Snake(pygame.sprite.Sprite):
#     # 定义构造函数
#     def __init__(self, filename, location):
#         # 调父类来初始化子类
#         pygame.sprite.Sprite.__init__(self)
#         # 加载图片，并转换为掩码
#         self.image = pygame.image.load(filename).convert_alpha()
#         self.mask = pygame.mask.from_surface(self.image)
#         # 获取图片rect区域
#         self.rect = self.image.get_rect()
#         # 设置位置
#         self.rect.topleft = location
#
# # 初始化pygame
# pygame.init()
# screen = pygame.display.set_mode((800, 600))
# pygame.display.set_caption('C语言中文网')
#
# # 填充为白色屏幕
# screen.fill((255, 255, 255))
#
# # 定义蛇的图片路径和位置
# filename = "/source/image/snake.png"
# location = (10, 150)
# snake1 = Snake(filename, location)
#
# # 定义第二个蛇的图片路径和位置
# location_2 = (450, 60)
# snake2_filename = '/source/image/logo.png'
# snake2 = Snake(snake2_filename, location_2)
#
# # 使用mask来检测碰撞
# crash_result = pygame.sprite.collide_mask(snake1, snake2)
# if crash_result:
#     print("精灵碰撞了!")
# else:
#     print('精灵没碰撞')
#
# # 游戏主循环
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # 绘制精灵到屏幕上
#     screen.blit(snake1.image, snake1.rect)
#     screen.blit(snake2.image, snake2.rect)
#
#     # 刷新显示屏幕
#     pygame.display.update()
#
#     # 这里可以添加移动蛇的代码
#
# # 退出pygame
# pygame.quit()