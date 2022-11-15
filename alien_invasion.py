import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gfn


def  run_game():

    #Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    #Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, stats, screen)

    #Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    #Make a ship, group of bullets and group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()


    #Create a fleet of alien
    gfn.create_fleet(ai_settings, screen, ship, aliens)

    #Main loop for the game.
    while True:

        gfn.check_events(ai_settings, stats, sb, screen, ship, bullets, aliens, play_button)
        
        if stats.game_active:
            ship.update()
            gfn.update_bullets(ai_settings, stats, sb, screen, ship, bullets, aliens)
            gfn.update_aliens(ai_settings, stats, screen, ship, bullets, aliens)
        
        gfn.update_screen(ai_settings, stats, sb, screen, ship, bullets, aliens, play_button)
        
     
run_game()
