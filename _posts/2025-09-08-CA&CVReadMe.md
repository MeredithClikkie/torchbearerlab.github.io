# M.SmithGitLabPA3Viz

## Name
M.SmithD598PA3Viz.ipynb

## Files
This project includes:
Code Analysis and Custom Visualization word doc [D598PA3.docx](https://gitlab.com/wgu-gitlab-environment/student-repos/msmit256/d598-analytics-programming/-/blob/PA3Viz/D598PA3.docx?ref_type=heads)
Import script from Task 2 code [PA2.py](https://gitlab.com/wgu-gitlab-environment/student-repos/msmit256/d598-analytics-programming/-/blob/PA3Viz/D598PA3.docx?ref_type=heads)
Create Jupyter notebook [PA3Viz.ipynb](https://gitlab.com/wgu-gitlab-environment/student-repos/msmit256/d598-analytics-programming/-/blob/PA3Viz/D598PA3.docx?ref_type=heads) file to create custom visualizations
Data for code comes from data set ['D598_Data_Set.xlsx'](https://gitlab.com/wgu-gitlab-environment/student-repos/msmit256/d598-analytics-programming/-/blob/PA3Viz/D598PA3.docx?ref_type=heads) from this repository.

## Description
This project provides four visualizations for the analysis of the performance of the 150 companies that make up an equity fund for a small investment company.
The outcome of this notebook shows:
-Viz 1: divides and color codes positive and negative [‘Debt to Equity’] grouped by [‘Business ID’]
-Viz 2: Bar chart that plots [‘Business_Counts’] grouped by  [‘Business State’]
-Viz 3: shows [‘Debt to Equity_mean’] in descending order and [‘DI_Ratio_mean’]  in a scatter plot with all the businesses grouped by [‘State’]
-Viz 4: plots the [‘Profit Margin_mean’] in descending order by [‘State’].

The purpose of the code from Task 2 is to provide
- descriptive stats for the businesses ('Business ID') grouped by states ('Business State')
- highlights the businesses that have negative debt-to-equity ratios (DE)
- an additional column to the original data set that provides the debt-to-income ratio ('DI_Ratio') for each business

## Visuals
See above for brief description of visuals and check out PA3Viz.ipynb for code and visualizations

## Installation
This project was created in Jupyter notebook with Python in the IntelliJ IDEA IDE, and the files were uploaded to GitLab.
The IntelliJ IDEA IDE is fully compatible with GitLab, and files can also easily be sent from the IDE via the 'Git' tab located on the dock/taskbar.

## Usage
Here is an example of a line of code from the program with the resulting output:

#filter out businesses with negative debt-to-equity(DE) ratios
'''Python
df4 = df[df['Debt to Equity']< 0][['Business ID', Debt to Equity']]
print(df4)
'''
Output:
[40 rows x 24 columns]
'''python
Business ID  Debt to Equity
18   9.345620e+08       -2.370953
57   8.343652e+09       -0.798921
87   9.323722e+09       -1.374036
109  1.091983e+10       -0.557949
117  1.124524e+10       -0.269484
142  1.453593e+10       -4.283552
143  1.463972e+10       -0.014343
'''
#This returns the row number, the 'Business ID' of the businesses that have negative DE ratios.

While cleaning data, the 'Business State' had a typo: 'MInnesota'.
The following line of code addresses this issue for all states:

#correct capitalization in 'Business State' column
'''python
df['Business State'] = df['Business State'].apply(lambda x: x.capitalize())
print(df2)
'''

#psuedocode
>>>
START
IMPORT data from “D598 Data Set” as df
CHECK for duplicate rows in df
IF duplicate rows exist THEN
delete duplicates and store as df2
ELSE
store df as df2
GROUP each ‘Business ID' by 'Business State'
RUN descriptive statistics (mean, median, min, and max) for all numeric variables by ‘Business State’
STORE this result as df3
FILTER df3 to identify ‘Business ID’ with negative debt-to-equity (DE) ratios
IF negative DE THEN
store as df4
ELSE
leave in df2
CALCULATE the debt-to-income ratio for each ‘Business ID’ ('DI_Ratio' = ‘Long-term Debt’/’Total Revenue’)
STORE as df5
CONCATENATE this df5 to the original cleaned data frame (df2)
END
>>>

<iframe 
  src="https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:3a46d370-41df-4320-856c-307f3fa66185" 
  width="100%" 
  height="600px" 
  style="border: none;">
</iframe>

## Support
There are many resources available for help. If using IntelliJ IDEA, go to https://www.jetbrains.com/idea/ for support.
To get help for GitLab, please see the help option at the bottom of the left navigation sidebar.
<div class="gist-container">
  <script src="https://gist.github.com/meredithclikkie/6b50a70871e9b955247a3dcc276a5930<img width="596" height="38" alt="image" src="https://github.com/user-attachments/assets/e6e3848a-49d6-4af6-8052-31bf3fe46003" />
.js"></script>
</div>
