import requests
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


API_KEY = st.secrets["ODDS_API_KEY"]
EPL_ODDS_URL =st.secrets["EPL_ODDS_URL"]
WC_ODDS_URL = st.secrets["WC_ODDS_URL"]


players_df = pd.read_csv('./data/players_22.csv')

def get_EPL_odds_data():
    '''
        With a valid API key, this function retrieves the any live games as well as the next 8 upcoming games across 
        the English Premier League. (Soccer ;)
    '''
    sports_response = requests.get(
        EPL_ODDS_URL, 
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

        # list_teams = [team for team in odds_df['home_team']] + [team for team in odds_df['away_team']]
        team_list = []
        team_list.append('Select your team')
        for team in list(odds_df['home_team']):
            if team not in team_list:
                team_list.append(team)
        for team in list(odds_df['away_team']):
            if team not in team_list:
                team_list.append(team)
        
        return odds_df, team_list


def get_team_logo(team_name):
    team_logo = players_df.loc[players_df['club_name'].str.contains(team_name)== True].head(1)['club_logo_url'].values[0]
    return team_logo

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()