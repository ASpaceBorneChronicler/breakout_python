# Pygame Breakout Game

## Overview
A classic Breakout-style arcade game implemented in Python using Pygame. Players control a paddle to bounce a ball and destroy bricks across multiple levels.

## Features
- Multiple levels with unique brick layouts
- Customizable brick health and colors
- Dynamic ball physics
- Paddle movement with responsive controls
- Countdown timer before each level start
- Pause functionality

## Prerequisites
- Python 3.x
- Pygame library
- Images for paddle and ball (in `img/` directory)

## Installation
1. Clone the repository
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Ensure `img/paddle.png` and `img/ball.png` exist in project directory

## Controls
- Left Arrow: Move paddle left
- Right Arrow: Move paddle right
- Space: Start game/Pause game
- Escape: Quit game

## Gameplay
- Destroy all bricks to advance to next level
- 3 levels with increasing complexity
- Ball bounces off paddle and changes trajectory based on hit location
- Game continues until all levels are completed

## Customization
Modify `Level` class to:
- Add more levels
- Change brick layouts
- Adjust brick colors and health

## License
Open-source. Feel free to modify and distribute.
