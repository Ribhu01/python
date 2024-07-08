# Snake Game

This is a simple Snake game implemented using Python's Turtle module. The game features a snake that moves around the screen, eating food to grow longer. The player controls the snake's movement using the arrow keys on the keyboard. The game ends if the snake collides with itself or with the screen boundaries.

## How to Play

1. Run the game by executing the `main.py` file.
2. Use the arrow keys (Up, Down, Left, Right) to control the snake's movement.
3. Eat the food (red circles) to grow longer and increase your score.
4. Avoid colliding with the snake's own body or the screen boundaries.

## Installation

To run the Snake game on your local machine, follow these steps:

1. Clone the repository:
2. Navigate to the project directory:
3. Run the game:

## Dependencies

This project uses the following Python modules:

- `turtle`: For creating the game graphics.
- `random`: For generating random positions for the food.

## File Structure

- `main.py`: The main Python script to run the game.
- `snake.py`: Python script containing the Snake class.
- `food.py`: Python script containing the Food class.
- `score.py`: Python script containing the Scoreboard class.

## Snake Class

The `snake.py` file contains the Snake class, responsible for controlling the snake's movement. Here's an overview of the methods in the Snake class:

- `__init__()`: Initializes the snake object and creates the snake's segments.
- `create_snake()`: Creates the initial segments of the snake.
- `add_head()`: Adds a new segment to the snake.
- `move()`: Moves the snake forward.
- `extends()`: Extends the length of the snake.
- Directional methods (`up()`, `down()`, `left()`, `right()`): Change the direction of the snake's movement based on user input.

## Food Class

The `food.py` file contains the Food class, responsible for managing the food items. Here's an overview of the methods in the Food class:

- `__init__()`: Initializes the food object.
- `respawn()`: Moves the food to a random position on the screen.

## Scoreboard Class

The `score.py` file contains the Scoreboard class, responsible for displaying and updating the score. Here's an overview of the methods in the Scoreboard class:

- `__init__()`: Initializes the scoreboard object.
- `u_scoreboard()`: Displays the current score.
- `increase_score()`: Increases the score by 10 points.
- `game_over()`: Displays "Game over" message when the game ends.

## Acknowledgments

This Snake game project was created for educational purposes and is inspired by classic arcade games. It serves as a fun way to learn Python programming concepts and game development.





