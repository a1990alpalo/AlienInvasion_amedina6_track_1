"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Display the game's score, high score, maximum session score,
current level, and remaining ships.
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


class HUD:
    """Display scoring, level, and remaining-life information."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the HUD and prepare its text and ship images."""
        self.game = game
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.settings = game.settings
        self.game_stats = game.game_stats

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.hud_font_size,
        )

        self.life_image = pygame.transform.scale(
            self.game.ship.image,
            (36, 24),
        )

        self.update_all()

    def update_all(self) -> None:
        """Prepare every HUD element using the current game statistics."""
        self._prepare_score()
        self._prepare_high_score()
        self._prepare_max_score()
        self._prepare_level()

    def _prepare_score(self) -> None:
        """Prepare the current-game score image."""
        score_text = f"SCORE: {self.game_stats.score:,}"

        self.score_image = self.font.render(
            score_text,
            True,
            self.settings.text_color,
        )
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - 20
        self.score_rect.top = 55

    def _prepare_high_score(self) -> None:
        """Prepare the saved all-time high-score image."""
        high_score_text = f"HI-SCORE: {self.game_stats.high_score:,}"

        self.high_score_image = self.font.render(
            high_score_text,
            True,
            self.settings.text_color,
        )
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.boundaries.centerx
        self.high_score_rect.top = 15

    def _prepare_max_score(self) -> None:
        """Prepare the highest score from the current program session."""
        max_score_text = f"MAX-SCORE: {self.game_stats.max_score:,}"

        self.max_score_image = self.font.render(
            max_score_text,
            True,
            self.settings.text_color,
        )
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - 20
        self.max_score_rect.top = 15

    def _prepare_level(self) -> None:
        """Prepare the current-level image."""
        level_text = f"LEVEL: {self.game_stats.level}"

        self.level_image = self.font.render(
            level_text,
            True,
            self.settings.text_color,
        )
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = 20
        self.level_rect.top = 55

    def _draw_remaining_ships(self) -> None:
        """Draw one small ship image for each remaining life."""
        ship_spacing = self.life_image.get_width() + 10

        for ship_number in range(self.game_stats.ships_left):
            ship_x = 20 + (ship_number * ship_spacing)
            ship_y = 15
            self.screen.blit(self.life_image, (ship_x, ship_y))

    def draw(self) -> None:
        """Draw every HUD element on the game screen."""
        self._draw_remaining_ships()
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)