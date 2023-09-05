# Snake-Game
Welcome to the Snake Arcade game! This classic game allows you to control a snake, collect food, and increase your score. Dive into the world of Snake and see how long you can grow your serpent!

## Project Screenshots
![image](https://github.com/sarvesh-2109/Snake-Game/assets/113255836/48f3c0c5-350b-4795-88d3-2b96335c6c8a)
![image](https://github.com/sarvesh-2109/Snake-Game/assets/113255836/3506a212-173b-4262-a4f8-b6fb880422ff)



## Game Overview

In this Snake Arcade game, you control a snake represented by a series of white squares on a black background. The goal is to collect the red food items to grow the snake and increase your score. However, be careful not to run into the walls or collide with the snake's own body!

## Object-Oriented Concepts

This game is a great example of object-oriented programming (OOP) in Python. Here are some of the key OOP concepts used in this project:

- **Classes and Objects:** The game is organized into classes like `Snake`, `Food`, and `ScoreBoard`, each representing a different aspect of the game.

- **Constructor (`__init__`):** Objects are initialized using the `__init__` method, which sets up their initial state and properties.

- **Method Overriding:** The `Food` class overrides the `refresh` method to generate random food positions.

- **Composition:** Multiple instances of classes are composed together to create the complete game.

- **Attributes:** Each object has attributes (e.g., `score`, `color`) that store information about them.

- **Methods:** Methods (e.g., `move`, `up`, `down`) define the behaviors and actions of the objects.

  ## File Descriptions

- `main.py`: This script is the main entry point for the Snake Arcade game. It sets up the game window, initializes the snake, food, and scoreboard, and controls the game loop.

- `scoreboard.py`: This file contains the `ScoreBoard` class, responsible for managing and displaying the player's score and game over messages.

- `snake.py`: This file contains the `Snake` class, which defines the behavior and properties of the snake. It includes methods for movement and handling collisions.

- `food.py`: This file contains the `Food` class, which represents the food items the snake must collect. It includes methods to generate and refresh food positions.


## How to Play

1. Clone this repository to your local machine.
2. Run the `main.py` script in a Python environment.
3. Control the snake using the arrow keys: Up, Down, Left, Right.
4. Collect red food items to increase your score.
5. Avoid running into the walls or colliding with the snake's body.

## Contributions

Contributions to this project are welcome! If you have ideas for improvements or new features, feel free to fork this repository and submit a pull request. Let's make the Snake Arcade game even better together!

## Acknowledgements

This project was inspired by the "100 Days of Code: The Complete Python Pro Bootcamp for 2023" on Udemy. Special thanks to the course instructors and contributors for their valuable insights.
