import streamlit as st
import pandas as pd
import datetime
import os

# --- SETTINGS ---
MAIN_FILE = '/Users/meredithsmith/Desktop/TØPAnalysis/trench_health.xlsx'
LEGACY_FILE = '/Users/meredithsmith/Desktop/TØPAnalysis/Trench_Weight_History2.xlsx'
USER_HEIGHT_IN = 63  # Enter your height once to calculate BMI from weight


def calculate_bmi(weight_lb):
    """Imperial BMI formula."""
    return (weight_lb * 703) / (USER_HEIGHT_IN ** 2)


def load_all_data():
    # 1. Load Main App Data
    main_df = pd.read_excel(MAIN_FILE) if os.path.exists(MAIN_FILE) else pd.DataFrame()

    # 2. Load Legacy 2011 Data
    legacy_df = pd.read_excel(LEGACY_FILE) if os.path.exists(LEGACY_FILE) else pd.DataFrame()

    # 3. Combine and Clean
    full_df = pd.concat([main_df, legacy_df], ignore_index=True)
    if not full_df.empty:
        full_df['Date'] = pd.to_datetime(full_df['Date'])
        # Automatically calculate BMI for any row with Weight
        if 'Weight' in full_df.columns:
            full_df['BMI'] = full_df['Weight'].apply(lambda x: calculate_bmi(x) if pd.notnull(x) else None)
        full_df = full_df.sort_values('Date')
    return full_df


# --- APP UI ---
st.title("🛡️ Trench Survival: Long-Term Chronicles")
df = load_all_data()

# 1. SIDEBAR: DATA ENTRY
with st.sidebar:
    st.header("➕ Log Today's Vitals")
    with st.form("vit_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.date.today())
        weight = st.number_input("Weight (lbs)", min_value=0.0)
        metric = st.selectbox("Other Metric", ["None", "Vitamin D", "Iron", "B12"])
        val = st.number_input("Metric Value", min_value=0.0)

        if st.form_submit_button("Record"):
            new_row = pd.DataFrame(
                {'Date': [pd.to_datetime(date)], 'Weight': [weight], 'Metric': [metric], 'Value': [val]})
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_excel(MAIN_FILE, index=False)
            st.rerun()

# 2. CHARTS (Weight & BMI Trends)
if not df.empty and 'Weight' in df.columns:
    st.subheader("📉 Weight & BMI Journey (Since 2011)")

    # Multi-line chart for Weight and BMI
    # Note: Streamlit line_chart displays all columns in the dataframe except the index
    chart_data = df.set_index('Date')[['Weight', 'BMI']]
    st.line_chart(chart_data)

    # "Lore" Status for Weight
    latest_bmi = df.dropna(subset=['BMI']).iloc[-1]['BMI']
    status = "🟡 BANDITO: Healthy Range" if 18.5 <= latest_bmi <= 24.9 else "🔴 VIALISM: Out of Range"
    st.metric("Current BMI Status", f"{latest_bmi:.1f}", delta=status)