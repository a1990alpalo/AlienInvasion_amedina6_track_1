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

from pygame.sprite import Group, groupcollide, spritecollideany

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
        """Update all aliens and process laser collisions and loss collisions."""
        self.aliens.update()
        self._check_laser_collisions()
        self._check_loss_conditions()


    def _check_loss_conditions(self) -> None:
        """Restart the game when an alien hits the ship or left the edge."""
        ship_was_hit = (
            spritecollideany(self.game.ship, self.aliens) is not None
        )
        alien_reached_edge = any(
            alien.reached_left_edge()
            for alien in self.aliens
        )

        if ship_was_hit or alien_reached_edge:
            self.game.restart_game()


    def _check_laser_collisions(self) -> None:
        """Award points and remove aliens and lasers after collisions."""
        lasers = self.game.ship.arsenal.arsenal

        collisions = groupcollide(
            self.aliens,
            lasers,
            True,
            True,
        )

        if collisions:
            destroyed_aliens = len(collisions)
            self.game.game_stats.update_score(destroyed_aliens)
            self.game.hud.update_all()

        if not self.aliens:
            self.game.game_stats.increase_level()
            self.game.hud.update_all()
            self._create_fleet()

    def reset_fleet(self) -> None:
        """Remove the current aliens and create a new fleet."""
        self.aliens.empty()
        self._create_fleet()

    def draw(self) -> None:
        """Draw every alien in the fleet."""
        self.aliens.draw(self.screen)