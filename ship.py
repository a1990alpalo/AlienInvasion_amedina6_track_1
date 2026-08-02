"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Represent the player's ship and manage its movement, drawing,
and laser-firing behavior.
Starter code: Based on the Alien Invasion classroom starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 26, 2026
"""

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal


class Ship:
    """Represent the player's ship and its available arsenal."""

    def __init__(
        self,
        game: "AlienInvasion",
        arsenal: "Arsenal",
    ) -> None:
        """Initialize the ship's image, position, movement, and arsenal."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image,
            (self.settings.ship_w, self.settings.ship_h),
        )

        #Rotate the upward facing ship clockwise so it faces right.
        self.image = pygame.transform.rotate(self.image, -90)

        #Start the ship near the middle of the left edge.
        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        self.rect.left = 20

        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal

    def update(self) -> None:
        """Update the ship's position and active lasers."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self) -> None:
        """Move the ship vertically while keeping it on the screen."""
        temporary_speed = self.settings.ship_speed

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temporary_speed

        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temporary_speed

        self.rect.y = round(self.y)

    def draw(self) -> None:
        """Draw the active lasers and ship on the screen."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """Attempt to fire a laser and report whether one was created."""
        return self.arsenal.fire_bullet()

    def reset_position(self) -> None:
        """Return the ship to its starting position and stop movement."""
        self.rect.midleft = self.boundaries.midleft
        self.rect.left = 20
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False