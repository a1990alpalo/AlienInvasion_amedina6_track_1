"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Initialize Pygame, manage the main game loop, process player
input, and update the game display.
Starter code: Based on the Alien Invasion classroom starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""

import sys
import pygame
from settings import Settings 
from ship import Ship
from arsenal import Arsenal
from alien_fleet import AlienFleet
from game_stats import GameStats
from hud import HUD
from button import Button

class AlienInvasion: 
    """Manage the game resources, events, updates, and main loop."""
    
    def __init__(self) -> None:
        """Initialize Pygame and create the game resources."""
        pygame.init()
        self.settings = Settings()
        self.game_stats = GameStats(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bf = pygame.transform.scale(self.bg, 
            (self.settings.screen_w, self.settings.screen_h),
            )
        

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        
        self.ship = Ship(self, Arsenal(self))
        self.hud = HUD(self)
        self.alien_fleet = AlienFleet(self)
        self.play_button = Button(self, "Play")

        self.game_active = False
        pygame.mouse.set_visible(True)
    
    def run_game(self)-> None:
        """Run the main game loop until the player exits."""
        #Game Loop 
        while self.running:
            self._check_events()

            if self.game_active: 
                self.ship.update()
                self.alien_fleet.update()

            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def restart_game(self) -> None:
        """Reset the ship, lasers, and alien fleet after a loss."""
        self.ship.arsenal.arsenal.empty()
        self.ship.reset_position()
        self.alien_fleet.reset_fleet()

    def _update_screen(self)-> None:
        """Draw the current game objects and refresh the display."""
        # Game loop
        self.screen.blit(self.bf, (0, 0))
        self.alien_fleet.draw()
        self.ship.draw()
        self.hud.draw()

        if not self.game_active:
            self.play_button.draw()

        pygame.display.flip()

    def _check_events(self)-> None:
        """Respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_play_button(event.pos)

    def _check_play_button(
            self,
            mouse_position: tuple[int, int],
    ) ->None:
        """Start a new game when the inactive Play button is clicked."""
        button_was_clicked = self.play_button.was_clicked(mouse_position)

        if button_was_clicked and not self.game_active:
            self._start_new_game()

    def _start_new_game(self) -> None:
        """Reset game and restart a new active game."""
        self.game_stats.reset_stats()
        self.ship.arsenal.arsenal.empty()
        self.ship.reset_position()
        self.alien_fleet.reset_fleet()
        self.hud.update_all()

        self.game_active = True
        pygame.mouse.set_visible(False)
                

            
    def _check_keyup_events(self, event)-> None:
        """Stop vertical movement when a movement key is released."""
        if event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = False
    
    
    def _check_keydown_events(self, event) -> None:
        """Respond when the player presses a supported key."""
        if event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

        if not self.game_active:
            return

        if event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
