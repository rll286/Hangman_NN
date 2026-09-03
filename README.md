# Hangman NN

This project is a hand implemented neural network foundation attached to a lightweight
Hangman game. The main pourpose of this is to learn about the implementation and inner 
workings of neural networks and how to attach to a simple framework for training.

## Status

**Current version:** `0.1.0`

Repo initialization and starting on the game engine implementation.

## Goals

The primary goals of this project are:

- Build a working Hangman game with rigid rules
- Make large word selection for training 
- Implement training from random game states
- Implement neural network
- Attatch network to the training front end
- Allow players to play against network 

## Non-Goals

The project does not currently aim to:

- Make a general fraimwork for all neural network implementation

## Features

### Implemented

- Rules for loss, input, and valid word inputs

### Planned

- Game engine
- Game state object with only exposed data that a real player would know

## Requirements

- Python 3.12+

## Installation

Clone the repository:

```bash
git clone https://github.com/rll286/Hangman_NN.git
cd Hangman_NN