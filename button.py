"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Create and display the Play button used to start a new game.
Starter code: Adapted from the Alien Invasion classroom project:
https://github.com/a1990alpalo/alien-invasion-
Original starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: August 9, 2026
"""

from typing import TYPE_CHECKING

import pygame

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Button:
    """Represent a clickable button displayed on the game screen."""

    def __init__(self, game: "AlienInvasion", message: str) -> None:
        """Initialize the button's dimensions, font, and message."""
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = game.settings

        self.rect = pygame.Rect(
            0,
            0,
            self.settings.button_w,
            self.settings.button_h,
        )
        self.rect.center = self.boundaries.center

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.button_font_size,
        )

        self._prepare_message(message)

    def _prepare_message(self, message: str) -> None:
        """Render the supplied message and center it on the button."""
        self.message_image = self.font.render(
            message,
            True,
            self.settings.text_color,
        )
        self.message_rect = self.message_image.get_rect()
        self.message_rect.center = self.rect.center

    def was_clicked(self, mouse_position: tuple[int, int]) -> bool:
        """Return whether the supplied mouse position is inside the button."""
        return self.rect.collidepoint(mouse_position)

    def draw(self) -> None:
        """Draw the button and its centered message."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_rect)