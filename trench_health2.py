import streamlit as st
import pandas as pd
import datetime
import os

# --- FILE SETUP ---

file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/trench_health2.xlsx'

def load_data():
    """Loads data from Excel or creates a new DataFrame if the file doesn't exist."""
    if os.path.exists(file_path):
        return pd.read_excel(file_path)

def save_data(file_path):
    """Saves the DataFrame back to the Excel file."""
    df.to_excel(file_path, index=False)


# --- STYLE LOGIC (Lore Formatting) ---
def style_health_log(row):
    """Applies yellow background for good results and red for concerns."""
    # Example threshold: Vitamin D > 30 is Bandito (Yellow)
    if row['Panel'] == 'Vitamin D':
        color = 'background-color: rgba(255, 215, 0, 0.3)' if row[
                                                                  'Results'] >= 30 else 'background-color: rgba(255, 75, 75, 0.3)'
    else:
        color = ''  # Default
    return [color] * len(row)


# --- APP UI ---
st.set_page_config(page_title="Trench Survival Dashboard", layout="wide")
st.title("🛡️ The Trench Survival Dashboard")

df = load_data()

# 1. SIDEBAR: DATA ENTRY
with st.sidebar:
    st.header("➕ Log New Evidence")
    with st.form("entry_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.date.today())
        metric = st.selectbox("Panel", ["Vitamin D", "Iron", "B12", "Cholesterol", "Other"])
        value = st.number_input("Results", min_value=0.0)
        notes = st.text_input("Facility")

        if st.form_submit_button("Record in Archives"):
            new_entry = pd.DataFrame(
                {'Date': [pd.to_datetime(date)], 'Panel': [metric], 'Results': [value], 'Facility': [notes]})
            df = pd.concat([df, new_entry], ignore_index=True)
            save_data(df)
            st.success("Evidence Secured!")
            st.rerun()

# 2. MAIN DASHBOARD: CHARTS
if not df.empty:
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📈 Survival Trends")
        selected_metric = st.selectbox("Select Metric to View", df['Panel'].unique())
        plot_df = df[df['Panel'] == selected_metric].sort_values('Date')

        # Streamlit Line Chart
        st.line_chart(plot_df.set_index('Date')['Results'])

    with col2:
        st.subheader("⚠️ Lore Status")
        if not plot_df.empty:
            latest = plot_df.iloc[-1]
            # Custom status based on TØP Lore
            is_optimal = latest['Results'] >= 30  # Simple example threshold
            status_text = "🟡 BANDITO STATUS: Optimal" if is_optimal else "🔴 VIALISM: Action Required"
            st.info(status_text)
            st.metric("Latest Result", f"{latest['Results']}", delta="Optimal" if is_optimal else "Low",
                      delta_color="normal" if is_optimal else "inverse")

    # 3. STYLED TABLE
    st.divider()
    st.subheader("📜 Styled Survival Logs")
    # Apply the Lore-based background colors to the table
    styled_df = df.style.apply(style_health_log, axis=1)
    st.dataframe(styled_df, use_container_width=True)

else:
    st.warning("Your archives are empty. Enter your first lab result in the sidebar to begin.")
