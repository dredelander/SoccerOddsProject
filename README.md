# Soccer Odds Analysis : 2022 WorldCup and EPL

To run this application visit: https://dredelander-socceroddsproject-app-a1puse.streamlit.app/

To run this application locally you will need to follow the Streamlit directions for setting up a secrets variable flow.

    In the root of the project folder create a folder, name it: '.streamlit'. 
    In this folder create a file and name it a secrets.toml file.
    In this file you will need to add the variables listed below.
    
        ODDS_API_KEY_2 ="<your api key>"
        WC_ODDS_URL = "https://api.the-odds-api.com/v4/sports/soccer_fifa_world_cup/odds/?regions=uk&bookmakers=williamhill"
        EPL_ODDS_URL = "https://api.the-odds-api.com/v4/sports/soccer_epl/odds/?regions=uk&bookmakers=williamhill"
        FD_API_KEY = "<your api key>"
        EPL_TEAMS_URL = "http://api.football-data.org/v4/competitions/PL/teams"
        EPL_TOP_SCORERS_URL ="http://api.football-data.org/v4/competitions/PL/scorers"
        WC_STANDINGS_URL="https://api.football-data.org/v4/competitions/WC/standings"
        FD_EPL_STANDINGS_URL="https://api.football-data.org/v4/competitions/PL/standings"
        WC_TOP_SCORERS_URL ="http://api.football-data.org/v4/competitions/WC/scorers"

    ###For the API keys (see URL to request):
        ODDS_API_KEY_2 vist: https://api.the-odds-api.com/
        FD_API_KEY  visit: https://api.football-data.org/

## PURPOSE : 
To provide data driven insights into upcoming soccer games during the 2022 World Cup and '22-'23  English Premier League.

## STATEMENT OF WORK

Collect odds, statistics and informational data for each team and key players.

## FEATURE 1

API request for odds information & transformation of data for analysis

## FEATURE 2

Turn the data scripts into a shareable web application via opensource Streamlit app. 

## FEATURE 3

Combine, clean, and merge preview odds data from an api.

## FEATURE 4

Offer dataframe visualizations to aid in results insights.

