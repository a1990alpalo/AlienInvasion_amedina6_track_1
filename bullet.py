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
    """Represent a horizontal laser fired from the player's ship."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Create a right-moving laser beside the ship."""
        super().__init__()

        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.bullet_w, self.settings.bullet_h),
        )

        # Rotate the upward-facing laser to it points right.
        self.image = pygame.transform.rotate(self.image, -90)

        # Position the laser at the right side of the ship.
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.rect.left += 10
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the laser horizontally toward the right edge."""
        self.x += self.settings.bullet_speed
        self.rect.x = round(self.x)

    def draw_bullet(self) -> None:
        """Draw the laser at its current position."""
        self.screen.blit(self.image, self.rect)

