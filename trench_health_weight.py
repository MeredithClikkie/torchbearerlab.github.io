import streamlit as st
import pandas as pd
import datetime
import os

# --- FILE SETTINGS ---
MAIN_FILE = '/Users/meredithsmith/Desktop/TØPAnalysis/trench_health.xlsx'
HISTORY_FILE = '/Users/meredithsmith/Desktop/TØPAnalysis/Trench_Weight_History2.xlsx'

def load_unified_data():
    """Merges historical data with active logs without calculating BMI."""
    # 1. Load Current Main Data
    if os.path.exists(MAIN_FILE):
        main_df = pd.read_excel(MAIN_FILE)
    else:
        main_df = pd.DataFrame(columns=['Date', 'Weight', 'BMI', 'Metric', 'Value', 'Notes'])

    # 2. Load History 2011 Data
    if os.path.exists(HISTORY_FILE):
        hist_df = pd.read_excel(HISTORY_FILE)
        # Optional: Rename columns if they differ in your history file
        # hist_df = hist_df.rename(columns={'YourOldName': 'Weight', 'OldBMI': 'BMI'})
    else:
        hist_df = pd.DataFrame()

    # 3. Combine into Master Chronicles
    combined = pd.concat([main_df, hist_df], ignore_index=True)

    if not combined.empty:
        # Convert Dates and Sort for the timeline charts
        combined['Date'] = pd.to_datetime(combined['Date'])
        combined = combined.sort_values('Date')

    return combined


# --- APP UI ---
st.set_page_config(page_title="Trench Unified Tracker", layout="wide")
st.title("🛡️ The Unified Survival Chronicles")
st.markdown("Displaying your historical BMI and Weight data since 2011.")

df = load_unified_data()

# 1. SIDEBAR ENTRY (Saves to MAIN_FILE)
with st.sidebar:
    st.header("➕ New Entry")
    with st.form("entry_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.date.today())
        weight = st.number_input("Weight (lbs)", min_value=0.0)
        bmi = st.number_input("BMI (Current)", min_value=0.0, format="%.2f")
        metric = st.selectbox("Other Metric", ["None", "Vitamin D", "Iron", "B12"])
        val = st.number_input("Result Value", min_value=0.0)
        note = st.text_input("Notes")

        if st.form_submit_button("Record in Archives"):
            new_entry = pd.DataFrame({
                'Date': [pd.to_datetime(date)],
                'Weight': [weight],
                'BMI': [bmi],
                'Metric': [metric],
                'Value': [val],
                'Notes': [note]
            })

            # Save to active file
            if os.path.exists(MAIN_FILE):
                existing_main = pd.read_excel(MAIN_FILE)
                updated_main = pd.concat([existing_main, new_entry], ignore_index=True)
            else:
                updated_main = new_entry

            updated_main.to_excel(MAIN_FILE, index=False)
            st.success("Entry added!")
            st.rerun()

# 2. VISUALIZATION
if not df.empty:
    tab1, tab2 = st.tabs(["📉 Long-Term Trends", "📜 Full Chronicles"])

    with tab1:
        # Metrics Row
        col1, col2 = st.columns(2)
        latest_bmi = df.dropna(subset=['BMI']).iloc[-1]['BMI']
        latest_weight = df.dropna(subset=['Weight']).iloc[-1]['Weight']

        col1.metric("Current Weight", f"{latest_weight} lbs")
        col2.metric("Current BMI", f"{latest_bmi}")

        st.subheader("Weight & BMI Journey")
        # Line chart showing your pre-existing Weight and BMI columns
        st.line_chart(df.set_index('Date')[['Weight', 'BMI']])

    with tab2:
        st.subheader("Master Medical History")
        st.dataframe(df.sort_values('Date', ascending=False), use_container_width=True)
else:
    st.info("No data found. Ensure your history file is in the same folder as this script.")