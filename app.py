from flask import Flask, render_template, request, jsonify
from utils.detector import start_detection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    result = start_detection()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
