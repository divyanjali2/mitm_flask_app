import os
from flask import Flask, render_template, jsonify, request
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
            'message': 'Monitoring started successfully',
            'result': result
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error starting monitoring: {str(e)}'
        }), 500

@app.route('/stop_monitoring', methods=['POST'])
def stop_monitoring():
    try:
        return jsonify({
            'status': 'success',
            'message': 'Monitoring stopped successfully'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Error stopping monitoring: {str(e)}'
        }), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'message': 'MITM Detector is running'})

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Only run locally with Flask development server
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
