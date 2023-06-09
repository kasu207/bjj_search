import streamlit as st
import pandas as pd
import requests
import streamlit.components.v1 as components


# Page setup
st.set_page_config(page_title="BJJ Instructions Search Engine", page_icon="🦐", layout="wide")


# Styling
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Connect to the Google Sheet
@st.cache_data(ttl=600)
def load_data(sheets_url):
    return pd.read_csv(sheets_url, dtype=str).fillna("")

df = load_data(st.secrets["gsheetsurl"])

#Content Design
st.title("BJJ Anleitung Search Engine")


# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Suche nach Videos nach Title, Instructor, Gameplay", value="")

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
            st.image(f"{row['thumbnail']}")
            st.markdown(f"**Instructor:** *{row['instructor'].strip()}*")
            st.markdown(f"**Game:** *{row['game'].strip()}*")
            st.markdown(f"**Start Position:** *{row['start position'].strip()}*")
            st.markdown(f"**Type:** *{row['type'].strip()}*")
            st.markdown(f"*{row['source'].strip()}*")
            st.markdown(f"*{row['contributor'].strip()}*")
            st.write('hier die andere Karte')
            
else:
    if st.checkbox('Zeige mir alle Anleitungen'):
        for n_row, row in df.reset_index().iterrows():
            i = n_row%N_cards_per_row
            if i==0:
                st.write("---")
                cols = st.columns(N_cards_per_row, gap="large")
            # draw the card
            with cols[n_row%N_cards_per_row]:
                st.caption(f"{row['title'].strip()} - {row['game'].strip()}")
                st.markdown(f"**{row['title'].strip()}**")
                st.image(f"{row['thumbnail']}")
                st.markdown(f"**Instructor:** *{row['instructor'].strip()}*")
                st.markdown(f"**Game:** *{row['game'].strip()}*")
                st.markdown(f"**Start Position:** *{row['start position'].strip()}*")
                st.markdown(f"**Type:** *{row['type'].strip()}*")
                st.markdown(f"*{row['source'].strip()}*")
                st.markdown(f"*{row['contributor'].strip()}*")


