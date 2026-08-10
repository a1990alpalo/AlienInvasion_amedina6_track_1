"""
Program: Alien Invasion: Side Strike - Track 1
Author: Alberto Medina
Purpose: Store configuration values and portable asset paths for the game. 
Starter code: Based on the Alien Invasion classroom starter repository: 
https://github.com/RedBeard41/alien_Invasion_starter
Date: July 26, 2026 
"""

from pathlib import Path


class Settings:
    """Store static configuration values for the game."""

    def __init__(self) -> None:
        """Initialize screen, ship, laser, sound, and asset settings."""
        self.name = "Alien Invasion: Side Strike - Track 1"
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60

        base_directory = Path(__file__).resolve().parent
        asset_directory = base_directory / "Assets"

        self.bg_file = (
            asset_directory
            / "images"
            / "Starbasesnow.png"
        )

        self.ship_file = (
            asset_directory
            / "images"
            / "ship2(no bg).png"
        )

        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.alien_file = (
            asset_directory
            / "images"
            / "enemy_4.png"
        )
        self.alien_w = 60
        self.alien_h = 60
        self.fleet_speed = 1
        self.starting_ship_count = 3
        self.alien_points = 50

        self.bullet_file = (
            asset_directory
            / "images"
            / "laserBlast.png"
        )
        self.bullet_speed = 7
        self.bullet_w = 35
        self.bullet_h = 80
        self.bullet_amount = 10

        self.laser_sound = (
            asset_directory
            / "sound"
            / "laser.mp3"
        )

        self.scores_file = (
            asset_directory
            / "files"
            / "scores.js"
        )

        self.font_file = (
            asset_directory
            / "Fonts"
            / "Silkscreen"
            / "Silkscreen-Regular.ttf"
        )
        self.hud_font_size = 24
        self.text_color = (255, 255, 255)