# Tic-Tac-Toe Flask Application

A simple web-based tic-tac-toe game built with Flask.

## Features

- Interactive 3x3 tic-tac-toe board
- Two-player gameplay (X and O)
- Win detection for rows, columns, and diagonals
- Draw detection when board is full
- Game reset functionality
- Clean, responsive web interface

## Setup and Installation

### Prerequisites
- Python 3.7 or higher

### Installation

1. Clone or navigate to the project directory:
   ```bash
   cd /Users/kajin/git/demo-repo
   ```

2. The virtual environment is already set up. Activate it:
   ```bash
   source .venv/bin/activate
   ```

3. Install dependencies (Flask is already installed):
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. Make sure you're in the project directory and the virtual environment is activated
2. Run the Flask application:
   ```bash
   python app.py
   ```

3. Open your web browser and go to: `http://127.0.0.1:5000`

## How to Play

1. The game starts with Player X
2. Click on any empty cell to make your move
3. Players alternate turns automatically
4. The game ends when:
   - A player gets three in a row (horizontally, vertically, or diagonally)
   - The board is full (draw)
5. Click "New Game" to start over

## Project Structure

```
.
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Game interface template
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technical Details

- **Backend**: Flask web framework
- **Frontend**: HTML, CSS, JavaScript
- **Game Logic**: Python class-based implementation
- **Session Management**: Flask sessions for game state
- **API Endpoints**:
  - `GET /` - Main game page
  - `POST /move` - Make a move
  - `POST /reset` - Reset the game
  - `GET /status` - Get current game state
