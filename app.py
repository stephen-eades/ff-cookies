from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        response = requests.get('https://www.espn.com')
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
