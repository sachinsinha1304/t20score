import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))

teams = [
    'Australia',
    'India',
    'Bangladesh',
    'New Zealand',
    'South Africa',
    'England',
    'West Indies',
    'Afghanistan',
    'Pakistan',
    'Sri Lanka'
]

cities = [
     'Colombo',
     'Mirpur',
     'Johannesburg',
     'Dubai',
     'Auckland',
     'Cape Town',
     'London',
     'Pallekele',
     'Barbados',
     'Sydney',
     'Melbourne',
     'Durban',
     'St Lucia',
     'Wellington',
     'Hamilton',
     'Lauderhill',
     'Centurion',
     'Manchester',
     'Abu Dhabi',
     'Mumbai',
     'Nottingham',
     'Southampton',
     'Mount Maunganui',
     'Kolkata',
     'Lahore',
     'Chittagong',
     'Delhi',
     'Nagpur',
     'Cardiff',
     'Adelaide',
     'Bangalore',
     'St Kitts',
     'Christchurch',
     'Trinidad',
     'Brisbane',
     'Birmingham',
     'Hambantota',
     'Dhaka',
     'Lucknow']

st.title('T20 Score Predictor')

col1, col2 = st.columns(2)

with col1:
    bat_team = st.selectbox('Select Batting Team', sorted(teams))

with col2:
    bowl_team = st.selectbox('Select Bowling Team', sorted(teams))

city = st.selectbox('Select City', sorted(cities))

col3,col4,col5 = st.columns(3)

with col3:
    cur_score = st.number_input('Current Score')

with col4:
    overs = st.number_input('Over done (works for over 3 overs)')

with col5:
    wicket = st.number_input('Wickets Out')

last_three = st.number_input('Runs scored in last 3 overs')

if st.button('Predict'):
    ball_left = 120-(overs*6)
    wicket_left = 10 - wicket
    curr = cur_score/overs

    input_df = pd.DataFrame({'batting_team':[bat_team],'bowling_team':[bowl_team],'city':[city],'curr_score':[cur_score],'ball_left':[ball_left],'wicket_left':[wicket_left],'crr':[curr],'last_three':[last_three]})

    res = pipe.predict(input_df)
    st.write(f'The final Score is Predicted to be {int(res)}')
    # st.dataframe(input_df)
