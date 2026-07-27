"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Create, update, draw, and remove the player's active lasers.
Starter code: Based on the Alien Invasion classroom starter respository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""


import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal: 
    """Manage the collection of lasers fired by the player's ship"""

    def __init__(self, game: 'AlienInvasion'):
        """Create an empty group for active lasers."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """Update every laser and remove lasers that leave the screen."""
        self.arsenal.update()
        self._remove_bullets_offscreen()


    def _remove_bullets_offscreen(self):
        """Remove lasers that have traveled beyond the top edge."""
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """Draw all active lasers."""
        for bullet in self.arsenal:
            bullet.draw_bullet()        
        
    def fire_bullet(self):
        """Create a laser if the maximum active-laser limit allows it."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False

