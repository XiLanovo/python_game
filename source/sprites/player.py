import pygame as pg
from pygame.locals import *
from source.states.died_menu import died_menu

class Player:
    def __init__(self, x, y, image_path, walk_image_path, jump_image_path, screen_width, screen_height):
        # 初始化玩家的起始位置和基本属性
        self.initial_x = x
        self.initial_y = y
        self.image = pg.image.load(image_path).convert_alpha()  # 玩家默认图像
        self.rect = self.image.get_rect(topleft=(x, y))  # 玩家的矩形区域
        self.mask = pg.mask.from_surface(self.image)  # 玩家的碰撞掩码

        # 加载行走和跳跃动画帧
        self.walk_images = [self.image]
        self.load_walk_animation(walk_image_path)
        self.jump_images = [self.image]
        self.fall_images = [self.image]
        self.load_jump_animation(jump_image_path)
        self.current_image = self.image  # 当前显示的图像
        self.state = 'stand'  # 玩家的初始状态为站立

        # 玩家的动画帧计数器和计时器
        self.animation_frame = 0
        self.animation_timer = pg.time.get_ticks()

        # 玩家的物理属性
        self.velocity_x = 0  # 玩家的水平速度
        self.velocity_y = 0  # 玩家的垂直速度
        self.gravity = 0.3  # 玩家的重力加速度
        self.jump_speed = -7  # 玩家跳跃时的初始速度
        self.walk_speed = 3  # 玩家行走的速度
        self.on_ground = True  # 玩家是否在地面上
        self.screen_width = screen_width  # 屏幕的宽度
        self.screen_height = screen_height  # 屏幕的高度
        self.facing_left = False  # 玩家面向的方向
        self.max_fall_speed = 13  # 玩家下落的最大速度
        self.jump_hold_time = 0.3  # 跳跃持续的时间
        self.double_jumped = False  # 是否已经进行了二段跳

        # 跳跃和下落动画的当前帧索引
        self.jump_frame_index = 0
        self.fall_frame_index = 0

    def check_wall_collision_x(self, wall_tiles, dx):
        # 检查与墙体的水平碰撞
        for tile in wall_tiles:
            if self.rect.colliderect(tile.rect):
                if dx > 0:
                    self.rect.right = tile.rect.left
                elif dx < 0:
                    self.rect.left = tile.rect.right

    def check_wall_collision_y(self, wall_tiles):
        # 检查与墙体的垂直碰撞
        for tile in wall_tiles:
            if self.rect.colliderect(tile.rect):
                if self.velocity_y < 0:
                    self.rect.top = tile.rect.bottom
                    self.velocity_y = 0
                elif self.velocity_y > 0:
                    self.rect.bottom = tile.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    self.double_jumped = False
                    self.jump_frame_index = 0
                    self.fall_frame_index = 0
                    self.state = 'stand'

    def check_trap_collision(self, trap_tiles):
        # 检查与陷阱的碰撞
        for tile in trap_tiles:
            if pg.sprite.collide_mask(self, tile):
                return True
        return False

    def load_jump_animation(self, jump_image_path):
        # 加载跳跃动画
        jump_image = pg.image.load(jump_image_path).convert_alpha()
        for i in range(8):
            frame = jump_image.subsurface(pg.Rect(i * 32, 0, 32, 32))
            if i < 4:
                self.jump_images.append(frame)
            else:
                self.fall_images.append(frame)

    def load_walk_animation(self, walk_image_path):
        # 加载行走动画
        walk_image = pg.image.load(walk_image_path).convert_alpha()
        for i in range(6):
            frame = walk_image.subsurface(pg.Rect(i * 32, 0, 32, 32))
            self.walk_images.append(frame)

    def reset_position(self):
        # 重置玩家位置
        self.rect.topleft = (self.initial_x, self.initial_y)
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = True
        self.state = 'stand'
        self.current_image = self.image

    def update(self, wall_tiles, trap_tiles):
        # 更新玩家状态
        if not self.on_ground:
            self.velocity_y += self.gravity
            if self.velocity_y > self.max_fall_speed:
                self.velocity_y = self.max_fall_speed
            if self.velocity_y > 0 and self.state == 'jump':
                self.state = 'fall'
            elif self.velocity_y == 0:
                self.state = 'stand'

            self.rect.y += self.velocity_y
            self.check_wall_collision_y(wall_tiles)

            if self.rect.bottom > self.screen_height:
                self.rect.bottom = self.screen_height
                self.velocity_y = 0
                self.on_ground = True
                self.double_jumped = False
                self.jump_frame_index = 0
                self.fall_frame_index = 0
                self.state = 'stand'

        if self.rect.bottom >= self.screen_height:
            pg.mixer.music.stop()
            pg.mixer.music.unload()
            died_menu()

        if self.on_ground:
            self.check_fall(wall_tiles)

        if self.check_trap_collision(trap_tiles):
            pg.mixer.music.stop()
            pg.mixer.music.unload()
            died_menu()

        current_time = pg.time.get_ticks()
        if current_time - self.animation_timer > 100:
            if self.state == 'walk':
                self.animation_frame = (self.animation_frame + 1) % len(self.walk_images)
                self.current_image = self.walk_images[self.animation_frame]
            elif self.state == 'jump':
                self.current_image = self.jump_images[self.jump_frame_index]
            elif self.state == 'fall':
                self.current_image = self.fall_images[self.fall_frame_index]
            self.animation_timer = current_time

    def draw(self, screen):
        # 绘制玩家图像
        image_to_draw = self.current_image
        if self.state == 'jump':
            image_to_draw = self.jump_images[self.jump_frame_index]
        elif self.state == 'fall':
            image_to_draw = self.fall_images[self.fall_frame_index]
        elif self.state == 'walk':
            image_to_draw = self.walk_images[self.animation_frame]
        elif self.state == 'stand':
            image_to_draw = self.image

        if self.facing_left:
            image_to_draw = pg.transform.flip(image_to_draw, True, False)
        screen.blit(image_to_draw, self.rect.topleft)

    def move(self, keys, delta_time, wall_tiles, trap_tiles):
        # 处理玩家移动
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
            self.current_image = self.image

        if keys[K_SPACE]:
            if self.on_ground:
                self.velocity_y = self.jump_speed
                self.state = 'jump'
                self.on_ground = False
                self.double_jumped = False
                self.current_image = self.jump_images[0]
            elif not self.double_jumped and self.velocity_y > 0 and not self.on_ground:
                self.velocity_y = self.jump_speed
                self.state = 'jump'
                self.double_jumped = True
            else:
                self.update(wall_tiles, trap_tiles)

        self.rect.x += self.velocity_x
        self.update(wall_tiles, trap_tiles)

        self.rect.x = max(0, min(self.screen_width - self.image.get_width(), self.rect.x))
        self.rect.y = max(0, min(self.screen_height - self.image.get_height(), self.rect.y))

    def check_fall(self, wall_tiles):
        # 检查是否掉落
        self.rect.y += 1
        for tile in wall_tiles:
            if pg.sprite.collide_mask(self, tile):
                self.rect.y -= 1
                return
        self.rect.y -= 1
        self.on_ground = False
        self.state = 'fall'
