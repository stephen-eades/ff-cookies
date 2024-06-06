from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Simulate data fetching
        # For example, make a request to an external API
        # response = requests.get('http://external-api-url')
        # data = response.json()

        # Placeholder data for example purposes
        data = {"key1": "value1", "key2": "value2"}
        
        # Check if data is valid (this is just a placeholder condition)
        if not data:
            return jsonify({'error': 'No data found'}), 404

        return jsonify(data), 200

    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
