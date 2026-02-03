"""
Ethiopia Financial Inclusion Dashboard
Selam Analytics - Forecasting Financial Inclusion

This Streamlit dashboard enables stakeholders to explore data, 
understand event impacts, and view forecasts for Ethiopia's 
financial inclusion indicators.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import os

# Page configuration
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Dashboard",
    page_icon="🇪🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A5F;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Data loading functions
@st.cache_data
def load_data():
    """Load all required datasets"""
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load main enriched data
    main_data = pd.read_csv(os.path.join(base_path, 'data/processed/ethiopia_fi_unified_data_enriched.csv'))
    
    # Load forecast data
    forecast_data = pd.read_csv(os.path.join(base_path, 'data/processed/forecast_2025_2027.csv'))
    
    # Load impact matrix
    impact_matrix = pd.read_csv(os.path.join(base_path, 'data/processed/event_indicator_matrix_refined.csv'))
    
    return main_data, forecast_data, impact_matrix

@st.cache_data
def process_observations(main_data):
    """Extract and process observations"""
    obs = main_data[main_data['record_type'] == 'observation'].copy()
    obs['year'] = pd.to_datetime(obs['observation_date'], format='mixed', errors='coerce').dt.year
    return obs

@st.cache_data  
def process_events(main_data):
    """Extract and process events"""
    events = main_data[main_data['record_type'] == 'event'].copy()
    events['year'] = pd.to_datetime(events['observation_date'], format='mixed', errors='coerce').dt.year
    return events

# Load data
try:
    main_data, forecast_data, impact_matrix = load_data()
    observations = process_observations(main_data)
    events = process_events(main_data)
    data_loaded = True
except Exception as e:
    st.error(f"Error loading data: {e}")
    data_loaded = False

# Sidebar navigation
st.sidebar.image("https://img.icons8.com/color/96/000000/ethiopia.png", width=80)
st.sidebar.title("🇪🇹 Ethiopia FI Dashboard")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate to:",
    ["📊 Overview", "📈 Trends", "🔮 Forecasts", "🎯 Inclusion Projections"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### About")
st.sidebar.info(
    "This dashboard presents financial inclusion forecasts for Ethiopia, "
    "analyzing the impact of mobile money, digital ID, and infrastructure "
    "investments on ACCESS and USAGE indicators."
)
st.sidebar.markdown("---")
st.sidebar.markdown("*Selam Analytics*")
st.sidebar.markdown("*February 2026*")

# ============================================================================
# PAGE 1: OVERVIEW
# ============================================================================
if page == "📊 Overview":
    st.markdown('<h1 class="main-header">📊 Ethiopia Financial Inclusion Overview</h1>', unsafe_allow_html=True)
    
    if data_loaded:
        # Key Metrics Row
        st.subheader("Key Metrics (2024)")
        
        col1, col2, col3, col4 = st.columns(4)
        
        # Account Ownership
        acc_ownership = observations[
            (observations['indicator_code'] == 'ACC_OWNERSHIP') & 
            (observations['gender'] == 'all')
        ].sort_values('year')
        current_acc = acc_ownership['value_numeric'].iloc[-1] if len(acc_ownership) > 0 else 49.0
        prev_acc = acc_ownership['value_numeric'].iloc[-2] if len(acc_ownership) > 1 else 46.0
        
        with col1:
            st.metric(
                label="Account Ownership",
                value=f"{current_acc:.0f}%",
                delta=f"{current_acc - prev_acc:+.0f}pp vs 2021"
            )
        
        # Digital Payment
        with col2:
            st.metric(
                label="Digital Payment Usage",
                value="35%",
                delta="+7pp vs 2021"
            )
        
        # P2P/ATM Crossover Ratio
        with col3:
            st.metric(
                label="P2P/ATM Crossover Ratio",
                value="1.08x",
                delta="Historic First! 🎉",
                delta_color="normal"
            )
        
        # Telebirr Users
        with col4:
            st.metric(
                label="Telebirr Users",
                value="54.8M",
                delta="+45% YoY"
            )
        
        st.markdown("---")
        
        # Second row of metrics
        col5, col6, col7, col8 = st.columns(4)
        
        with col5:
            st.metric(
                label="M-Pesa Users",
                value="10.8M",
                delta="2+ years in market"
            )
        
        with col6:
            st.metric(
                label="4G Coverage",
                value="70.8%",
                delta="+33.3pp vs 2023"
            )
        
        with col7:
            st.metric(
                label="Gender Gap",
                value="20pp",
                delta="56% M vs 36% F",
                delta_color="inverse"
            )
        
        with col8:
            st.metric(
                label="NFIS-II Target",
                value="70%",
                delta="-21pp gap",
                delta_color="inverse"
            )
        
        st.markdown("---")
        
        # Growth Highlights
        st.subheader("📈 Growth Highlights")
        
        col_left, col_right = st.columns(2)
        
        with col_left:
            # P2P vs ATM Transactions Chart
            st.markdown("#### P2P vs ATM Transactions (FY2024/25)")
            
            transaction_data = pd.DataFrame({
                'Channel': ['P2P Digital', 'ATM Withdrawals'],
                'Transactions (M)': [128.3, 119.3],
                'YoY Growth': ['+158%', '+26%']
            })
            
            fig_txn = px.bar(
                transaction_data, 
                x='Channel', 
                y='Transactions (M)',
                color='Channel',
                color_discrete_map={'P2P Digital': '#27ae60', 'ATM Withdrawals': '#3498db'},
                text='Transactions (M)'
            )
            fig_txn.update_traces(texttemplate='%{text:.1f}M', textposition='outside')
            fig_txn.update_layout(showlegend=False, height=350)
            st.plotly_chart(fig_txn, use_container_width=True)
        
        with col_right:
            # Account Ownership Trajectory
            st.markdown("#### Account Ownership Trajectory")
            
            acc_data = pd.DataFrame({
                'Year': [2011, 2014, 2017, 2021, 2024],
                'Account Ownership (%)': [14, 22, 35, 46, 49]
            })
            
            fig_acc = px.line(
                acc_data, 
                x='Year', 
                y='Account Ownership (%)',
                markers=True,
                line_shape='spline'
            )
            fig_acc.add_hline(y=70, line_dash="dash", line_color="red", 
                            annotation_text="NFIS-II Target (70%)")
            fig_acc.update_traces(line_color='#27ae60', marker_size=10)
            fig_acc.update_layout(height=350)
            st.plotly_chart(fig_acc, use_container_width=True)
        
        # Data Summary
        st.markdown("---")
        st.subheader("📋 Data Summary")
        
        col_a, col_b, col_c = st.columns(3)
        
        with col_a:
            st.markdown("**Record Types**")
            record_counts = main_data['record_type'].value_counts()
            st.dataframe(record_counts, use_container_width=True)
        
        with col_b:
            st.markdown("**Events Timeline**")
            events_summary = events[['indicator', 'year']].dropna()
            events_summary = events_summary.sort_values('year', ascending=False).head(8)
            st.dataframe(events_summary, use_container_width=True, hide_index=True)
        
        with col_c:
            st.markdown("**Data Coverage**")
            st.write(f"• Total Records: {len(main_data)}")
            st.write(f"• Observations: {len(observations)}")
            st.write(f"• Events: {len(events)}")
            st.write(f"• Temporal Range: 2011-2025")
            st.write(f"• Pillars: ACCESS, USAGE, GENDER, AFFORDABILITY")

# ============================================================================
# PAGE 2: TRENDS
# ============================================================================
elif page == "📈 Trends":
    st.markdown('<h1 class="main-header">📈 Trend Analysis</h1>', unsafe_allow_html=True)
    
    if data_loaded:
        # Date range selector
        st.sidebar.markdown("### Filters")
        year_range = st.sidebar.slider(
            "Select Year Range",
            min_value=2011,
            max_value=2027,
            value=(2011, 2025)
        )
        
        # Pillar selector
        selected_pillars = st.sidebar.multiselect(
            "Select Pillars",
            options=['ACCESS', 'USAGE', 'GENDER', 'AFFORDABILITY'],
            default=['ACCESS', 'USAGE']
        )
        
        # Interactive Time Series Plot
        st.subheader("📊 Financial Inclusion Indicators Over Time")
        
        # Filter observations by selected pillars
        filtered_obs = observations[
            (observations['pillar'].isin(selected_pillars)) &
            (observations['year'] >= year_range[0]) &
            (observations['year'] <= year_range[1]) &
            (observations['unit'] == '%')
        ]
        
        if len(filtered_obs) > 0:
            # Group by indicator and year
            trend_data = filtered_obs.groupby(['indicator_code', 'year', 'pillar'])['value_numeric'].mean().reset_index()
            
            fig_trends = px.line(
                trend_data,
                x='year',
                y='value_numeric',
                color='indicator_code',
                markers=True,
                title='Indicator Trends by Year'
            )
            fig_trends.update_layout(
                xaxis_title='Year',
                yaxis_title='Value (%)',
                legend_title='Indicator',
                height=500
            )
            st.plotly_chart(fig_trends, use_container_width=True)
        else:
            st.info("No data available for selected filters. Try adjusting the year range or pillars.")
        
        st.markdown("---")
        
        # Channel Comparison View
        st.subheader("📱 Channel Comparison: Mobile Money Providers")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Mobile Money User Growth
            mm_data = pd.DataFrame({
                'Provider': ['Telebirr', 'M-Pesa', 'CBE Birr'],
                'Users (M)': [54.8, 10.8, 2.5],
                'Launch Year': [2021, 2023, 2017]
            })
            
            fig_mm = px.bar(
                mm_data,
                x='Provider',
                y='Users (M)',
                color='Provider',
                color_discrete_map={
                    'Telebirr': '#27ae60',
                    'M-Pesa': '#e74c3c', 
                    'CBE Birr': '#3498db'
                },
                title='Mobile Money User Base (2024/25)'
            )
            fig_mm.update_traces(texttemplate='%{y:.1f}M', textposition='outside')
            fig_mm.update_layout(showlegend=False, height=400)
            st.plotly_chart(fig_mm, use_container_width=True)
        
        with col2:
            # Infrastructure Growth
            infra_data = pd.DataFrame({
                'Year': ['2023', '2025'],
                '4G Coverage (%)': [37.5, 70.8],
                'Smartphone Penetration (%)': [20, 24]
            })
            
            fig_infra = go.Figure()
            fig_infra.add_trace(go.Bar(
                name='4G Coverage',
                x=infra_data['Year'],
                y=infra_data['4G Coverage (%)'],
                marker_color='#3498db',
                text=infra_data['4G Coverage (%)'].apply(lambda x: f'{x}%'),
                textposition='outside'
            ))
            fig_infra.add_trace(go.Bar(
                name='Smartphone Penetration',
                x=infra_data['Year'],
                y=infra_data['Smartphone Penetration (%)'],
                marker_color='#9b59b6',
                text=infra_data['Smartphone Penetration (%)'].apply(lambda x: f'{x}%'),
                textposition='outside'
            ))
            fig_infra.update_layout(
                title='Infrastructure Growth',
                barmode='group',
                height=400
            )
            st.plotly_chart(fig_infra, use_container_width=True)
        
        st.markdown("---")
        
        # Gender Gap Analysis
        st.subheader("👥 Gender Gap in Financial Inclusion")
        
        gender_data = pd.DataFrame({
            'Year': [2017, 2021, 2024],
            'Male': [40, 56, 58],
            'Female': [30, 36, 38],
            'Gap': [10, 20, 20]
        })
        
        fig_gender = go.Figure()
        fig_gender.add_trace(go.Scatter(
            x=gender_data['Year'], y=gender_data['Male'],
            name='Male', mode='lines+markers',
            line=dict(color='#3498db', width=3),
            marker=dict(size=10)
        ))
        fig_gender.add_trace(go.Scatter(
            x=gender_data['Year'], y=gender_data['Female'],
            name='Female', mode='lines+markers',
            line=dict(color='#e74c3c', width=3),
            marker=dict(size=10)
        ))
        fig_gender.add_trace(go.Bar(
            x=gender_data['Year'], y=gender_data['Gap'],
            name='Gender Gap',
            marker_color='rgba(155, 89, 182, 0.5)',
            yaxis='y2'
        ))
        fig_gender.update_layout(
            title='Account Ownership by Gender',
            xaxis_title='Year',
            yaxis_title='Account Ownership (%)',
            yaxis2=dict(title='Gap (pp)', overlaying='y', side='right'),
            height=450,
            legend=dict(orientation='h', yanchor='bottom', y=1.02)
        )
        st.plotly_chart(fig_gender, use_container_width=True)
        
        # Download data
        st.markdown("---")
        st.subheader("📥 Download Data")
        
        csv = observations.to_csv(index=False)
        st.download_button(
            label="Download Observations CSV",
            data=csv,
            file_name="ethiopia_fi_observations.csv",
            mime="text/csv"
        )

# ============================================================================
# PAGE 3: FORECASTS
# ============================================================================
elif page == "🔮 Forecasts":
    st.markdown('<h1 class="main-header">🔮 Forecasts (2025-2027)</h1>', unsafe_allow_html=True)
    
    if data_loaded:
        # Model selection
        st.sidebar.markdown("### Forecast Settings")
        model_type = st.sidebar.selectbox(
            "Select Model",
            ["Event-Augmented (Recommended)", "Linear Trend Only"]
        )
        
        show_ci = st.sidebar.checkbox("Show Confidence Intervals", value=True)
        
        # Forecast data
        acc_forecast = pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027],
            'Account Ownership (%)': [49.0, 61.8, 73.7, 82.5],
            'Trend Only': [49.0, 54.8, 57.7, 60.5],
            'CI Lower': [49.0, 42.9, 53.9, 61.9],
            'CI Upper': [49.0, 80.8, 93.4, 103.1],
            'Pessimistic': [49.0, 57.8, 64.7, 70.0],
            'Optimistic': [49.0, 64.4, 79.5, 90.6]
        })
        
        dp_forecast = pd.DataFrame({
            'Year': [2024, 2025, 2026, 2027],
            'Digital Payment (%)': [42.0, 59.6, 82.9, 100.0],  # Capped at 100
            'Trend Only': [42.0, 48.6, 52.9, 57.3],
            'CI Lower': [42.0, 35.8, 59.1, 79.1],
            'CI Upper': [42.0, 83.4, 100.0, 100.0],  # Capped
            'Pessimistic': [42.0, 53.3, 66.4, 79.1],
            'Optimistic': [42.0, 63.6, 93.4, 100.0]  # Capped
        })
        
        # Forecast Visualizations
        st.subheader("📊 Account Ownership Forecast")
        
        fig_acc_fc = go.Figure()
        
        # Historical data
        fig_acc_fc.add_trace(go.Scatter(
            x=[2011, 2014, 2017, 2021, 2024],
            y=[14, 22, 35, 46, 49],
            name='Historical',
            mode='lines+markers',
            line=dict(color='#2c3e50', width=2),
            marker=dict(size=10)
        ))
        
        if model_type == "Event-Augmented (Recommended)":
            # Base forecast
            fig_acc_fc.add_trace(go.Scatter(
                x=acc_forecast['Year'],
                y=acc_forecast['Account Ownership (%)'],
                name='Base Scenario',
                mode='lines+markers',
                line=dict(color='#27ae60', width=3),
                marker=dict(size=12)
            ))
            
            if show_ci:
                # Confidence interval
                fig_acc_fc.add_trace(go.Scatter(
                    x=list(acc_forecast['Year']) + list(acc_forecast['Year'][::-1]),
                    y=list(acc_forecast['CI Upper']) + list(acc_forecast['CI Lower'][::-1]),
                    fill='toself',
                    fillcolor='rgba(39, 174, 96, 0.2)',
                    line=dict(color='rgba(255,255,255,0)'),
                    name='95% CI'
                ))
        else:
            # Trend only
            fig_acc_fc.add_trace(go.Scatter(
                x=acc_forecast['Year'],
                y=acc_forecast['Trend Only'],
                name='Linear Trend',
                mode='lines+markers',
                line=dict(color='#7f8c8d', width=2, dash='dash'),
                marker=dict(size=10)
            ))
        
        # NFIS-II Target
        fig_acc_fc.add_hline(y=70, line_dash="dash", line_color="red",
                           annotation_text="NFIS-II Target (70%)")
        
        fig_acc_fc.update_layout(
            xaxis_title='Year',
            yaxis_title='Account Ownership (%)',
            yaxis_range=[0, 110],
            height=500,
            legend=dict(orientation='h', yanchor='bottom', y=1.02)
        )
        st.plotly_chart(fig_acc_fc, use_container_width=True)
        
        st.markdown("---")
        
        st.subheader("💳 Digital Payment Usage Forecast")
        
        fig_dp_fc = go.Figure()
        
        # Historical data
        fig_dp_fc.add_trace(go.Scatter(
            x=[2017, 2021, 2024],
            y=[12, 35, 42],
            name='Historical/Estimated',
            mode='lines+markers',
            line=dict(color='#2c3e50', width=2),
            marker=dict(size=10)
        ))
        
        if model_type == "Event-Augmented (Recommended)":
            fig_dp_fc.add_trace(go.Scatter(
                x=dp_forecast['Year'],
                y=dp_forecast['Digital Payment (%)'],
                name='Base Scenario',
                mode='lines+markers',
                line=dict(color='#3498db', width=3),
                marker=dict(size=12)
            ))
            
            if show_ci:
                fig_dp_fc.add_trace(go.Scatter(
                    x=list(dp_forecast['Year']) + list(dp_forecast['Year'][::-1]),
                    y=list(dp_forecast['CI Upper']) + list(dp_forecast['CI Lower'][::-1]),
                    fill='toself',
                    fillcolor='rgba(52, 152, 219, 0.2)',
                    line=dict(color='rgba(255,255,255,0)'),
                    name='95% CI'
                ))
        else:
            fig_dp_fc.add_trace(go.Scatter(
                x=dp_forecast['Year'],
                y=dp_forecast['Trend Only'],
                name='Linear Trend',
                mode='lines+markers',
                line=dict(color='#7f8c8d', width=2, dash='dash'),
                marker=dict(size=10)
            ))
        
        fig_dp_fc.update_layout(
            xaxis_title='Year',
            yaxis_title='Digital Payment Usage (%)',
            yaxis_range=[0, 110],
            height=500,
            legend=dict(orientation='h', yanchor='bottom', y=1.02)
        )
        st.plotly_chart(fig_dp_fc, use_container_width=True)
        
        st.markdown("---")
        
        # Forecast Table
        st.subheader("📋 Forecast Summary Table")
        
        forecast_summary = pd.DataFrame({
            'Year': [2025, 2026, 2027],
            'Account Ownership (Base)': ['61.8%', '73.7%', '82.5%'],
            'ACC Range': ['57.8% - 64.4%', '64.7% - 79.5%', '70.0% - 90.6%'],
            'Digital Payment (Base)': ['59.6%', '82.9%', '100.0%'],
            'DP Range': ['53.3% - 63.6%', '66.4% - 93.4%', '79.1% - 100%']
        })
        
        st.dataframe(forecast_summary, use_container_width=True, hide_index=True)
        
        # Key Milestones
        st.subheader("🏆 Key Projected Milestones")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.success("**2025**: Account ownership surpasses 60%")
        
        with col2:
            st.success("**2026**: Digital payments exceed 80%, NFIS-II target reached")
        
        with col3:
            st.success("**2027**: Near-universal digital payment adoption")
        
        # Download forecasts
        st.markdown("---")
        csv_fc = forecast_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Forecast Data CSV",
            data=csv_fc,
            file_name="ethiopia_fi_forecasts_2025_2027.csv",
            mime="text/csv"
        )

# ============================================================================
# PAGE 4: INCLUSION PROJECTIONS
# ============================================================================
elif page == "🎯 Inclusion Projections":
    st.markdown('<h1 class="main-header">🎯 Financial Inclusion Projections</h1>', unsafe_allow_html=True)
    
    if data_loaded:
        # Scenario selector
        st.sidebar.markdown("### Scenario Settings")
        selected_scenario = st.sidebar.selectbox(
            "Select Scenario",
            ["Base Case", "Optimistic", "Pessimistic"]
        )
        
        # Scenario data
        scenarios = {
            'Base Case': {
                '2025': 61.8, '2026': 73.7, '2027': 82.5,
                'description': 'Expected event effects materialize as planned'
            },
            'Optimistic': {
                '2025': 64.4, '2026': 79.5, '2027': 90.6,
                'description': 'Strong execution, synergies realized, accelerated adoption'
            },
            'Pessimistic': {
                '2025': 57.8, '2026': 64.7, '2027': 70.0,
                'description': 'Economic headwinds, slower adoption, infrastructure delays'
            }
        }
        
        scenario_data = scenarios[selected_scenario]
        
        # Progress toward target visualization
        st.subheader(f"📊 Progress Toward 70% Target ({selected_scenario})")
        
        # Gauge chart for 2025 projection
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=scenario_data['2025'],
            delta={'reference': 70, 'relative': False, 'position': "bottom"},
            title={'text': f"2025 Account Ownership Projection<br><span style='font-size:0.8em;color:gray'>{selected_scenario}</span>"},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1},
                'bar': {'color': "#27ae60" if scenario_data['2025'] >= 60 else "#e74c3c"},
                'steps': [
                    {'range': [0, 49], 'color': "#fadbd8"},
                    {'range': [49, 70], 'color': "#fdebd0"},
                    {'range': [70, 100], 'color': "#d5f5e3"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 70
                }
            }
        ))
        fig_gauge.update_layout(height=400)
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        st.info(f"**Scenario Description**: {scenario_data['description']}")
        
        st.markdown("---")
        
        # All scenarios comparison
        st.subheader("📈 Scenario Comparison")
        
        fig_scenarios = go.Figure()
        
        # Historical
        fig_scenarios.add_trace(go.Scatter(
            x=[2011, 2014, 2017, 2021, 2024],
            y=[14, 22, 35, 46, 49],
            name='Historical',
            mode='lines+markers',
            line=dict(color='#2c3e50', width=2),
            marker=dict(size=8)
        ))
        
        # All three scenarios
        colors = {'Base Case': '#27ae60', 'Optimistic': '#3498db', 'Pessimistic': '#e74c3c'}
        for scenario_name, data in scenarios.items():
            fig_scenarios.add_trace(go.Scatter(
                x=[2024, 2025, 2026, 2027],
                y=[49, data['2025'], data['2026'], data['2027']],
                name=scenario_name,
                mode='lines+markers',
                line=dict(color=colors[scenario_name], width=2, 
                         dash='solid' if scenario_name == selected_scenario else 'dot'),
                marker=dict(size=8 if scenario_name == selected_scenario else 6)
            ))
        
        # Target line
        fig_scenarios.add_hline(y=70, line_dash="dash", line_color="purple",
                               annotation_text="NFIS-II Target (70%)")
        
        fig_scenarios.update_layout(
            xaxis_title='Year',
            yaxis_title='Account Ownership (%)',
            yaxis_range=[0, 100],
            height=500,
            legend=dict(orientation='h', yanchor='bottom', y=1.02)
        )
        st.plotly_chart(fig_scenarios, use_container_width=True)
        
        st.markdown("---")
        
        # Consortium Key Questions
        st.subheader("❓ Answers to Consortium's Key Questions")
        
        with st.expander("1. Will Ethiopia meet the NFIS-II target of 70% account ownership by 2025?", expanded=True):
            st.markdown("""
            **Answer: Very Unlikely** ❌
            
            - **Current (2024)**: 49%
            - **2025 Forecast (Base)**: 61.8%
            - **Gap to Target**: ~8pp
            
            Even in the optimistic scenario (64.4%), Ethiopia falls short of the 70% target. 
            The target may be reached by **2026** in base/optimistic scenarios.
            """)
        
        with st.expander("2. What events will have the largest impact on financial inclusion?"):
            st.markdown("""
            **Top 5 High-Impact Events:**
            
            | Rank | Event | ACCESS Impact | USAGE Impact | Confidence |
            |------|-------|--------------|--------------|------------|
            | 1 | Interoperability Full Launch (2026) | +4pp | +16pp | Low |
            | 2 | EthioPay Instant Payment (2025) | +3pp | +15pp | Low |
            | 3 | Telebirr Continued Growth | +6pp | +9pp | Medium |
            | 4 | Fayda Digital ID Rollout | +6pp | +2pp | Low |
            | 5 | M-Pesa Market Penetration | +3pp | +6pp | Medium |
            
            **Key Insight**: Interoperability and instant payment infrastructure have the highest 
            potential impact on USAGE, while Telebirr and Digital ID drive ACCESS growth.
            """)
        
        with st.expander("3. What are the key risks and uncertainties?"):
            st.markdown("""
            **Key Uncertainties:**
            
            1. **Data Sparsity**: Only 5 Findex data points over 13 years; CI width of ±21pp
            2. **Event Execution**: Interoperability & EthioPay timing uncertain; could shift forecasts by ±5pp
            3. **Macro Headwinds**: FX volatility, inflation may slow adoption
            4. **Survey vs Admin Gap**: Mobile money registrations ≠ Findex ownership (4x gap observed)
            5. **Gender Gap**: Women's adoption trajectory could drag overall rates
            
            **Confidence Assessment:**
            - ACCESS forecast: **MEDIUM** confidence (historical trend well-established)
            - USAGE forecast: **LOW** confidence (sparse data, proxy-based estimates)
            - Event effects: **LOW-MEDIUM** confidence (based on comparable countries)
            """)
        
        with st.expander("4. What is the P2P/ATM crossover significance?"):
            st.markdown("""
            **Historic Milestone: P2P > ATM in FY2024/25** 🎉
            
            - **P2P Transactions**: 128.3M (+158% YoY)
            - **ATM Transactions**: 119.3M (+26% YoY)
            - **Crossover Ratio**: 1.08x
            
            **Significance:**
            - First time digital P2P transfers exceed ATM cash withdrawals in Ethiopia
            - Indicates behavioral shift from cash to digital payments
            - Validates mobile money adoption success
            - Suggests USAGE indicators may grow faster than ACCESS
            """)
        
        # Download full report
        st.markdown("---")
        st.subheader("📥 Download Reports")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Download forecast data
            csv_fc = forecast_data.to_csv(index=False)
            st.download_button(
                label="📊 Download Forecast Data",
                data=csv_fc,
                file_name="ethiopia_fi_forecasts.csv",
                mime="text/csv"
            )
        
        with col2:
            # Download impact matrix
            csv_impact = impact_matrix.to_csv(index=False)
            st.download_button(
                label="📈 Download Impact Matrix",
                data=csv_impact,
                file_name="event_impact_matrix.csv",
                mime="text/csv"
            )

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Ethiopia Financial Inclusion Forecasting Dashboard | Selam Analytics | February 2026"
    "</div>",
    unsafe_allow_html=True
)
