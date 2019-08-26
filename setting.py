class Settings():
    """储存 外星人入侵 的所有设置类"""

    def __init__(self):
        """初始化游戏静态设置"""
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #飞船的设置
        self.ship_limit = 3
        #子弹设置
        self.bullet_width = 30
        self.bullet_height = 15
        #self.bullet_color = 60 , 60 , 60
        self.bullets_allowed = 7
        #外星人设置
        self.fleet_drop_speed = 20


        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随着游戏进行二变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet_direction 为1表示向右，为-1表示向左
        self.fleet_direction = 1
        # 记分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度装置,和外星人的点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points *self.score_scale)
        #print(self.alien_points)
        #外星人的点数是随着速度的怎讲不断变化的，初始是50
