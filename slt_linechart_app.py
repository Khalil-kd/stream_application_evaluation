import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.write("Voici les données utilisées :")
st.write(chart_data)

st.line_chart(chart_data)
