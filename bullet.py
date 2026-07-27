"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Represent and control an individual laser fired by the player.
Starter code: Based on the Alien Invasion classroom starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """Represent a laser fired from the player's ship."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Create a laser at the ship's current position."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h),
        )

        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the laser upward across the screen."""
        self.y -= self.settings.bullet_speed
        self.rect.y = round(self.y)

    def draw_bullet(self) -> None:
        """Draw the laser at its current position."""
        self.screen.blit(self.image, self.rect)

