import requests
import os
import pandas as pd


API_KEY = os.getenv('ODDS_API_KEY')

def get_odds_data():
    '''
        With a valid API key, this function retrieves the any live games as well as the next 8 upcoming games across 
        the English Premier League. (Soccer ;)
    '''
    sports_response = requests.get(
        'https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?regions=uk&bookmakers=williamhill', 
        params={
            'api_key': API_KEY,        
        }
    )

    if sports_response.status_code != 200:
        return {'message':f'Failed to get sports data: status_code {sports_response.status_code}, response body {sports_response.text}'}

    else:
        all_odds = sports_response.json()
        prem_odds =[]

        for value in all_odds:

            prem_odds.append({'home_team': value['home_team'],
                'away_team': value['away_team'],
                'match_start':value['commence_time'],
                'win_home_team': value['bookmakers'][0]['markets'][0]['outcomes'][0]['price'],
                'win_away_team':value['bookmakers'][0]['markets'][0]['outcomes'][1]['price'],
                'tie':value['bookmakers'][0]['markets'][0]['outcomes'][2]['price'],
            })
            
        odds_df = pd.DataFrame(prem_odds)

        odds_df['match_start'] = pd.to_datetime(odds_df['match_start'])
        odds_df['match_start'] = odds_df['match_start'].dt.tz_convert('EST')

        return odds_df

