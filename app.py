from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('game.json', 'r') as file:
    data = json.load(file)

def search_game(query, category, games):
    results = []
    for game in games:
        if query.lower() in game[category].lower():
            results.append(game)
    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        category = request.form['category']
        results = search_game(query, category, data)
        return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
