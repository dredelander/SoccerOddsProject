import streamlit as st
st.set_page_config(page_title='WC & EPL Portal', page_icon=':soccer', layout='wide')
from dotenv import load_dotenv
import os
load_dotenv()
from helpers import *

# TEST_VAR = os.getenv('TEST_VAR')
# ODDS_API_KEY = os.getenv('ODDS_API_KEY')
# WC_ODDS_URL= os.getenv('WC_ODDS_URL')

epl_odds_df = get_EPL_odds_data()

st.title('Hello' )
st.write(epl_odds_df)

print('no problem')