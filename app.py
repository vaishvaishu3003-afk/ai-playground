import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")

data = pd.DataFrame(
    np.random.randn(10, 2),
    columns=["A", "B"]
)

st.write(data)

