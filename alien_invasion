#https://blog.csdn.net/wyh196646/article/details/82990775
import pygame
from  pygame.sprite import  Group
from setting import Settings
from ship import Ship
#from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():


    """初始化游戏并创建对象"""
    pygame.init()#初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#创建一个名为screen的显示窗口
    pygame.display.set_caption("Alien Invasion")
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")
    #创建一艘飞船,一个子弹编组和一个外星人编组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    #alien = Alien(ai_settings,screen)

    gf.create_fleet(ai_settings,screen,ship,aliens)
    #创建一个用于贮存游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)


    #开始游戏的主循环
    while True:

        #监听键盘和鼠标事件
        gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,
                      bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,stats,sb,ship,
                                  aliens,bullets)
            gf.update_aliens(ai_settings,screen,stats,sb,ship,aliens,bullets)

        gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,
                         play_button)





run_game()




