import os
from flask import Flask, render_template, jsonify
from utils.detector import detect_mitm

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_monitoring', methods=['POST'])
def start_monitoring():
    try:
        result = detect_mitm()
        return jsonify({
            'status': 'success',
            'message': 'Monitoring started',
            'result': result
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    # For local development
    app.run(debug=True)
else:
    # For production (Azure)
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)