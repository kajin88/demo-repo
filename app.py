from flask import Flask, render_template, request, jsonify, session
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# Game state storage (in production, use a database)
games = {}

class TicTacToe:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False
        
    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.game_over:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
                self.game_over = True
            elif self.is_board_full():
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        
        return False
    
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True
    
    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
        self.game_over = False

@app.route('/')
def index():
    if 'game_id' not in session:
        session['game_id'] = str(uuid.uuid4())
        games[session['game_id']] = TicTacToe()
    return render_template('index.html')

@app.route('/move', methods=['POST'])
def make_move():
    game_id = session.get('game_id')
    if not game_id or game_id not in games:
        return jsonify({'error': 'Game not found'}), 400
    
    data = request.get_json()
    row = data.get('row')
    col = data.get('col')
    
    if row is None or col is None:
        return jsonify({'error': 'Invalid move'}), 400
    
    game = games[game_id]
    if game.make_move(row, col):
        return jsonify({
            'board': game.board,
            'current_player': game.current_player,
            'winner': game.winner,
            'game_over': game.game_over
        })
    else:
        return jsonify({'error': 'Invalid move'}), 400

@app.route('/reset', methods=['POST'])
def reset_game():
    game_id = session.get('game_id')
    if not game_id or game_id not in games:
        return jsonify({'error': 'Game not found'}), 400
    
    games[game_id].reset()
    return jsonify({
        'board': games[game_id].board,
        'current_player': games[game_id].current_player,
        'winner': games[game_id].winner,
        'game_over': games[game_id].game_over
    })

@app.route('/status')
def get_status():
    game_id = session.get('game_id')
    if not game_id or game_id not in games:
        return jsonify({'error': 'Game not found'}), 400
    
    game = games[game_id]
    return jsonify({
        'board': game.board,
        'current_player': game.current_player,
        'winner': game.winner,
        'game_over': game.game_over
    })

if __name__ == '__main__':
    app.run(debug=True)
