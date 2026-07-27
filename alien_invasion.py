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

class AlienInvasion: 
    """Manage the game resources, events, updates, and main loop."""
    
    def __init__(self) -> None:
        """Initialize Pygame and create the game resources."""
        pygame.init()
        self.settings = Settings()

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
    
    def run_game(self)-> None:
        """Run the main game loop until the player exits."""
        #Game Loop 
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self)-> None:
        """Draw the current game objects and refresh the display."""
        # Game loop
        self.screen.blit(self.bf, (0, 0))
        self.ship.draw()     
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
                

            
    def _check_keyup_events(self, event)-> None:
        """Stop vertical movement when a movement key is released."""
        if event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = False
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = False
    
    
    def _check_keydown_events(self, event)-> None:
        """Respond when the player presses a supported key."""
        if event.key in (pygame.K_UP, pygame.K_w):
            self.ship.moving_up = True
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()
        
            



if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
