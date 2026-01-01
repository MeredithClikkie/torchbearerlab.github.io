A.   Task 2 Code Description
A small investment company needs to rebalance its equity fund’s holdings, which is comprised of 150 U.S. companies.  The code for the program cleans, groups business IDs by state, runs descriptive statistics for all financial information provided, provides businesses with negative debt-to-equity ratios, and calculates the debt-to-income ratio. This data analysis will provide actionable insights to the fund managers who are looking to rebalance the fund’s holdings and assess risk. This code for Task 2 was executed using Python in IntelliJ IDE and pulled, committed, and pushed to GitLab for version control.
import pandas as pd
import openpyxl as xl

#load workbook and specify columns to exclude unnecessary data
file_path = "/Users/meredithsmith/PycharmProjects/PythonProject/PythonProject/D598PA1/D598_Data_Set.xlsx"
df = pd.read_excel(file_path, usecols=["Business ID", "Business State", "Total Long-term Debt", "Total Equity", "Debt to Equity", "Total Liabilities", "Total Revenue", "Profit Margin"], sheet_name = "1-150 V2")

#check df rows and columns
print(df.head)
This script imports necessary packages and loads the Excel sheet data into the IntelliJ IDE.
Step by step:
	Import the necessary packages pandas and openpyxl
	Load data frame ‘df’from Excel spreadsheet
o	Listing the necessary columns of the data frame (df) eliminates the inclusion of any unnecessary data
#check for duplicate rows
duplicates = df[df.duplicated(keep=False)]
print(duplicates)

#check data types
df['Business State'] = df['Business State'].astype('string')
df['Business State'] = df['Business State'].fillna('').astype('string')
print(df.dtypes)

#correct capitalization in 'Business State' column
df['Business State'] = df['Business State'].apply(lambda x: x.capitalize())
df['Business State'] = df['Business State'].apply(lambda x: x.title())
df = df.apply(lambda col: col.str.strip() if col.dtype == 'object' else col)
df = df.astype({col: 'string' for col in df.select_dtypes(include='object').columns})
df.fillna(" ", inplace=True)
This script cleans data.
Step by step:
	Check and preview any duplicates 
	Convert all object columns to ‘string’ data type (dtype)
o	Fill empty spaces with ‘na’
o	Check data types
	Corrects capitalization errors discovered from print(df.head) in previous code block
	Removes whitespace from string entries across the entire data frame
	Replace all ‘nan’ values with a blank space
	Store and preview the cleaned data frame
#group businesses by states and calculate descriptive stats
df3 = df2.groupby(['Business State']).agg({
'Total Long-term Debt': ['mean', 'median', 'min', 'max'],
'Total Equity': ['mean', 'median', 'min', 'max'],
'Debt to Equity': ['mean', 'median', 'min', 'max'],
'Total Liabilities': ['mean', 'median', 'min', 'max'],
'Total Revenue': ['mean', 'median', 'min', 'max'],
'Profit Margin': ['mean', 'median', 'min', 'max']
})
Step by Step:
	This script groups the cleaned data frame by state 
	 Assigns descriptive statistics to calculate all numerical columns.
#Flatten the multi-index columns
df3.columns = ['_'.join(col).strip() for col in df3.columns.values]
df3 = df3.reset_index()
print(df3)
Step by Step:
	This code flattens hierarchical column names. Example: 
o	(‘Profit Margin’, ‘mean’)) into single level [‘Profit Margin_mean’].
	Reset index moves the index back into the df as a column
	Preview ‘df3’
Output Description:
The new data frame ‘df3’ has 24 columns, 40 rows. [‘Business ID’] is grouped by [‘Business State’] with statistical analysis of each numerical value.
#filter and identify businesses with negative debt-to-equity(DE) ratios
df4 = df2[df2['Debt to Equity']<0][['Business ID', 'Debt to Equity']].copy()
#print(df4)
Step by step:
	Creates new df4
	Filter [‘Business ID’] that have negative [‘Debt to Equity’] ratios
	Preview df4
Output description: 
	7 [‘Business ID’] with negative [‘Debt to Equity’}
#create new column, calculate debt-to-income (DI) ratio, and concatenate it to df2 (cleaned original df)
df5 = df2.copy()
df5['DI_ratio']= df5['Total Long-term Debt']/df5['Total Revenue']
print(df5.columns)
Step by Step:
	Copies df2 and stores to df5
	Creates a new column [‘DI_ratio’] and calculates the debt-to-income ratio 
	 Preview df5 columns 
Output description:
New data frame df5 has 9 columns and 150 rows, concatenating [‘DI_ratio’] with df2.
B.  4 Customized Data Visualizations
(See GitLab link)
C.  Creating Custom Visualizations in Jupyter Notebook
Viz Overview
The following four visualizations, described below, were made using Python in a Jupyter notebook. Matplotlib inline was used to keep static images embedded in the notebook.
The Jupyter notebook is best utilized for development, collaboration, sharing, and even publication of data science results” (VanderPlas, 2022). 
•	Viz 1 
o	divides and color codes positive and negative [‘Debt to Equity’] grouped by [‘Business ID’]
•	Viz 2
o	Bar chart that plots [‘Business_Counts’] grouped by  [‘Business State’]

•	Viz 3
o	shows [‘Debt to Equity_mean’] in descending order and [‘DI_Ratio_mean’]  in a scatter plot with all the businesses grouped by [‘State’]
•	Viz 4 
o	plots the [‘Profit Margin_mean’] in descending order by [‘State’].
Project Code Prep:
#import script
%run -i /Users/meredithsmith/IdeaProjects/D598PA1/D598PA2.py
Step by Step:
	This Jupyter magic command imports Python script and variables from Task 2 code to Jupyter notebook
	It also prints index and lists columns
from D598PA2 import df3, df5, df, df2
%matplotlib inline
import pandas as pd
import numpy as np
Step by Step:
	Imports data frames from Task 2 program
	Imports necessary packages for program
Viz 1 – Negative D/E Ratio by ID with Labeled Markers
Viz Code prep:
#Viz1 Neg and Pos DE by ID
import matplotlib.pyplot as plt

# Sort data
dfDE = df5.copy()
dfDE = df5.sort_values(by='Debt to Equity', ascending=False)

# Split into positive and negative segments
pm_pos = np.where(dfDE['Debt to Equity'] >= 0, dfDE['Debt to Equity'], np.nan)
pm_neg = np.where(dfDE['Debt to Equity'] < 0, dfDE['Debt to Equity'], np.nan)
Step by Step:
	Creates ‘dfDE’ to store sorted ‘df5’ sorted by [‘Debt to Equity’].
	Separates positive and negative [‘Debt to Equity’] values.
# Plot all points
fig, ax = plt.subplots(figsize=(12, 8))

# Plot positive DE in teal
ax.scatter(dfDE['Business ID'], pm_pos,  marker = 'x', color='teal', label='Positive PM')

# Plot negative DE in red
ax.scatter(dfDE['Business ID'], pm_neg, marker='<', color='red', label='Negative PM')

# Round for clean labels
dfDE['Debt to Equity'] = dfDE['Debt to Equity'].round(2)
Step by Step:
	Differentiates positive [‘Debt to Equity’] values associated with its [‘Business ID’] by color coding and labeling.
	Rounds [‘Debt to Equity’] to two decimal places
# Filter negative values
neg_mask = dfDE['Debt to Equity'] < 0
neg_points = dfDE[neg_mask]

# Annotate only negative points
for i in neg_points.index:
    business_id = dfDE.loc[i, 'Business ID']
    equity_val = dfDE.loc[i, 'Debt to Equity']
    label = f"{business_id} ({equity_val})"
    ax.text(business_id, equity_val - 0.5, label, fontsize=8, color='red', ha='center')
Step by Step:
	‘neg_mask’ creates a Boolean series to filter negative [‘Debt to Equity’] values
	‘neg_points’ applies the mask above to return only negative values
	Annotate only negative points
o	Iterates through flagged negative points
o	Retrieves [‘Business ID’] and [‘Debt to Equity’] from ‘dfDE’
o	Places the point label on the plot just below the point
o	Uses red text for the negative points and labels
# Create legend handles manually
import matplotlib.patches as mpatches

handles = [mpatches.Patch(color='red', label=f"{row['Business ID']}: {row['Debt to Equity']:.2f}")
           for _, row in neg_points.iterrows()]
Step by Step:
	Iterates values and labels only ytick markers for negative [‘Debt to Equity’] values with the [‘Business ID’] and negative DE value.
# Layout
ax.set_title("Negative D/E by ID with Labeled Markers")
ax.set_xlabel("Business ID")
ax.set_ylabel("Debt to Equity")
ax.legend(handles=handles, title="IDS with neg D/E", loc='upper right', fontsize=9)
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
Step by step:
	Sets plot title and axes labels
	Creates a legend that prints out the numerical values for [‘Business ID’] and negative [‘Debt to Equity’] for easier accessibility
Viz Description:
This line graph shows [‘Debt to Equity’] in descending order in a scatter plot grouped by [‘Business ID’]. The plot has negative [‘Debt to Equity’] and [‘Business ID’] points labeled in red, as well as a legend to increase readability.
Viz 2 – Business Counts by State Bar Chart
#Viz2 Business Counts by State Bar Chart
df_counts = df5.copy()
df_counts = df5.groupby('Business State').size().reset_index(name='Business_Counts')
#print(df_counts)
plt.figure(figsize=(12, 8))
plt.style.use('seaborn-v0_8-whitegrid')
Step by Step:
	Creates ‘df_counts’ from copy of ‘df5’
o	Groups by and counts [‘Business State’]
o	Creates new column [‘Business_Counts’]
	Preview ‘df_counts’
	Creates canvas size
	Creates canvas style
# Bar plot
plt.bar(df_counts['Business State'], df_counts['Business_Counts'], color='steelblue', edgecolor='black')

plt.title('Business Counts by State')
plt.ylabel('Business Count')
plt.xticks(rotation=65)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
Step by Step:
	Creates a bar chart to show [‘Business_Counts’] grouped by [‘Business State’]
o	Assigns bar color and edgecolor
	Creates bar chart title, label for y axis, rotates x ticks for accessibility, and horizontal grid
# Annotate each bar with its count
for idx, row in df_counts.iterrows():
    plt.text(row['Business State'], row['Business_Counts'] +0.25,
             str(row['Business_Counts']),
             ha='center', fontsize=14, color='darkred')

plt.show()
Step by Step:
	Annotates each bar with [‘Business_Counts’]
Viz Description:
This shows how many businesses are in each state with a bar chart and labeled [‘Business_Counts’] atop each bar. 
Viz 3 – Average D/E and DI Ratios by State
Code prep:
#Viz3 code and plot begins here#####################################
from matplotlib import pyplot as plt

#Code prep
#Sort by Business State to ensure proper plotting
dfState = df5.copy()
dfState = df5.sort_values('Business State')

# Dictionary mapping full names to abbreviations
state_abbrev = {
'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE','Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID',
'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN','Mississippi': 'MS','Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV',
'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY','North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK','Oregon': 'OR, 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC','South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'Washington D.C.': 'DC', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}

#Replace full names with abbreviations in 'Business State' column
dfState['State'] = df5['Business State'].map(state_abbrev)
dfState['State'] = dfState['State'].astype('string')
dfState=dfState['State'].astype('string')
dfState.fillna(" ", inplace=True)
print(dfState)
Step by Step:
	‘dfState’ is created from a copy of ‘df5’ to store the state abbreviations of each [‘Business State’].
	Converts object value to string by (.astype(‘string’))
	Fills ‘na’ values with blank spaces
	Previews ‘dfState’
	‘dfState’ has 1 column, 150 rows
df_combo2 = pd.concat([dfState, df5], axis=1)
df_new = df_combo2.copy()
df_new = df_combo2.groupby(['State']).agg({
    'Total Long-term Debt': ['mean'],
    'Total Equity': ['mean'],
    'Debt to Equity': ['mean'],
    'Total Liabilities': ['mean'],
    'Total Revenue': ['mean'],
    'Profit Margin': ['mean'],
    'DI_ratio': ['mean']
})
#Flatten the MultiIndex Columns
df_new.columns = ['_'.join(col).strip() for col in df_new.columns.values]
df_new = df_new.reset_index()
print(df_new)
Step by Step:
	Concatenates state abbreviation data frame ‘dfState’ with df5
o	‘df5’ has 9 columns, 150 rows
o	‘dfState’ has 1 column, 150 rows
o	‘df_combo2’ has 10 columns, 150 rows
	‘df_new’ is created from a copy of ‘df_combo2’ which concatenates ‘dfState’ to ‘df5’ to store the mean of each numerical value grouped by [‘State’]
o	[‘State’] is a created column from a dictionary of state abbreviations for easier graphical representation purposes. 
	‘df_new’ multi-index columns are flattened
	‘df_new’ has 8 columns and 40 rows, stores the means of all numerical data of each [‘State’]
df_sorted1 = df_new.copy()
df_sorted1 = df_new.sort_values(by='Debt to Equity_mean', ascending=False)
fig, ax = plt.subplots(figsize=(12,6))
Step by Step:
	‘df_sorted1’ is created from a copy of ‘df_new’ 
	 ‘df_sorted1’ is sorted by [‘Debt to Equity_mean’], the product of the flattened multi-index columns, and is ordered from largest to smallest
	‘fig’ is the container/canvas; ‘ax’ is the individual plot area
	(figsize=12,6)) sets the canvas to 12 inches wide x 6 inches tall
ax.scatter(df_sorted1['State'].astype(str), df_sorted1['Debt to Equity_mean'], label='DE', color='teal', marker ='x')
ax.scatter(df_sorted1['State'].astype(str), df_sorted1['DI_Ratio_mean'], label='DI', color = 'blue', marker ='o')
Step by Step:
	This script layers two scatter plots on one axis to visualize both [‘Debt to Equity_mean’] and [‘DI_Ratio_mean’] by [‘State’]
	Both axes are sorted by [‘State’], which is converted to a string for categorical plotting
	Both axes are assigned a label, color, and marker
#Labels and Title
ax.set_xlabel('State')
ax.set_ylabel('Avg DE and DI')
plt.title('Avg DE and DI by State')
plt.xticks(rotation=70,)
ax.legend(loc='upper right')
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()
Step by step:
	Sets x and y axis labels
	Creates plot title
	Xtick labels, rotated 70 degrees for accessibility
	Creates legend and position it in the upper right of canvas
	Creates a horizontal grid, line style and marker size
	Shows plot
Viz Description:
The outcome of this code presents a scatter plot with two lines sorted by descending [‘Debt to Equity_mean’] values. The [‘Debt to Equity-mean’] line is colored with teal ‘x’ markers; the [‘DI_Ratio_mean’] has blue ‘o’ markers. The markers indicate the corresponding value for each [‘State’]. This allows the stakeholders to visualize which states have the highest average DE and DI ratios, as well as the lowest. This provides insights into the riskier states that have businesses that need to be rebalanced due to low DE or DI. 
Viz 4 – Average Profit Margin by State
# Viz 4 Average Profit Margin by State 
dfPM = df_new.sort_values(by='Profit Margin_mean)

# Split into positive and negative segments
pm_pos = np.where(dfPM['Profit Margin_mean'] >= 0, dfPM['Profit Margin_mean'], np.nan)
pm_neg = np.where(dfPM['Profit Margin_mean'] < 0, dfPM['Profit Margin_mean'], np.nan)
Step by Step:
	creates ‘dfPM’
	 sort values by [‘Profit Margin_mean’] in ascending order
	‘pm_pos’ and ‘pm_neg’ splits positive and negative segments by [‘Profit Margin_mean’]
# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot positive profit margins in teal
ax.plot(dfPM['State'], pm_pos, marker='o', color='teal', label='Positive PM')

# Plot negative profit margins in red
ax.plot(dfPM['State'], pm_neg, marker='x', color='red', label='Negative PM')
	See Viz 1 for similar descriptions
# Labels and layout
ax.set_title("Average Profit Margin by State")
ax.set_xlabel("State")
ax.set_ylabel("Profit Margin (%)")
ax.legend(loc='lower right')
plt.xticks(rotation=45)
plt.tight_layout()
ax.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.show()
	See Viz 1 for similar explanation
Viz 4 Description:
This visualization provides insights into the states that have high or low [‘Profit Margin_mean’]. The value in splitting positive and negative segments is apparent in this visualization, as it clearly shows Virginia has lost a lot of money in the last quarter.
Conclusion
	This code turned an 8-column, 150-row Excel spreadsheet into a dozen different data frames to provide insights to the fund managers of the small investment company. Four visualizations were created to show the stakeholders which states and businesses are at high risk. This analysis helps stakeholders to make decisions on how to rebalance their funds for the next quarter. 
	Each visualization measures how the individual businesses or states compare to the rest. The insights of how they did or did not stand out were noticed in each viz when plotting the businesses’ debt-to-equity and debt-to-income ratios, and profit margins. For example, Virginia has a negative average profit margin of -24.30, and Texas has three businesses in the top five highest DI ratios, however, there are 14 businesses in Texas which is to be factored in before making a conclusion. The business count bar chart plots the number of businesses per state so that the stakeholders will not make a skewed judgment based on state results alone. 
















D.  References
Vanderplas, Jake. (2022). Python Data Science Handbook. Sebastopol, CA: O’Reilly Media, 2022. https://research.ebsco.com/linkprocessor/plink?id=784a5973-0f83-38c2-baff-ec6631b66091. Accessed: September 7, 2025.

<img width="468" height="638" alt="image" src="https://github.com/user-attachments/assets/ad9d9e32-c71c-4309-8bae-43e629deb516" />
