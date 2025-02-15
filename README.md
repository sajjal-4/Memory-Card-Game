# Memory Card Game

This is a simple memory card game implemented in Python. The game presents a board of hidden cards. The player chooses two cards at a time, trying to find matching pairs. A time limit adds to the challenge.

## How to Play

1.  **Clone or Download:** Clone this repository to your local machine or download the ZIP file.
2.  **Install Python:** Make sure you have Python 3 installed on your system.
3.  **Run the Game:** Open a terminal or command prompt, navigate to the directory where you saved the files, and run the game using the command `python main.py` (if you name the python file as main.py).

4.  **Gameplay:**
    *   The game presents a board of hidden cards represented by `[*]`.
    *   You will be prompted to choose two cards by entering their indices (numbers between 0 and 15).
    *   If the cards match, they will remain revealed.
    *   If the cards do not match, they will be hidden again.
    *   You have a time limit to find all the matching pairs.
    *   The game ends when you find all pairs or when the time runs out.

## Files Included

*   `main.py`: The Python script containing the game logic.

## Functionality

The code implements the following features:

*   **Deck Creation:** The `create_deck()` function creates a deck of cards with matching pairs.
*   **Board Display:** The `display_board()` function displays the current state of the board, showing revealed cards and hiding the rest.
*   **Match Checking:** The `check_match()` function checks if two selected cards are a match.
*   **Game Logic:** The `play_game()` function handles the main game loop, user input, validation, match checking, and time limit.

## Customization

*   **Card Sets:** Modify the `create_deck()` function to use different card sets (e.g., numbers, symbols, images).
*   **Board Size:** Adjust the number of cards in the deck to change the board size.  Remember to adjust the time limit accordingly.
*   **Time Limit:** Change the `time_limit` variable in the `play_game()` function to adjust the difficulty.
*   **Difficulty Levels:** Implement different difficulty levels with varying time limits and board sizes.
*   **Graphical Interface:** Enhance the game by creating a graphical user interface (GUI) using libraries like Tkinter or PyQt.

## Technologies Used

*   Python

