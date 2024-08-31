# Hangman-Game

# Hangman Game with Floral Theme

## Overview

This project is a Python-based implementation of the classic **Hangman Game**, featuring a unique floral theme. Players are challenged to guess letters of a hidden word related to flowers. The game provides visual feedback as incorrect guesses are made, bringing the hangman closer to completion.

## Features

- **Floral Vocabulary:** Hidden words are names of various flowers, adding a thematic twist.
- **Visual Hangman Display:** As players make incorrect guesses, a hangman figure is progressively drawn.
- **Interactive Gameplay:** Players receive feedback on each guess and can see the partially revealed word.

## Code Description

- **`hangman_game.py`**: Contains the main game logic and user interface.
  - **`flowers`**: A list of flower names used as potential hidden words.
  - **`hangman_display(attempt)`**: Function that returns the visual representation of the hangman based on the number of remaining attempts.
  - **Game Loop**: Manages user input, updates game state, and provides feedback.

## Usage

1. Start the game by running the Python script.
2. Guess letters to reveal the hidden flower name.
3. Incorrect guesses will draw the hangman figure, and you have a limited number of attempts.
4. The game ends when you either guess the word correctly or run out of attempts.
