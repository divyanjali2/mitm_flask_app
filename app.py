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
        # Call your MITM detection function
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
    """Health check endpoint for Render"""
    return jsonify({'status': 'healthy', 'message': 'MITM Detector is running'})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    # For production (Render)
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)