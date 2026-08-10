"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Track the player's score, high score, maximum session score,
remaining lives, and current level.
Starter code: Adapted from the Alien Invasion classroom project:
https://github.com/a1990alpalo/alien-invasion-
Original starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: August 9, 2026
"""

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """Track statistics for the current game and saved high score."""

    def __init__(self, game: "AlienInvasion") -> None:
        """Initialize the statistics manager and load the saved high score."""
        self.settings = game.settings
        self.max_score = 0
        self.high_score = 0

        self._load_high_score()
        self.reset_stats()

    def reset_stats(self) -> None:
        """Reset statistics that should start over with each new game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update_score(self, destroyed_aliens: int) -> None:
        """Add points for destroyed aliens and update score records."""
        self.score += destroyed_aliens * self.settings.alien_points

        self._update_max_score()
        self._update_high_score()

    def increase_level(self) -> None:
        """Increase the current level after the fleet is destroyed."""
        self.level += 1

    def lose_ship(self) -> None:
        """Remove one remaining ship after the player is hit."""
        if self.ships_left > 0:
            self.ships_left -= 1

    def _update_max_score(self) -> None:
        """Update the highest score earned during this program session."""
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_high_score(self) -> None:
        """Update and save the all-time high score when it is surpassed."""
        if self.score > self.high_score:
            self.high_score = self.score
            self._save_high_score()

    def _load_high_score(self) -> None:
        """Load the all-time high score from the JSON score file."""
        score_path = self.settings.scores_file

        try:
            contents = score_path.read_text(encoding="utf-8")
            saved_scores = json.loads(contents)
            self.high_score = saved_scores.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            self.high_score = 0
            self._save_high_score()

    def _save_high_score(self) -> None:
        """Save the all-time high score to the JSON score file."""
        score_path = self.settings.scores_file
        score_path.parent.mkdir(parents=True, exist_ok=True)

        saved_scores = {
            "high_score": self.high_score,
        }

        contents = json.dumps(saved_scores, indent=4)
        score_path.write_text(contents, encoding="utf-8")