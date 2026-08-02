"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Represent and control an alien that advances horizontally
toward the player's ship.
Starter code: Adapted from the Alien Invasion classroom project:
https://github.com/a1990alpalo/alien-invasion-
Original starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: August 1, 2026
"""

from typing import TYPE_CHECKING

import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet


class Alien(Sprite):
    """Represent one alien in the side-scrolling fleet."""

    def __init__(
            self,
            fleet: "AlienFleet",
            x_position: float,
            y_position: float,
    ) -> None:
        """Initialize the alien and place it at the supplied coordinates."""
        super().__init__()

        self.fleet = fleet
        self.game = fleet.game 
        self.screen = self.game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = self.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.alien_w, self.settings.alien_h),
        )

        self.rect = self.image.get_rect()
        self.rect.x = int(x_position)
        self.rect.y = int(y_position)

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the alien horizontally toward the left side of the screen."""
        self.x -= self.settings.fleet_speed
        self.rect.x = round(self.x)

    def reached_left_edge(self) -> bool:
        """Return True when the alien reaches the edge behind the ship."""
        return self.rect.left <= self.boundaries.left

    def draw_alien(self) -> None:
        """Draw the alien at its current position."""
        self.screen.blit(self.image, self.rect)
    