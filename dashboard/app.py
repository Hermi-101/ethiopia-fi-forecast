import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page Config
st.set_page_config(page_title="Ethiopia Financial Inclusion Dashboard", layout="wide")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Trends Analysis", "Forecasts", "Inclusion Projections"])

# 1. OVERVIEW PAGE
if page == "Overview":
    st.title("Ethiopia's Digital Financial Transformation")
    
    # Summary Cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Account Ownership (2024)", "49%", "+3pp")
    col2.metric("Digital Payment Usage", "35%", "High Growth")
    col3.metric("P2P/ATM Crossover", "Reached", "2024 Milestone")
    
    st.markdown("""
    ### Key Insights
    - **Structural Plateau:** Growth slowed to +3pp in 2021-2024.
    - **Infrastructure Ceiling:** Inclusion is currently limited by a 44% electricity access rate.
    - **Mobile Money Gap:** Only 9.45% of adults have a dedicated mobile money account despite massive Telebirr/M-Pesa registration.
    """)

# 2. FORECASTS PAGE
elif page == "Forecasts":
    st.title("Forecasting Financial Inclusion (2025-2027)")
    
    # Scenario Selector
    scenario = st.selectbox("Select Scenario", ["Base", "Optimistic", "Pessimistic"])
    
    # Load your forecast data (Mock data based on your previous table)
    data = {
        "Year": [2025, 2026, 2027],
        "Forecast": [51.25, 53.50, 55.75] if scenario == "Base" else [54.0, 59.5, 64.0] if scenario == "Optimistic" else [49.5, 50.0, 50.5],
        "Lower_CI": [50.45, 51.90, 53.35],
        "Upper_CI": [52.05, 55.10, 58.15]
    }
    df = pd.DataFrame(data)
    
    # Plotly Forecast Chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Forecast'], mode='lines+markers', name='Forecast'))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Upper_CI'], mode='lines', line=dict(width=0), showlegend=False))
    fig.add_trace(go.Scatter(x=df['Year'], y=df['Lower_CI'], mode='lines', fill='tonexty', fillcolor='rgba(0,100,80,0.2)', name='95% Confidence Interval'))
    
    st.plotly_chart(fig, use_container_width=True)
    st.table(df)

# 3. INCLUSION PROJECTIONS
elif page == "Inclusion Projections":
    st.title("Progress Toward 60% Inclusion Target")
    progress = 49 # Current status
    target = 60
    st.progress(progress/target)
    st.write(f"Ethiopia is currently at {progress}%. To reach the {target}% target, the 'Optimistic' scenario must be achieved.")