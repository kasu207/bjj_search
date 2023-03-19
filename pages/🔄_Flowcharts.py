import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open('bjj_flowchart.png')


st.image(image, 'BJJ Flowchart', use_column_width='auto')