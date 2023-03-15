import streamlit as st
import pandas as pd
import requests

# Page setup
st.set_page_config(page_title="BJJ Instructions Search Engine", page_icon="🦐", layout="wide")
st.title("BJJ Instructions Search Engine")

# Connect to the Google Sheet
sheet_id = "17AvwdOvpD7CaFVF9CKGWS6kJ4gNeqcfTV6ekZiGGqwU"
sheet_name = "list"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).fillna("")

# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search videos by title, instructor, game ply", value="")

# Filter the dataframe using masks
m1 = df["title"].str.contains(text_search, case=False)
m2 = df["instructor"].str.contains(text_search, case=False)
m3 = df["game"].str.contains(text_search, case=False)
m4 = df["type"].str.contains(text_search, case=False)
df_search = df[m1 | m2 | m3 | m4]

# Show the results, if you have a text_search
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.caption(f"{row['title'].strip()} - {row['game'].strip()}")
            st.markdown(f"**{row['title'].strip()}**")
            st.markdown(f"*{row['instructor'].strip()}*")
            st.markdown(f"*{row['game'].strip()}*")

