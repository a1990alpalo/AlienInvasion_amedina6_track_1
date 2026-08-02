# Alien Invasion: Side Strike - Track 1

A side-scrolling variation of the Alien Invasion game developed with Python and Pygame. This project focuses on custom gameplay mechanics that change the ship’s position, orientation, movement, and firing direction.

## Author

Alberto Medina

## Milestone 1: New Ship Mechanics

Milestone 1 changes the original bottom-up gameplay into a side-scrolling format.

Completed features include:

* The ship begins near the middle of the left edge.
* The ship is rotated to face right.
* The ship moves vertically instead of horizontally.
* Arrow keys and `W`/`S` support vertical movement.
* Screen boundaries prevent the ship from leaving the display.
* Lasers originate from the ship’s right side.
* Lasers travel horizontally toward the right edge.
* Offscreen lasers are removed automatically.
* Up to ten lasers can be active simultaneously.
* The display caption identifies the game and Track 1.
* Asset paths use Python’s `pathlib` library for Windows and macOS compatibility.
* Modules, classes, and functions include descriptive docstrings.

## Milestone 2: Fleet and Collision Logic

Milestone 2 adds an alien fleet and game logic consistent with the new side-scrolling mechanics.

Completed features include:

* Aliens spawn in rows on the right half of the screen.
* The alien fleet moves horizontally from right to left.
* Lasers collide with and destroy aliens.
* Lasers are removed after striking aliens.
* A complete new fleet appears after all aliens are destroyed.
* The game restarts when an alien collides with the ship.
* The game restarts when an alien reaches the left edge behind the ship.
* Restarting clears active lasers and returns the ship to its starting position.
* Modules, classes, and functions include descriptive docstrings.

## Controls

| Action     | Key               |
| ---------- | ----------------- |
| Move up    | Up arrow or `W`   |
| Move down  | Down arrow or `S` |
| Fire laser | Spacebar          |
| Quit       | `Q`               |

## Requirements

* Python 3.11 or later
* Pygame 2.6.1

Install all dependencies with:

```bash
python -m pip install -r requirements.txt
```

## Running the Game

From the project’s root directory, run:

```bash
python alien_invasion.py
```

## Project Structure

```text
AlienInvasion_amedina6_track_1/
├── Assets/
│   ├── images/
│   └── sound/
├── alien_invasion.py
├── arsenal.py
├── bullet.py
├── settings.py
├── ship.py
├── alien.py
├── alien_fleet.py
├── alien_invasion.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Development Roadmap
## Development Roadmap

### Final Submission

* Add a Play button and game states.
* Add score, high score, and remaining lives.
* Hide the mouse cursor while gameplay is active.
* Complete final testing and documentation.

### Milestone 2

* Create a fleet consistent with side-scrolling gameplay.
* Spawn aliens from the opposite side of the screen.
* Implement horizontal fleet movement.
* Add laser-and-alien collisions.
* Restart the game when an alien hits the ship or reaches the edge behind it.

### Final Submission

* Add a Play button and game states.
* Add score, high score, and remaining lives.
* Hide the mouse cursor while gameplay is active.
* Complete final testing and documentation.

## Starter-Code Attribution

This project began with the classroom Alien Invasion starter repository:

[RedBeard41/alien_Invasion_starter](https://github.com/RedBeard41/alien_Invasion_starter)

The base project was modified for the Track 1 custom game-mechanics requirements.
