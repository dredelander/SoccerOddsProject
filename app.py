import streamlit as st
st.set_page_config(page_title='WC & EPL Portal', page_icon=':soccer', layout='wide')
from dotenv import load_dotenv
import requests
import os
load_dotenv()
from helpers import *
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

epl_odds_df , epl_teams_list = get_EPL_odds_data()
wc_odds_df, wc_team_list = get_WC_odds_data()

main_animation = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_bvxz04bd.json')
goal_animation = load_lottieurl('https://assets2.lottiefiles.com/private_files/lf30_2wjx4xzb.json')



### Header and NavBar

col1, col2, col3 ,col4,col5= st.columns(5)
with col1:
    st_lottie(main_animation, key="main_animation")
with col2:
    st.write('')
with col3:
    st.subheader('Football Odds, stats and more!' )
    st.markdown('<style>body {font-family: Arial, Helvetica, sans-serif;}</style>', unsafe_allow_html=True)
with col4:
    st.write('')
with col5:
    st_lottie(goal_animation, key='goal_animation')



selected = option_menu(
    menu_title = None,
    options = ['World Cup 2022', 'English Premier League'],
    icons = ['trophy', 'medal'],
    menu_icon = 'bars',
    default_index = 0,
    orientation = 'horizontal',
    
 )


### Sidebar Navigation

if selected == 'World Cup 2022':

    st.sidebar.title('World Cup 2022')
    wc_data= st.sidebar.radio(
        "Set EPL data to view 👉",
        key="world_cup",
        options=["Standings", "Top 10 Scorers", "Odds and Game Times", "See Previous Match Ups"],
        index=0,
        label_visibility='hidden'
    )
    if wc_data == 'See Previous Match Ups':
        home_team = st.sidebar.selectbox('Home Team:',(wc_team_list))
        away_team = st.sidebar.selectbox('Away Team:',(wc_team_list))
        if home_team and home_team != 'Select your team' and away_team and away_team != 'Select your team':
            if home_team == away_team:
                st.write('Please select diferent teams')
            else:
                try:
                    hist_df, tt_wins, tt_loss, ties, games,num_home_games, num_away_games = get_past_results(home_team, away_team)

                    if len(hist_df) > 0:
                        col1, col2,col3 = st.columns(3)
                        with col1:
                            st.write('')
                            st.title(str(games) + ' games played')
                            
                        with col2:
                            
                            st.write('')
                            st.subheader(str(tt_wins) + ' home wins for '  +home_team+ ' in ' + str(num_home_games)+' games.')
                            st.subheader(str(tt_loss) + ' home losses for '  +home_team + ' in ' + str(num_away_games)+' games.')
                            st.subheader(str(ties) + ' ties in total.')
                            
                        with col3:
                            image_wc_home = get_team_logo(home_team.replace('and','&'),'wc')
                            if image_wc_home != 'Logo/Flag is not Available':
                                st.image(image_wc_home) 
                            st.subheader(home_team)
                            st.write('')
                            image_wc = get_team_logo(away_team.replace('and','&'),'wc')
                            if image_wc != 'Logo/Flag is not Available':
                                st.image(image_wc) 
                            st.subheader(away_team)

                        st.write(hist_df)
                    else:
                        'No data available for this match up'
                except ValueError:
                    st.write('No data available for this match up')

elif selected == 'English Premier League':

    st.sidebar.title('English Premier League')
    epl_data= st.sidebar.radio(
        "Set EPL data to view 👉",
        key="epl",
        options=["Standings", "Top 10 Scorers", "Odds and Game Times", "FIFA 2023 Team Info"],
        index=0,
        label_visibility='hidden'
    )
    if epl_data == 'FIFA 2023 Team Info':
        epl_team = st.sidebar.selectbox('Select a team FIFA 23 Stats:',(epl_teams_list))
        if epl_team and epl_team != 'Select your team':

            col1, col2 = st.columns(2)
            with col1:
                image_epl = get_team_logo(epl_team.replace('and','&'),'club')
                if image_epl != 'Logo/Flag is not Available':
                    st.image(image_epl)  
            with col2:
                st.subheader(epl_team)
            epl_top_player, epl_avg_overall,epl_top_3_int_players, epl_top16_value = get_team_fifa_info(epl_team.replace('and','&'))
            st.subheader('Top player')
            epl_top_player
            st.write('')
            st.subheader('Value of top 16 players')
            epl_top16_value
            st.write('')
            st.subheader('Overall rating of top 16 players')
            epl_avg_overall
            st.write('')
            st.subheader('Top 3 international players')
            epl_top_3_int_players


if selected == 'English Premier League':
    col1,col2,col3 = st.columns(3)
    with col1:
        st.write('')
    with col2:
        st.subheader('2022-2023 Season')
    with col3:
        st.write('')
    
    if epl_data == 'Odds and Game Times':
        st.write(epl_odds_df)
    if epl_data == 'Top 10 Scorers':
        epl_top_scorers = get_epl_top_scorers_df()
        st.write(epl_top_scorers)
    if epl_data == 'Standings':
        
        epl_standings = get_epl_standings_df()
        st.write(epl_standings)

if selected == 'World Cup 2022':
    col1,col2,col3 = st.columns(3)
    st.write('')
    with col1:
        st.write('')
    with col2:
        st.write('')
        if wc_data != 'FIFA 2023 Team Info':
            st.image("https://www.kindpng.com/picc/m/185-1859678_fifa-world-cup-qatar-2022-logo-hd-png.png")
        else:
            st.write('')
    with col3:
        st.write('')
    
    if wc_data == 'Odds and Game Times':
        st.write(wc_odds_df)
    if wc_data == 'Top 10 Scorers':
        wc_top_scorers = get_wc_top_scores()
        if len(wc_top_scorers) >5:
            st.write(wc_top_scorers)
        else: 
            st.write('No goal scorers in tournament yet')
    if wc_data == 'Standings':
        
        wc_standings = get_wc_standings_df()
        st.write(wc_standings)