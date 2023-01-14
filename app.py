import pandas as pd
import streamlit as st
import datetime


import pickle


path = "./match_batsman_details_male.xlsx - Sheet1.csv"

batsman_col = ["date" ,"name"  , 
 "team"   , "opposition" , "venue" ,  
"innings_played" , "previous_average" ,   
 "previous_strike_rate"  , "previous_centuries"  ,
  "previous_fifties"  ,  "previous_zeros" , "runs"  ]

@st.cache
def get_data(path):
    return pd.read_csv(path)

df = get_data(path)
df = df[batsman_col]

team = df['team'].drop_duplicates()
team_choice = st.sidebar.selectbox('Select your team:', team)
df = df.loc[df["team"] == team_choice]


opposition = df['opposition'].drop_duplicates()
opposition_choice = st.sidebar.selectbox('Select your team:', opposition)
df = df.loc[df["opposition"] == opposition_choice]

st.write("""
# match_batsman_details_2022
""")





st.dataframe(df.head())


run = df.groupby(['name','team','opposition']).runs.agg(['count','sum', 'mean'])

st.dataframe(run)


