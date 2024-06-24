import pygame as pg
from pygame.locals import *
from source.states.died_menu import died_menu

class Player:
    def __init__(self, x, y, image_path, walk_image_path, jump_image_path, screen_width, screen_height):
        self.initial_x = x
        self.initial_y = y
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pg.mask.from_surface(self.image)  # 创建遮罩

        self.walk_images = [self.image]  # 初始行走帧列表包含站立图像
        self.load_walk_animation(walk_image_path)
        self.jump_images = [self.image]  # 初始跳跃帧列表包含站立图像
        self.fall_images = [self.image]  # 初始下落帧列表包含站立图像
        self.load_jump_animation(jump_image_path)
        self.current_image = self.image  # 当前显示的图像
        self.state = 'stand'  # 初始状态为站立
        self.animation_frame = 0
        self.animation_timer = pg.time.get_ticks()

        self.velocity_x = 0  # 水平速度
        self.velocity_y = 0  # 垂直速度
        self.gravity = 0.3  # 重力加速度
        self.jump_speed = -7  # 跳跃速度
        self.walk_speed = 3  # 行走速度
        self.on_ground = True  # 初始在地面上
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.facing_left = False  # 初始朝向向右
        self.max_fall_speed = 13  # 设置最大下落速度
        self.jump_hold_time = 0.3  # 跳跃时保持初始速度的时间
        self.double_jumped = False  # 初始化第二段跳跃状态

        # 跳跃和下落动画的当前帧索引
        self.jump_frame_index = 0
        self.fall_frame_index = 0

    def check_wall_collision_x(self, wall_tiles, dx):
        for tile in wall_tiles:
            if self.rect.colliderect(tile.rect):  # 使用矩形进行碰撞检测
                if dx > 0:
                    self.rect.right = tile.rect.left
                elif dx < 0:
                    self.rect.left = tile.rect.right

    def check_wall_collision_y(self, wall_tiles):
        for tile in wall_tiles:
            if pg.sprite.collide_mask(self, tile):  # 使用遮罩进行碰撞检测
                if self.velocity_y < 0:
                    self.rect.top = tile.rect.bottom
                    self.velocity_y = 0  # 碰到墙体时向上速度变为0
                elif self.velocity_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    self.double_jumped = False
                    self.jump_frame_index = 0
                    self.fall_frame_index = 0
                    self.state = 'stand'

    def check_trap_collision(self, trap_tiles):
        for tile in trap_tiles:
            if pg.sprite.collide_mask(self, tile):  # 使用遮罩进行碰撞检测
                return True
        return False

    def load_jump_animation(self, jump_image_path):
        jump_image = pg.image.load(jump_image_path).convert_alpha()
        for i in range(8):  # 从256*32的图片中切分出8个32*32的帧
            frame = jump_image.subsurface(pg.Rect(i * 32, 0, 32, 32))
            if i < 4:
                self.jump_images.append(frame)
            else:
                self.fall_images.append(frame)

    def load_walk_animation(self, walk_image_path):
        walk_image = pg.image.load(walk_image_path).convert_alpha()
        for i in range(6):  # 从192*32的图片中切分出6个32*32的帧
            frame = walk_image.subsurface(pg.Rect(i * 32, 0, 32, 32))
            self.walk_images.append(frame)

    def reset_position(self):
        self.rect.topleft = (self.initial_x, self.initial_y)
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = True
        self.state = 'stand'
        self.current_image = self.image

    def update(self, wall_tiles, trap_tiles):
        # 如果玩家不在地面上，应用重力
        if not self.on_ground:
            self.velocity_y += self.gravity
            # 检查是否达到最大下落速度
            if self.velocity_y > self.max_fall_speed:
                self.velocity_y = self.max_fall_speed
            if self.velocity_y > 0 and self.state == 'jump':
                self.state = 'fall'
            elif self.velocity_y == 0:
                self.state = 'stand'

            # 应用垂直速度
            self.rect.y += self.velocity_y
            self.check_wall_collision_y(wall_tiles)

            # 检查是否到达地面
            if self.rect.bottom > self.screen_height:
                self.rect.bottom = self.screen_height
                self.velocity_y = 0  # 重置垂直速度
                self.on_ground = True
                self.double_jumped = False  # 重置第二段跳跃状态
                self.jump_frame_index = 0  # 重置跳跃帧索引
                self.fall_frame_index = 0  # 重置下落帧索引
                self.state = 'stand'

        if self.rect.bottom >= self.screen_height:
            died_menu()

            # 检查玩家脚下是否有墙体
        if self.on_ground:
            self.check_fall(wall_tiles)

        # 检查玩家是否碰到了陷阱
        if self.check_trap_collision(trap_tiles):
            died_menu()

        # 用于控制动画帧切换的计时器
        current_time = pg.time.get_ticks()
        if current_time - self.animation_timer > 100:  # 200毫秒切换一次动画帧
            if self.state == 'walk':
                self.animation_frame = (self.animation_frame + 1) % len(self.walk_images)
                self.current_image = self.walk_images[self.animation_frame]
            elif self.state == 'jump':
                self.current_image = self.jump_images[self.jump_frame_index]
            elif self.state == 'fall':
                self.current_image = self.fall_images[self.fall_frame_index]
            self.animation_timer = current_time  # 更新计时器

    def draw(self, screen):
        image_to_draw = self.current_image
        # 根据当前状态选择图像
        if self.state == 'jump':
            # 如果处于跳跃状态，使用跳跃动画的当前帧
            image_to_draw = self.jump_images[self.jump_frame_index]
        elif self.state == 'fall':
            # 如果处于跳跃状态，使用跳跃动画的当前帧
            image_to_draw = self.fall_images[self.fall_frame_index]
        elif self.state == 'walk':
            # 如果处于行走状态，使用行走动画的当前帧
            image_to_draw = self.walk_images[self.animation_frame]
        elif self.state == 'stand':
            # 如果处于站立状态，使用站立图像
            image_to_draw = self.image

        # 根据 facing_left 值决定是否翻转图像
        if self.facing_left:
            image_to_draw = pg.transform.flip(image_to_draw, True, False)
        screen.blit(image_to_draw, self.rect.topleft)
        self.mask = pg.mask.from_surface(image_to_draw)  # 更新遮罩

    def move(self, keys, delta_time, wall_tiles, trap_tiles):
        # 水平移动
        if keys[K_a]:
            self.rect.x -= self.walk_speed
            self.check_wall_collision_x(wall_tiles, -self.walk_speed)
            self.facing_left = True
            if self.on_ground:
                self.state = 'walk'
        elif keys[K_d]:
            self.rect.x += self.walk_speed
            self.check_wall_collision_x(wall_tiles, self.walk_speed)
            self.facing_left = False
            if self.on_ground:
                self.state = 'walk'
        else:
            self.velocity_x = 0
            self.state = 'stand'
            self.current_image = self.image  # 切换回站立图像

        # 处理跳跃逻辑
        if keys[K_SPACE]:
            if self.on_ground:
                # 第一次跳跃
                self.velocity_y = self.jump_speed
                self.state = 'jump'
                self.on_ground = False
                self.double_jumped = False  # 重置第二段跳跃状态
                self.current_image = self.jump_images[0]
            elif not self.double_jumped and self.velocity_y > 0 and not self.on_ground:
                # 允许在空中进行第二段跳跃
                self.velocity_y = self.jump_speed
                self.state = 'jump'
                self.double_jumped = True  # 标记已进行第二段跳跃
            else:
                # 跳跃后立即应用重力
                self.update(wall_tiles, trap_tiles)

        self.rect.x += self.velocity_x  # 更新位置
        self.update(wall_tiles, trap_tiles)

        # 确保玩家不会移出屏幕边界
        self.rect.x = max(0, min(self.screen_width - self.image.get_width(), self.rect.x))
        self.rect.y = max(0, min(self.screen_height - self.image.get_height(), self.rect.y))

    def check_fall(self, wall_tiles):
        self.rect.y += 1  # 向下试探1个像素
        for tile in wall_tiles:
            if pg.sprite.collide_mask(self, tile):  # 使用遮罩进行碰撞检测
                self.rect.y -= 1  # 恢复位置
                return
        self.rect.y -= 1  # 恢复位置
        self.on_ground = False
        self.state = 'fall'
