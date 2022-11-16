import requests
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
load_dotenv()


API_KEY = st.secrets["ODDS_API_KEY"]
EPL_ODDS_URL =st.secrets["EPL_ODDS_URL"]
WC_ODDS_URL = st.secrets["WC_ODDS_URL"]
FD_API_KEY = st.secrets["FD_API_KEY"]
EPL_TEAMS_URL = st.secrets["EPL_TEAMS_URL"]
EPL_TOP_SCORERS_URL = st.secrets["EPL_TOP_SCORERS_URL"]
FD_EPL_STANDINGS_URL= st.secrets["FD_EPL_STANDINGS_URL"]
WC_STANDINGS_URL = st.secrets["WC_STANDINGS_URL"]
WC_TOP_SCORERS_URL = st.secrets["WC_TOP_SCORERS_URL"]


players_df = pd.read_csv('./data/players_short_csv.csv')
sec_players_df = pd.read_csv('./data/players_fifa23.csv')
players_short_df = sec_players_df[['FullName', 'Club','BestPosition','Overall','ValueEUR','Age','IntReputation','NationalTeam']]
fifa_df= pd.read_csv('./data/fifa_results.csv')

def get_WC_odds_data():
    '''
        With a valid API key, this function retrieves the any live games as well as the next 8 upcoming games across 
        the English Premier League. (Soccer ;)
    '''
    sports_response = requests.get(
        WC_ODDS_URL, 
        params={
            'api_key': API_KEY,        
        }
    )

    if sports_response.status_code != 200:
        return {'message':f'Failed to get sports data: status_code {sports_response.status_code}, response body {sports_response.text}'}

    else:
        all_odds = sports_response.json()
        wc_odds =[]

        for value in all_odds:

            wc_odds.append({'home_team': value['home_team'],
                'away_team': value['away_team'],
                'match_start':value['commence_time'],
                'win_home_team': value['bookmakers'][0]['markets'][0]['outcomes'][0]['price'],
                'win_away_team':value['bookmakers'][0]['markets'][0]['outcomes'][1]['price'],
                'tie':value['bookmakers'][0]['markets'][0]['outcomes'][2]['price'],
            })
            
        odds_df = pd.DataFrame(wc_odds)

        odds_df['match_start'] = pd.to_datetime(odds_df['match_start'])
        odds_df['match_start'] = odds_df['match_start'].dt.tz_convert('EST')
        odds_df.rename(columns={"home_team":"Home Team", "away_team":"Away Team","match_start": "Game Time","win_home_team":"Home Team Win",
                "win_away_team":"Away Team Win","tie":"Tie"}, inplace=True)

        team_list = []
        team_list.append('Select your team')
        for team in list(odds_df['Home Team']):
            if team not in team_list:
                team_list.append(team)
        for team in list(odds_df['Away Team']):
            if team not in team_list:
                team_list.append(team)        
        return odds_df, team_list

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
        odds_df.rename(columns={"home_team":"Home Team", "away_team":"Away Team","match_start": "Game Time","win_home_team":"Home Team Win",
                "win_away_team":"Away Team Win","tie":"Tie"}, inplace=True)

        # list_teams = [team for team in odds_df['home_team']] + [team for team in odds_df['away_team']]
        team_list = []
        team_list.append('Select your team')
        for team in list(odds_df['Home Team']):
            if team not in team_list:
                team_list.append(team)
        for team in list(odds_df['Away Team']):
            if team not in team_list:
                team_list.append(team)
        
        return odds_df, team_list


def get_team_logo(team_name, type):
    if type =='club':
        team_logo = players_df.loc[players_df['club_name'].str.contains(team_name)== True]
        if len(team_logo)> 0:
            team_logo = team_logo.head(1)['club_logo_url'].values[0]
            return team_logo
        else:
            return 'Logo/Flag is not Available'
        
    else:
        team_logo = players_df.loc[players_df['nationality_name'].str.contains(team_name)== True]
        if len(team_logo)>0:
            team_logo = team_logo.head(1)['nation_flag_url'].values[0]
            return team_logo
            
        else:
            return 'Logo/Flag is not Available'

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def get_football_data(url_link, api_key):
    sports_response = requests.get(
            url_link, 
            headers={
                'X-Auth-Token': api_key,        
            }
        )
    if sports_response.status_code != 200:
            return({'message':f'Failed to get sports data: status_code {sports_response.status_code}, response body {sports_response.text}'})

    else:
            all_odds = sports_response.json()
            return(all_odds)

def get_epl_top_scorers_df():
    top_epl_scorers = get_football_data(EPL_TOP_SCORERS_URL, FD_API_KEY)
    players_top_ten=[]
    teams_tops_scorers =[]
    number_goals =[]
    number_assists=[]
    for player in top_epl_scorers['scorers']:
        players_top_ten.append((player['player']['name']))
        teams_tops_scorers.append((player['team']['name']))
        number_goals.append(player['goals'])
        number_assists.append(player['assists'])
    dic_top_epl_scorers = {'Player Name': players_top_ten,'Team': teams_tops_scorers,'Goals':number_goals,'Assists':number_assists}
    top_epl_scorers_df = pd.DataFrame(dic_top_epl_scorers)
    top_epl_scorers_df.set_index('Player Name')
    return top_epl_scorers_df

def get_wc_top_scores():
    top_wc_scorers = get_football_data(WC_TOP_SCORERS_URL, FD_API_KEY)
    players_top_ten=[]
    teams_tops_scorers =[]
    number_goals =[]
    number_assists=[]
    for player in top_wc_scorers['scorers']:
        print(player['assists'])
        players_top_ten.append((player['player']['name']))
        teams_tops_scorers.append((player['team']['name']))
        number_goals.append(player['goals'])
        number_assists.append(player['assists'])
    dic_top_wc_scorers = {'Player Name': players_top_ten,'Team': teams_tops_scorers, 'Goals':number_goals,'Assists':number_assists}
    top_wc_scorers_df = pd.DataFrame(dic_top_wc_scorers)
    top_wc_scorers_df.set_index('Player Name')

    return top_wc_scorers_df

def get_epl_standings_df():
    epl_standings = get_football_data(FD_EPL_STANDINGS_URL, FD_API_KEY)
    team_names =[]
    team_points=[]
    team_played_count =[]
    team_form =[]
    team_goal_dif =[]
    for position in epl_standings['standings'][0]['table']:
        team_names.append(position['team']['name'])
        team_played_count.append(position['playedGames'])
        team_points.append(position['points'])
        team_form.append(position['form'])
        team_goal_dif.append(position['goalDifference'])
    dic_epl_table ={'Team':team_names,'Points':team_points,'Games Played':team_played_count,'Form':team_form, 'Goal Difference':team_goal_dif}
    epl_table_df = pd.DataFrame(dic_epl_table)
    return epl_table_df

def get_team_df(name):
    team_df =players_short_df.loc[players_short_df['Club'].str.contains(name)== True]
    return team_df

def get_team_fifa_info(team):
    team_df = get_team_df(team)
    top_player = team_df.sort_values(by='Overall', ascending =False).head(1)
    avg_overall = round(team_df.head(16)['Overall'].mean(),2)
    top_3_int_players = team_df.sort_values(by='IntReputation', ascending =False).head(3)
    top16_value = "${:,.2f}".format(round(team_df.sort_values(by='ValueEUR', ascending =False).head(16)['ValueEUR'].sum(),2))

    return top_player, avg_overall,top_3_int_players, top16_value

def get_wc_standings_df():
    wc_standings = get_football_data(WC_STANDINGS_URL, FD_API_KEY)
    team_names =[]
    team_points=[]
    team_played_count =[]
    team_form =[]
    team_goal_dif =[]
    for position in wc_standings['standings']:
        # print(position)
        for table in position['table']:
            # print(table)

            team_names.append(table['team']['name'])
            team_played_count.append(table['playedGames'])
            team_points.append(table['points'])
            team_form.append(table['form'])
            team_goal_dif.append(table['goalDifference'])
            # print(team_names)
    dic_wc_table ={'Team':team_names,'Points':team_points,'Games Played':team_played_count,'Form':team_form, 'Goal Difference':team_goal_dif}
    wc_table_df = pd.DataFrame(dic_wc_table)
    return wc_table_df

def get_past_results(team1,team2):
    df = fifa_df.loc[((fifa_df['home_team'].str.contains(team1)== True )& (fifa_df['away_team'].str.contains(team2)== True)) | ((fifa_df['away_team'].str.contains(team1)== True )& (fifa_df['home_team'].str.contains(team2)== True))]
    team_1_home_wins = fifa_df.loc[((fifa_df['home_team'].str.contains(team1)== True )& (fifa_df['away_team'].str.contains(team2)== True)) & (fifa_df['home_score'] > fifa_df['away_score'])]
    team_1_away_wins = fifa_df.loc[((fifa_df['away_team'].str.contains(team1)== True )& (fifa_df['home_team'].str.contains(team2)== True)) & (fifa_df['home_score'] < fifa_df['away_score'])]
    ties = fifa_df.loc[(((fifa_df['home_team'].str.contains(team1)== True )& (fifa_df['away_team'].str.contains(team2)== True)) | ((fifa_df['away_team'].str.contains(team1)== True )& (fifa_df['home_team'].str.contains(team2)== True)))& (fifa_df['home_score'] == fifa_df['away_score'])]
    num_ties = len(ties)
    tt_wins_team1 = len(team_1_away_wins) + len(team_1_home_wins)
    tt_loss_team1 = len(df) - tt_wins_team1 - num_ties
    num_games=len(df)
    num_home_games = len(df.loc[df['home_team']== team1])
    num_away_games = len(df.loc[df['away_team']== team1])
    if len(df) >0:
        df = df.sort_values('date', ascending =False)
        df.set_index('date', inplace=True)
        return df, tt_wins_team1, tt_loss_team1 , num_ties, num_games, num_home_games, num_away_games
    else:
        return 'Not historical match history available'