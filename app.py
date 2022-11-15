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
        options=["Standings", "Top 10 Scorers", "Odds and Game Times", "FIFA 2023 Team Info"],
        index=0,
        label_visibility='hidden'
    )
    if wc_data == 'FIFA 2023 Team Info':
        wc_team = st.sidebar.selectbox('Select a team FIFA 23 Stats:',(wc_team_list))
        if wc_team and wc_team != 'Select your team':
            col1, col2 = st.columns(2)
            with col1:
                image_wc = get_team_logo(wc_team.replace('and','&'),'wc')
                if image_wc != 'Logo/Flag is not Available':
                    st.image(image_wc) 
                
            with col2:
                st.subheader(wc_team)

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
    # if epl_data == 'Top 10 Scorers':
        # epl_top_scorers = get_epl_top_scorers_df()
        # st.write(epl_top_scorers)
    if wc_data == 'Standings':
        
        wc_standings = get_wc_standings_df()
        st.write(wc_standings)