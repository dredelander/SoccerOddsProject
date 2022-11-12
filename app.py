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
main_animation = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_ky03n5aXvs.json')
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

    view_type = st.sidebar.multiselect('Select info option:', ('View Upcoming Games', 'View info by Country'))
    st.sidebar.markdown('---')

elif selected == 'English Premier League':

    st.sidebar.title('English Premier League')
    epl_team = st.sidebar.selectbox('Select a team for team:',(epl_teams_list))
    if epl_team and epl_team != 'Select your team':
        print(epl_team)
        st.image(get_team_logo(epl_team))

print('no problem')


if selected == 'English Premier League':
    st.subheader('Odds for Upcoming Games')
    st.write(epl_odds_df)
