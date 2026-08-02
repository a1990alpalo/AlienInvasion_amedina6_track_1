"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina 
Purpose: Create and manage the fleet of aliens that advances toward
the player's ship.
Starter code: Adapted from the Alien Invasion classroom project:
https://github.com/a1990alpalo/alien-invasion-
Original starter repository:
https://github.com/RedBeard41/alien_Invasion_starter
Date: August 2, 2026"""

from typing import TYPE_CHECKING

from pygame.sprite import Group, groupcollide

from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Create and manage the game's alien fleet."""
    def __init__(self, game:"AlienInvasion") -> None:
        """Initialize the fleet and create the aliens."""
        self.game = game 
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()

        self.aliens = Group()

        self._create_fleet()

    def _create_fleet(self) -> None:
        """Create rows of aliens on the right half of the screen."""
        horizontal_spacing = self.settings.alien_w * 2
        vertical_spacing = self.settings.alien_h * 2

        starting_x = self.settings.screen_w // 2 
        ending_x = self.settings.screen_w - self.settings.alien_w
        ending_y = self.settings.screen_h - self.settings.alien_h

        for y_position in range(
            self.settings.alien_h,
            ending_y,
            vertical_spacing,
        ):
            for x_position in range(
                starting_x,
                ending_x,
                horizontal_spacing,
            ):
                self._create_alien(x_position, y_position)

    def _create_alien(
            self,
            x_position: float,
            y_position: float,
    ) -> None:
        """Create one alien and add it to the fleet."""
        alien = Alien(self, x_position, y_position)
        self.aliens.add(alien)

    def update(self) -> None:
        """Update all aliens and process laser collisions."""
        self.aliens.update()
        self._check_laser_collisions()

    def _check_laser_collisions(self) -> None:
        """Remove aliens and lasers involved in collisions."""
        lasers = self.game.ship.arsenal.arsenal

        groupcollide(
            self.aliens,
            lasers,
            True,
            True
        ) 

        if not self.aliens:
            self._create_fleet()   

    def draw(self) -> None:
        """Draw every alien in the fleet."""
        self.aliens.draw(self.screen)