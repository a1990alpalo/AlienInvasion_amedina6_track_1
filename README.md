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
├── requirements.txt
├── .gitignore
└── README.md
```

## Milestone Evidence

A screenshot or short demonstration video will show the ship positioned on the left side, moving vertically, and firing lasers horizontally toward the right edge.

## Development Roadmap

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
