
# Missionaries and Cannibals Game

This repository contains a Pygame-based implementation of the classic Missionaries and Cannibals puzzle, along with an AI solver using the Breadth-First Search (BFS) algorithm.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Gameplay](#gameplay)
- [AI Solver](#ai-solver)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Missionaries and Cannibals puzzle is a well-known problem in artificial intelligence, where the objective is to transport a group of missionaries and cannibals across a river using a boat. The challenge is to ensure that cannibals never outnumber missionaries on either side of the river.

## Features
- Graphical user interface using Pygame.
- AI solver using the Breadth-First Search (BFS) algorithm.
- Animation of the solution found by the AI.
- Interactive game controls.
- Sound effects and background music.

## Requirements
- Python 3.6+
- Pygame

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/missionaries-and-cannibals.git
   cd missionaries-and-cannibals
   ```
2. Install the required Python packages:
```sh 
pip install pygame
```
3. Usage
To run the game, execute the main.py file:
```sh
python main.py
```

## project structure 
missionaries-and-cannibals/
├── images/
├── music/
├── Boat.py
├── Person.py
├── aisolver.py
├── main.py
└── README.md

## Gameplay
The game starts with 3 missionaries and 3 cannibals on the left side of the river.
The objective is to move all missionaries and cannibals to the right side using the boat.
Ensure that cannibals never outnumber missionaries on either side of the river.
Click on the missionaries or cannibals to load them onto the boat, then click the boat to move it across the river.
The game includes sound effects for winning and losing.

## AI Solver
The AI solver uses the Breadth-First Search (BFS) algorithm to find the optimal solution.
The solution path is animated in the game, demonstrating the steps taken to solve the puzzle.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
