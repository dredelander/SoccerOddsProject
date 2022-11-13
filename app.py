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
main_animation = load_lottieurl('https://assets2.lottiefiles.com/packages/lf20_bvxz04bd.json')
goal_animation = load_lottieurl('https://assets2.lottiefiles.com/private_files/lf30_2wjx4xzb.json')

epl_top_scorers = get_epl_top_scorers_df()
epl_standings = get_epl_standings_df()


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
        key="visibility",
        options=["Standings", "Top 10 Scorers", "Odds and Game Times", "Fifa 2022 Team Info"],
        index=0,
        label_visibility='hidden'
    )

elif selected == 'English Premier League':

    st.sidebar.title('English Premier League')
    epl_data= st.sidebar.radio(
        "Set EPL data to view 👉",
        key="visibility",
        options=["Standings", "Top 10 Scorers", "Odds and Game Times", "Fifa 2022 Team Info"],
        index=0,
        label_visibility='hidden'
    )
    if epl_data == 'Fifa 2022 Team Info':
        epl_team = st.sidebar.selectbox('Select a team FIFA 22 Stats:',(epl_teams_list))
        if epl_team and epl_team != 'Select your team':
            print(epl_team)
            st.image(get_team_logo(epl_team))
    


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
        st.write(epl_top_scorers)
    if epl_data == 'Standings':
        st.write(epl_standings)
