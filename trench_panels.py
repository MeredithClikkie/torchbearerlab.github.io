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
        metric = st.selectbox("Panel", [[['Cholesterol, Total',
  'HDL',
  'LDL',
  'Non-HDL',
  'Triglycerides',
  '% Free + Weak',
  'Albumin',
  'Anion Gap',
  'Blood Urea Nitrogen (BUN)',
  'Chloride',
  'CO2',
  'Creatinine',
  'CRP',
  'CRP (high sensitivity)',
  'Cyclic Citruillinated Pep IgG CP',
  'Estrogen Total',
  'Follicle-stimulating Hormone (FSH)',
  'Free/Weakly Bound',
  'Glucose',
  'Hematocrit',
  'Hemoglobin',
  'Luteinizing Hormone (LH)',
  'Lyme Disease AB Total Antibody with Reflex',
  'Lymphocytes %',
  'Lymphocytes Absolute',
  'MCH',
  'MCHC',
  'MCV',
  'MPV',
  'nRBC %',
  'Platelet Count(Plt)',
  'Potassium',
  'RBC ',
  'Red Cell Distribution Width(RDW-CV)',
  'Sodium',
  'Testosterone Level',
  'TSH',
  'Vitamin D 25_Hydroxy',
  'WBC',
  'COVID ',
  'Ketones POL',
  'Cholesterol, Total',
  'Estimated Average Glucose',
  'HDL',
  'Hemoglobin A1C ',
  'LDL',
  'Non-HDL',
  'Triglycerides',
  'Anion Gap',
  'Basophils %',
  'Basophils Absolute',
  'Blood Urea Nitrogen (BUN)',
  'Calcium Level Total',
  'Chloride',
  'Cholesterol, Total',
  'CO2',
  'Creatinine',
  'eGFR',
  'Eosinophils %',
  'Eosinophils Absolute',
  'Glucose',
  'HDL',
  'Hematocrit',
  'Hemoglobin',
  'LDL',
  'Lymphocytes %',
  'Lymphocytes Absolute',
  'MCH',
  'MCHC',
  'MCV',
  'Monocytes %',
  'Monocytes Absolute',
  'MPV',
  'Neutrophils %',
  'Neutrophils Absolute',
  'Non-HDL',
  'nRBC %',
  'nRBC Absolute',
  'Platelet Count(Plt)',
  'Potassium',
  'RBC ',
  'Red Cell Distribution Width(RDW-CV)',
  'Sodium',
  'Triglycerides',
  'TSH',
  'WBC',
  'Alanine Aminotransferase',
  'Albumin',
  'Alk Phos Total',
  'Anion Gap',
  'Aspartate Aminotransferase(AST)',
  'Basophils %',
  'Basophils Absolute',
  'Bilirubin Total',
  'Blood Urea Nitrogen (BUN)',
  'Calcium Level Total',
  'Chloride',
  'Cholesterol, Total',
  'CO2',
  'Creatinine',
  'eGFR',
  'Eosinophils %',
  'Eosinophils Absolute',
  'Estimated Average Glucose',
  'Glucose',
  'HDL',
  'Hematocrit',
  'Hemoglobin',
  'Hemoglobin A1C ',
  'LDL',
  'Lymphocytes %',
  'Lymphocytes Absolute',
  'MCH',
  'MCHC',
  'MCV',
  'Monocytes %',
  'Monocytes Absolute',
  'MPV',
  'Neutrophils %',
  'Neutrophils Absolute',
  'Non-HDL',
  'nRBC %',
  'nRBC Absolute',
  'Platelet Count(Plt)',
  'Potassium',
  'Protein, Total',
  'RBC ',
  'Red Cell Distribution Width(RDW-CV)',
  'Sedimentation Rate (ESR)',
  'Sodium',
  'Triglycerides',
  'TSH',
  'Vitamin D 25_Hydroxy',
  'WBC',
  'Alanine Aminotransferase',
  'Albumin',
  'Alk Phos Total',
  'Anion Gap',
  'Aspartate Aminotransferase(AST)',
  'Basophils %',
  'Basophils Absolute',
  'Bilirubin Total',
  'Blood Urea Nitrogen (BUN)',
  'Calcium Level Total',
  'Chloride',
  'Cholesterol, Total',
  'CO2',
  'Creatinine',
  'eGFR',
  'Eosinophils %',
  'Eosinophils Absolute',
  'Estimated Average Glucose',
  'Glucose',
  'HDL',
  'Hematocrit',
  'Hemoglobin',
  'Hemoglobin A1C ',
  'LDL',
  'Lymphocytes %',
  'Lymphocytes Absolute',
  'MCH',
  'MCHC',
  'MCV',
  'Monocytes %',
  'Monocytes Absolute',
  'MPV',
  'Neutrophils %',
  'Neutrophils Absolute',
  'Non-HDL',
  'nRBC %',
  'nRBC Absolute',
  'Platelet Count(Plt)',
  'Potassium',
  'Protein, Total',
  'RBC ',
  'Red Cell Distribution Width(RDW-CV)',
  'Sodium',
  'Triglycerides',
  'TSH',
  'Vitamin D 25_Hydroxy',
  'WBC',
  'Magnesium',
  'P',
  'PR',
  'QRS ',
  'QRSD  ',
  'QT ',
  'QTc ',
  'Rate ',
  'T ',
  'Ferritin',
  'Serum Iron',
  'Total Iron Binding Capacity (TIBC)',
  'Transferrin',
  'Transferrin Saturation (TSAT)',
  'C3 Complement ',
  'C4 Complement ',
  'CK ',
  'Rheumatoid Factor ',
  'RNP Antibodies ',
  'Sedimentation Rate, Automated ',
  "Sjogren's Ab, Anti-SSA",
  "Sjogren's Ab, Anti-SSB",
  'Smith Antibodies ',
  'Uric Acid ',
  'Albumin',
  'Alk Phos Total',
  'ALT(SGPT)',
  'Anti - CCP Ab, IgG/IgA ',
  'Anti - DNA Antibody, Double',
  'Aspartate Aminotransferase(AST)',
  'Basophils %',
  'Basophils Absolute',
  'Bilirubin Direct',
  'Bilirubin Total',
  'Creatinine',
  'CRP',
  'eGFR',
  'Eosinophils %',
  'Eosinophils Absolute',
  'Hematocrit',
  'Hemoglobin',
  'Immature Granulocytes (Abs)',
  'Immature Granulocytes (Abs)',
  'Lymphocytes %',
  'Lymphocytes Absolute',
  'MCH',
  'MCHC',
  'MCV',
  'Monocytes %',
  'Monocytes Absolute',
  'Neutrophils %',
  'Neutrophils Absolute',
  'Platelet Count(Plt)',
  'Protein, Total',
  'RBC ',
  'RDW',
  'TSH',
  'WBC',
  '25-OH Vitamin D3',
  'Albumin',
  'Alk Phos Total',
  'ALT (SGPT)',
  'ALT (SGPT)',
  'AST (SGOT)',
  'AST (SGOT)',
  'Basophils %',
  'Basophils Absolute',
  'Bilirubin Total',
  'Bilirubin Total',
  'Blood Urea Nitrogen (BUN)',
  'BUN/Creatinine Ratio',
  'Calcium Level Total',
  'Chloride',
  'Cholesterol, Total',
  'Cholesterol/HDL Ratio',
  'CO2',
  'Cortisol rhythm, total',
  'Creatinine ',
  'CRP (high sensitivity)',
  'eGFR ',
  'Eosinophils %',
  'Eosinophils %',
  'Eosinophils Absolute',
  'Epithelial Cells (non renal)',
  'Ferritin',
  'Fibrinogen Activity',
  'Free T3',
  'Free T4',
  'Free Thyroxine Index',
  'FTI',
  'GGT',
  'Globulin, Total',
  'Glucose',
  'HCT ',
  'HDL ',
  'Hematocrit',
  'Hemoglobin',
  'Hemoglobin A1c ',
  'HGB ',
  'Homocysteine',
  'Immature Granulocytes (Abs)',
  'Immature Granulocytes (Abs)',
  'Iron',
  'Total Iron Binding Capacity (TIBC)',
  'Iron Saturation',
  'LDH',
  'LDL',
  'Lymphocytes %',
  'Lymphocytes %',
  'Lymphocytes Absolute',
  'Magnesium',
  'MCH',
  'MCHC',
  'MCV ',
  'Monocytes %',
  'Monocytes Absolute',
  'Neutrophils %',
  'Neutrophils Absolute',
  'pH',
  'Phosphorus',
  'Platelet Count(Plt)',
  'Potassium',
  'Protein, Total',
  'Protein, Total',
  'Protein, Total',
  'RBC',
  'RDW',
  'Reverse T3',
  'Serum Iron',
  'Sodium ',
  'Specific Gravity',
  'T. Chol/HDL Ratio',
  'T3',
  'T3 Uptake',
  'T4',
  'T4,Free(Direct)',
  'Thyroglobulin Antibody',
  'Thyroid Peroxidase (TPO), Ab',
  'Thyroxine (T4)',
  'Total Iron Binding Capacity (TIBC)',
  'Triglycerides',
  'Triiodothyronine (T3)',
  'Triiodothyronine (T3), Free',
  'TSH',
  'UIBC',
  'Uric Acid ',
  'Urobilinogen,Semi-Qn',
  'Vitamin D, 25-Hydroxy',
  'VLDL Cholesterol Cal',
  'WBC',
  'WBC Esterase',
  'WBC Microscopic', "Other"]]])
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
