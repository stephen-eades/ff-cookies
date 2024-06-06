from flask import Flask, jsonify, request
import requests
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/current', methods=['POST'])
def get_data():
    try:
        # Get the league id, swid, and espn_s2 values from the POST body
        data = request.get_json()
        league_id = data.get('leagueId')
        swid = data.get('swid')
        espn_s2 = data.get('espn_s2')

        # Check if all parameters are provided
        if league_id is None or swid is None or espn_s2 is None:
            return jsonify({'error': 'Missing one or more parameters'}), 400

        # Define variables for ESPN fantasy api request
        current_year = str(datetime.datetime.now().year)
        base_url = 'https://lm-api-reads.fantasy.espn.com/apis/v3/'
        current_season_endpoint = 'games/ffl/seasons/'+current_year+'/segments/0/leagues/'+league_id+'?view=mMatchupScore&view=mTeam&view=mSettings'
        
        # Make the request
        response = requests.get(url=base_url+current_season_endpoint, verify=False, cookies={'swid': swid, 'espn_s2': espn_s2})
        espn_data = response.json()
        
        # Check if data is valid (this is just a placeholder condition)
        if not espn_data:
            return jsonify({'error': 'No espn data found'}), 404

        return jsonify(espn_data), 200

    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500
    

@app.route('/historic', methods=['POST'])
def get_data():
    try:
        # Get the league id, swid, and espn_s2 values from the POST body
        data = request.get_json()
        league_id = data.get('leagueId')
        swid = data.get('swid')
        espn_s2 = data.get('espn_s2')

        # Check if all parameters are provided
        if league_id is None or swid is None or espn_s2 is None:
            return jsonify({'error': 'Missing one or more parameters'}), 400

        # Define variables for ESPN fantasy api request
        current_year = str(datetime.datetime.now().year)
        base_url = 'https://lm-api-reads.fantasy.espn.com/apis/v3/'
        historic_season_endpoint = 'games/ffl/leagueHistory/'+league_id+'?view=mLiveScoring&view=mMatchupScore&view=mRoster&view=mSettings&view=mStandings&view=mStatus&view=mTeam&view=modular&view=mNav&seasonId='
        
        # Make the request
        response = requests.get(url=base_url+historic_season_endpoint, verify=False, cookies={'swid': swid, 'espn_s2': espn_s2})
        espn_data = response.json()
        
        # Check if data is valid (this is just a placeholder condition)
        if not espn_data:
            return jsonify({'error': 'No espn data found'}), 404

        return jsonify(espn_data), 200

    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
