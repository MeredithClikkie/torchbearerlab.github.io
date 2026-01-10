import streamlit as st
import pandas as pd
import datetime
import os

# --- FILE SETUP ---

file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/trench_health.xlsx'

def load_data():
    """Loads data from Excel or creates a new DataFrame if the file doesn't exist."""
    if os.path.exists(file_path):
        return pd.read_excel(file_path)
    else:
        # Create empty DataFrame with required columns
        return pd.DataFrame(columns=['Date', 'Metric', 'Value', 'Notes'])


def save_data(file_path):
    """Saves the DataFrame back to the Excel file."""
    df.to_excel(file_path, index=False)


# --- APP UI ---
st.set_page_config(page_title="Trench Survival Log", page_icon="💛")
st.title("🛡️ Trench Survival: Excel Health Log")
st.markdown("Track your vitals and escape the cycle of **Vialism** using an Excel backend.")

# Load current data
df = load_data()

# 1. DATA ENTRY SECTION
with st.expander("➕ Log New Lab Results"):
    with st.form("health_form", clear_on_submit=True):
        date = st.date_input("Date of Lab/Test", datetime.date.today())
        metric = st.selectbox("Metric", ["Vitamin D", "Iron", "Cholesterol", "B12", "Other"])
        value = st.number_input("Result Value", min_value=0.0, format="%.2f")
        notes = st.text_area("Imaging Notes / Physician Comments")

        if st.form_submit_button("Record in Survival Log"):
            # Create a new row
            new_row = pd.DataFrame({
                'Date': [date.strftime("%Y-%m-%d")],
                'Metric': [metric],
                'Value': [value],
                'Notes': [notes]
            })
            # Append and save
            df = pd.concat([df, new_row], ignore_index=True)
            save_data(df)
            st.success(f"Log secured in {EXCEL_FILE}!")
            st.rerun()

# 2. DATA VISUALIZATION
if not df.empty:
    st.divider()
    st.subheader("📈 Health Trends Over Time")

    # Filter by metric for the chart
    available_metrics = df['Metric'].unique()
    selected_metric = st.selectbox("Select metric to visualize:", available_metrics)

    # Filter and sort data for plotting
    plot_df = df[df['Metric'] == selected_metric].copy()
    plot_df['Date'] = pd.to_datetime(plot_df['Date'])
    plot_df = plot_df.sort_values('Date')

    if not plot_df.empty:
        latest_val = plot_df.iloc[-1]['Value']
        # Lore-based indicator logic (Example threshold for Vitamin D)
        status = "🟡 BANDITO (Optimal)" if latest_val >= 30 else "🔴 VIALISM (Sub-optimal)"

        st.metric(label=f"Latest {selected_metric}", value=latest_val, delta=status)
        st.line_chart(plot_df.set_index('Date')['Value'])

    # 3. FULL LOG TABLE
    st.subheader("📜 The Complete Chronicles")
    st.dataframe(df, use_container_width=True)

    # Download button for the Excel file
    with open(EXCEL_FILE, "rb") as file:
        st.download_button(
            label="📂 Download Survival Log (Excel)",
            data=file,
            file_name=EXCEL_FILE,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.info("No logs found. Start your journey by entering your first lab result.")