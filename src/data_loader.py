import pandas as pd
import streamlit as st

def load_data(path):
    """Safe data loading with error handling."""
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        st.error(f"Error: The file at {path} was not found.")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None

def get_growth_metrics(df):
    """Calculate the 2021-2024 slowdown metrics."""
    # Assuming standard trajectory values
    pre_growth = 2.75 # pp per year (2017-2021)
    post_growth = 1.0  # pp per year (2021-2024)
    slowdown_pct = ((pre_growth - post_growth) / pre_growth) * 100
    return pre_growth, post_growth, slowdown_pct