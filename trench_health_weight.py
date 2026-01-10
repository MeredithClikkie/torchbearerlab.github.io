import streamlit as st
import pandas as pd
import datetime
import os

# --- FILE PATHS ---
LAB_FILE = '/Users/meredithsmith/Desktop/TØPAnalysis/trench_health2.xlsx'
WEIGHT_FILE = '/Users/meredithsmith/Desktop/TØPAnalysis/Trench_Weight_History2.xlsx'


# --- DATA LOGIC ---
def load_combined_data():
    # 1. Load Lab Data (Panel, Results, Facility)
    if os.path.exists(LAB_FILE):
        lab_df = pd.read_excel(LAB_FILE)
        lab_df = lab_df.rename(columns={'Panel': 'Panel', 'Results': 'Lab_Value', 'Facility': 'Notes'})
    else:
        lab_df = pd.DataFrame(columns=['Date', 'Panel', 'Lab_Value', 'Notes'])

    # 2. Load Weight History (Weight, BMI)
    if os.path.exists(WEIGHT_FILE):
        weight_df = pd.read_excel(WEIGHT_FILE)
        # Assuming your weight file already has Date, Weight, and BMI
    else:
        weight_df = pd.DataFrame(columns=['Date', 'Weight', 'BMI'])

    # Ensure Date types match
    lab_df['Date'] = pd.to_datetime(lab_df['Date'])
    weight_df['Date'] = pd.to_datetime(weight_df['Date'])

    # 3. Merge files on Date
    combined = pd.merge(lab_df, weight_df, on='Date', how='outer')
    return combined.sort_values('Date', ascending=True)


def style_health_log(row):
    """Lore-based highlighting."""
    # Bandito Yellow for optimal Vitamin D
    if row['Panel'] == 'Vitamin D' and pd.notnull(row['Lab_Value']):
        color = 'background-color: rgba(255, 215, 0, 0.3)' if row[
                                                                  'Lab_Value'] >= 30 else 'background-color: rgba(255, 75, 75, 0.3)'
    # Vialism Red for BMI out of range
    elif pd.notnull(row['BMI']):
        color = 'background-color: rgba(255, 215, 0, 0.3)' if 18.5 <= row[
            'BMI'] <= 24.9 else 'background-color: rgba(255, 75, 75, 0.3)'
    else:
        color = ''
    return [color] * len(row)


# --- APP UI ---
st.set_page_config(page_title="Trench Unified Dashboard", layout="wide")
st.title("🛡️ The Unified Survival Chronicles")

df = load_combined_data()

# 1. SIDEBAR: DATA ENTRY
with st.sidebar:
    st.header("➕ Log New Evidence")
    entry_type = st.radio("What are you logging?", ["Lab Results", "Physical Vitals"])

    with st.form("entry_form", clear_on_submit=True):
        date = st.date_input("Date", datetime.date.today())

        if entry_type == "Lab Results":
            panel = st.selectbox("Panel", ["Vitamin D", "Iron", "B12", "Cholesterol", "Other"])
            res = st.number_input("Results", min_value=0.0)
            fac = st.text_input("Facility")

            if st.form_submit_button("Record Labs"):
                new = pd.DataFrame(
                    {'Date': [pd.to_datetime(date)], 'Panel': [panel], 'Results': [res], 'Facility': [fac]})
                # Append to existing lab file
                existing = pd.read_excel(LAB_FILE) if os.path.exists(LAB_FILE) else pd.DataFrame()
                pd.concat([existing, new], ignore_index=True).to_excel(LAB_FILE, index=False)
                st.success("Lab Archives Updated!")
                st.rerun()

        else:
            wgt = st.number_input("Weight (lbs)", min_value=0.0)
            bmi_val = st.number_input("BMI (from your file)", min_value=0.0)

            if st.form_submit_button("Record Vitals"):
                new = pd.DataFrame({'Date': [pd.to_datetime(date)], 'Weight': [wgt], 'BMI': [bmi_val]})
                # Append to existing weight file
                existing = pd.read_excel(WEIGHT_FILE) if os.path.exists(WEIGHT_FILE) else pd.DataFrame()
                pd.concat([existing, new], ignore_index=True).to_excel(WEIGHT_FILE, index=False)
                st.success("Vitals Secured!")
                st.rerun()

# 2. MAIN DASHBOARD
if not df.empty:
    tab1, tab2 = st.tabs(["📉 Survival Trends", "📜 Master Chronicles"])

    with tab1:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Physical Vitals (Weight & BMI)")
            if not df['Weight'].dropna().empty:
                st.line_chart(df.dropna(subset=['Weight']).set_index('Date')[['Weight', 'BMI']])

        with col2:
            st.subheader("Lab Panels")
            lab_only = df.dropna(subset=['Panel'])
            if not lab_only.empty:
                selected = st.selectbox("Select Panel", lab_only['Panel'].unique())
                plot_df = lab_only[lab_only['Panel'] == selected]
                st.line_chart(plot_df.set_index('Date')['Lab_Value'])

                # Metric display
                latest = plot_df.iloc[-1]
                is_opt = latest['Lab_Value'] >= 30 if selected == 'Vitamin D' else True
                st.metric(f"Latest {selected}", f"{latest['Lab_Value']}",
                          delta="Optimal" if is_opt else "Low",
                          delta_color="normal" if is_opt else "inverse")

    with tab2:
        st.subheader("Unified Medical Logs")
        styled_df = df.sort_values('Date', ascending=False).style.apply(style_health_log, axis=1)
        st.dataframe(styled_df, use_container_width=True)

else:
    st.warning("No data found in your Excel files.")