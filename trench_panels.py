import streamlit as st
import pandas as pd
import datetime
import os

# --- FILE SETUP ---

file_path = '/Users/meredithsmith/Desktop/TØPAnalysis/trench_health3.xlsx'

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
        metric = st.selectbox("Panel", ['25-Oh Vitamin D3',
                                         'Alanine Aminotransferase',
                                         'Albumin',
                                         'Alk Phos Total',
                                         'Alt (Sgpt)',
                                         'Anion Gap',
                                         'Anti - Ccp Ab, Igg/Iga',
                                         'Anti - Dna Antibody, Double',
                                         'Aspartate Aminotransferase(Ast)',
                                         'Ast (Sgot)',
                                         'Basophils %',
                                         'Basophils Absolute',
                                         'Bilirubin Direct',
                                         'Bilirubin Total',
                                         'Blood Urea Nitrogen (Bun)',
                                         'Bun/Creatinine Ratio',
                                         'C3 Complement',
                                         'C4 Complement',
                                         'Calcium Level Total',
                                         'Chloride',
                                         'Cholesterol, Total',
                                         'Cholesterol/Hdl Ratio',
                                         'Ck',
                                         'Co2',
                                         'Cortisol Rhythm, Total',
                                         'Covid',
                                         'Creatinine',
                                         'Crp',
                                         'Crp (High Sensitivity)',
                                         'Cyclic Citruillinated Pep Igg Cp',
                                         'Egfr',
                                         'Eosinophils %',
                                         'Eosinophils Absolute',
                                         'Epithelial Cells (Non Renal)',
                                         'Estimated Average Glucose',
                                         'Estrogen Total',
                                         'Ferritin',
                                         'Fibrinogen Activity',
                                         'Follicle-Stimulating Hormone (Fsh)',
                                         'Free T3',
                                         'Free T4',
                                         'Free Thyroxine Index',
                                         'Free/Weakly Bound',
                                         'Fti',
                                         'Ggt',
                                         'Globulin, Total',
                                         'Glucose',
                                         'Hct',
                                         'Hdl',
                                         'Hematocrit',
                                         'Hemoglobin',
                                         'Hemoglobin A1C',
                                         'Hgb',
                                         'Homocysteine',
                                         'Immature Granulocytes (Abs)',
                                         'Iron',
                                         'Iron Saturation',
                                         'Ketones Pol',
                                         'Ldh',
                                         'Ldl',
                                         'Luteinizing Hormone (Lh)',
                                         'Lyme Disease Ab Total Antibody With Reflex',
                                         'Lymphocytes %',
                                         'Lymphocytes Absolute',
                                         'Magnesium',
                                         'Mch',
                                         'Mchc',
                                         'Mcv',
                                         'Monocytes %',
                                         'Monocytes Absolute',
                                         'Mpv',
                                         'Neutrophils %',
                                         'Neutrophils Absolute',
                                         'Non-Hdl',
                                         'Nrbc %',
                                         'Nrbc Absolute',
                                         'Other',
                                         'P',
                                         'Ph',
                                         'Phosphorus',
                                         'Platelet Count(Plt)',
                                         'Potassium',
                                         'Pr',
                                         'Protein, Total',
                                         'Qrs',
                                         'Qrsd',
                                         'Qt',
                                         'Qtc',
                                         'Rate',
                                         'Rbc',
                                         'Rdw',
                                         'Red Cell Distribution Width(Rdw-Cv)',
                                         'Reverse T3',
                                         'Rheumatoid Factor',
                                         'Rnp Antibodies',
                                         'Sedimentation Rate (Esr)',
                                         'Sedimentation Rate, Automated',
                                         'Serum Iron',
                                         "Sjogren'S Ab, Anti-Ssa",
                                         "Sjogren'S Ab, Anti-Ssb",
                                         'Smith Antibodies',
                                         'Sodium',
                                         'Specific Gravity',
                                         'T',
                                         'T. Chol/Hdl Ratio',
                                         'T3',
                                         'T3 Uptake',
                                         'T4',
                                         'T4,Free(Direct)',
                                         'Testosterone Level',
                                         'Thyroglobulin Antibody',
                                         'Thyroid Peroxidase (Tpo), Ab',
                                         'Thyroxine (T4)',
                                         'Total Iron Binding Capacity (Tibc)',
                                         'Transferrin',
                                         'Transferrin Saturation (Tsat)',
                                         'Triglycerides',
                                         'Triiodothyronine (T3)',
                                         'Triiodothyronine (T3), Free',
                                         'Tsh',
                                         'Uibc',
                                         'Uric Acid',
                                         'Urobilinogen,Semi-Qn',
                                         'Vitamin D 25_Hydroxy',
                                         'Vitamin D, 25-Hydroxy',
                                         'Vldl Cholesterol Cal',
                                         'Wbc',
                                         'Wbc Esterase',
                                         'Wbc Microscopic'])
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

        # 1. Get unique values and sort them alphabetically
        sorted_metrics = sorted(df['Panel'].dropna().unique())

        # 2. Pass the sorted list to the selectbox
        selected_metric = st.selectbox("Select Metric to View", sorted_metrics)
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
