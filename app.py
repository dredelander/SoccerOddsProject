import streamlit as st
from dotenv import load_dotenv
import os
load_dotenv()
from helpers import get_odds_data

TEST_VAR = os.getenv('TEST_VAR')
ODDS_API_KEY = os.getenv('ODDS_API_KEY')
WC_ODDS_URL= os.getenv('WC_ODDS_URL')


st.title('Hello' )

print('no problem')