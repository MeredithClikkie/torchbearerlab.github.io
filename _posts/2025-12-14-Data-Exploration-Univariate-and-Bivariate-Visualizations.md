Univariate and Bivariate Visualizations

This report presents an analysis of the patterns and correlations in a health insurance dataset comprising 1,338 records to investigate the impact of demographic and lifestyle factors, such as Age, BMI, and Smoking status, and the resulting Insurance Charge. This project examines the variables using univariate and bivariate visualizations, descriptive statistics, as well as parametric and non-parametric testing. In alignment with standard regression analysis, this project seeks to test the Null Hypothesis (H0)that there is no statistically significant relationship between the selected independent variables and medical charges.

PartI: Univariate and Bivariate Statistical Analysis and Visualization

A. 1. The Univariate Variables and Visualizations of ‘Age’, ‘Charges’, ‘BMI_Category’, & ‘SmokerQuantitative Variable 1 — Univariate Analysis of ‘Charges’

Press enter or click to view image in full size
![Figure 1.]({{/torchbearerlab}}/assets/images/D599t2viz1.jpg)
Figure 1. Charges: Histogram with KDE curve, Boxplot, & Q-Q Plot — Interpretation: Charges have a right-skewed distribution (positive skew), heavy‑tailed, meaning the mean is pulled higher than the median.

Quantitative Variable — Univariate Analysis: ‘Age’

Press enter or click to view image in full size

Figure 2. Age: Histogram with KDE curve, Boxplot, and Q-Q Plot — Interpretation: Age is almost perfectly symmetric (skew ≈ 0) but strongly platykurtic (kurtosis ≈ –1.24), meaning it has a flat, light‑tailed distribution rather than a normal bell curve.

Qualitative Variables Chosen: ‘BMI_Category (from BMI) and ‘Smoker’

Qualitative Variable 1 — Univariate Analysis: ‘BMI_Category’

Press enter or click to view image in full size

Figure 3. BMI_Category: Countplot, Pie Chart, and Summary- Interpretation: Most density around Class1_Obese, and secondarily Overweight

Qualitative Variable 2 — Univariate Analysis: ‘Smoker’

Press enter or click to view image in full size

and non-smokers.

2. Bivariate Visualization

Variable Mapping Table:

Selected VariableBivariate Pair 1Bivariate Pair 2Bivariate Pair 3ChargesAge vs ChargesCharges vs. SmokerBMI_Cat vs ChargesAgeAge vs ChargesAge vs BMI_CategoryBMI_CategoryBMI_CatBMI_Cat vs ChargesSmokerCharges vs SmokerAge vs SmokerBMI_Category vs Smoker

Figure 5. Mapping Table for Bivariate Variables — To ensure two visualizations per each variable chosen in A1

Bivariate Visualization: ‘Age’ vs ‘Charges’

Press enter or click to view image in full size

Figure 6. Age vs. Medical Charges: 2D KDE and Scatter — Analysis: Three Distinct Risk Tiers: The 2D KDE plot clearly shows three horizontal density tunnels. This indicates that while age is a factor, the population is divided into three distinct risk groups based on other variables (likely smoking and BMI): Youth Concentration: The brightest density area at the bottom left indicates that the majority of the dataset consists of younger individuals (18–30) in the lowest-cost tier.

Bivariate Visualization: ‘Smoker’ Status vs ‘Charges’

Press enter or click to view image in full size

Figure 7. Smoker Status vs. Charges: Violin and KDE — Analysis: The Violin Plot shows that non-smokers are tightly clustered at the bottom of the scale, while smokers have a much higher and broader distribution of charges; Bimodal Smoking Costs: The KDE Plot for smokers (blue) shows two distinct peaks. This suggests smokers are split into two groups: “healthier” smokers and a high-risk group (likely those with high BMI) whose charges frequently exceed $40,000.

Bivariate Visualization: ‘Age’ vs ‘Smoker’ Status

Press enter or click to view image in full size

Figure 8. Age vs. Smoker Status: Violin and KDE — Analysis: Identical Distributions — The Split Violin Plot and KDE Plot show how the age distributions for both smokers and non-smokers are almost identical; No Age Bias: Both groups show a wide range of ages (roughly 18 to 70) with similar peaks around age 20. This is an important finding because it confirms that smoking status is independent of age in this dataset — meaning you don’t have a “young smoker” or “old non-smoker” bias.

Bivariate Visualization: ‘BMI_Category’ vs Charges

Press enter or click to view image in full size

Figure 9. The Impact of BMI on Medical Costs: Bar and box plots — Analysis: A non-linear relationship between weight and cost: Average Charges Increase with BMI: There is a visible step-up in average charges as you move from “Under” to ‘C1_Obese’ and ‘C2_Obese’ categories.The “Obese” Outlier Effect: While the median charges for the “Obese” categories are higher, the boxplot reveals a massive amount of high-cost outliers (reaching $40–$60k). This suggests that high BMI itself isn’t the only driver.

Bivariate Visualization: ‘BMI_Category’ vs ‘Smoker’ Status

Press enter or click to view image in full size

Figure 10. Obesity and Smoking Intersection: Count Plot and Heatmap — Show that while there are fewer smokers than non-smokers overall, there is a significant population of Obese Smokers. This intersection is where the highest charges in the dataset occur.

B. Complete the following using the attached “Health Insurance Dataset” and R or Python:

Provide the descriptive statistics for all quantitative variables selected in the dataset.
Quantitative Variables:

AgeBMIChargescount1,3381,3381,338mean3931$13,270.42std146$12,110.01min1815$1,121.8725%2726$4,740.2950%3930$9,382.0375%5135$16,639.91max6453$63,770.43

Figure 11. Descriptive Statistics of Selected Quantitative Variables

2. Provide the Descriptive Statistics for all qualitative variables

Qualitative Variables:

CategoryVariableFrequencyPercentage9Class1_ObeseBMI_Category39729.67%10Class2_ObeseBMI_Category22616.89%11Class3_ObeseBMI_Category936.95%16NormalBMI_Category22116.52%19OverweightBMI_Category38028.40%22UnderweightBMI_Category211.57%6ALevel1128.37%7BLevel26419.73%8CLevel42731.91%12DLevel34826.01%13ELevel18713.98%17NortheastRegion32424.22%18NorthwestRegion32524.29%20SoutheastRegion36427.20%21SouthwestRegion32524.29%14FemaleSex66249.48%15MaleSex67650.52%23noSmoker106479.52%24yesSmoker27420.48%

Figure 12. Descriptive Statistics of Selected Qualitative Variables

Part II. Parametric Statistical Testing

C. Real-world Organizational Issue Description

1. Research Question:

To what extent do smoking status, BMI, and age significantly predict annual medical charges among policyholders, and which factor has the greatest impact on those charges?

D. Analyze the dataset by doing the following:

1. Parametric Statistical Test Chosen: Ordinary Least Squares Regression (OLS)

2. Dataset Variables: ‘BMI,’ ‘Age,’ ‘Smoker,’ and ‘Charges’

3. Why Ordinary Least Squares Regression(OLS) with Robust Standard Errors (SE)?

I selected Ordinary Least Squares (OLS) regression based on variables, ‘BMI’, ‘Age’, ‘Smoker’, and ‘Charges’ because it provides a direct, interpretable measure of how smoking status, BMI, and age impact annual medical charges. This approach is uniquely suited for health insurance pricing research, as it converts complex predictors into quantifiable, financially meaningful explanations of cost drivers, while providing robust evaluation metrics such as R-squared and RMSE (Bruce & Bruce, 2017).

The research design aligns with the core assumptions of OLS: linearity, independent errors, and approximately normal residuals (Rajaretnam, 2016). These conditions are met to a defensible degree within this dataset: Normality — while ‘Charges’ are right-skewed and ‘Age’ and ‘BMI’ are not perfectly normal, the moderate sample size ensures the residuals remain roughly normal and; Stability — No extreme outliers dominate the results, and the variance is not severely unequal. Taken together, these factors make OLS a robust choice for the hypothesis testing and relationship analysis required to evaluate insurance charges (Waples, 2025).

Standard OLS assumes homoskedasticity, or constant error variance. However, medical charges are notoriously high-variance and often exhibit heteroskedasticity — where the spread of charges increases alongside predictors like BMI or Age (Waples, 2025). Without correction, standard errors can be biased, potentially leading to “false significance” or Type I errors.

To protect the integrity of the findings, I employed the HC3 estimator for robust standard errors. HC3 is an advanced jackknife estimator designed to: Correct for unequal variance in the residuals and; Adjust for high-leverage observations, ensuring that a few influential data points do not distort the reliability of p-values. This choice aligns with modern statistical best practices, providing the most accurate and conservative inference for health cost modeling (Pinzon, 2022).

4. Null and Alternative Hypotheses: Null Hypothesis (H0): There is no statistically significant relationship between the independent variables (BMI, age, and smoking status) and the dependent variable (medical charges); the regression coefficients for these predictors are equal to zero. Alternative Hypothesis(H1): There is a statistically significant relationship between at least one of the independent variables (BMI, age, or smoking status) and the dependent variable (medical charges); at least one regression coefficient is not equal to zero.

5. Error-free Code in Python Calculations

Press enter or click to view image in full size

Figure 13: Screenshot of OLS with SE calculation code exported to HTML .

OLS with Robust SE Output and Results

Press enter or click to view image in full size

Figure 14. OLS Regression Results from PyCharm

E. OLS with Robust SE Test Results The p-value of the regression model (1.48e-292), is essentially zero. This confirms that the model is statistically significant overall. With R-squared explaining approximately 75% of the variation in medical charges, this indicates strong predictive performance for real-world health‑cost data. Smoking status is the dominant cost driver, with smokers incurring an estimated $23,800 more in charges than non‑smokers, controlling for BMI and age. BMI and age also contribute meaningfully, with each additional BMI point associated with $323 higher charges and each additional year of age associated with $260 higher charges.

Because the residual diagnostics indicated heteroscedasticity and non‑normality, the model was refit using robust standard errors, ensuring more reliable confidence intervals and hypothesis tests (Bruce & Bruce, 2017). As exhibited in Figure 12 above, the coefficients remain unchanged across models, confirming that the underlying relationships are stable. However, the robust standard errors are larger, particularly for the smoking variable, reflecting the heteroscedasticity observed in the residual diagnostics. This widens the confidence intervals and produces more conservative hypothesis tests. Despite this adjustment, all predictors remain highly significant, indicating that the model’s conclusions are trustworthy.

More from the results:

Durbin-Watson (2.026): A value near 2.0 suggests no autocorrelation in the residuals, which is a good sign that the observations are independent.
Skew (1.213) & Kurtosis (5.618): These indicate that the residuals (errors) are not perfectly normally distributed; they are heavy-tailed. This is common in insurance data, where a small number of individuals have extremely high costs. Because of HC3, the model is robust against this.
RMSE (6,083.21): On average, the model’s predictions are off by about $6,083. Given that some charges exceed $50,000, this is a respectable margin of error. (Bruce & Bruce, 2017).
Null Hypothesis (H0): Rejected. — There is no statistically significant relationship between the independent variables (BMI, age, and smoking status) and the dependent variable (medical charges); the regression coefficients for these predictors are equal to zero.

Alternative Hypothesis(H1): Accepted — There is a statistically significant relationship between at least one of the independent variables (BMI, age, or smoking status) and the dependent variable (medical charges); at least one regression coefficient is not equal to zero.

Press enter or click to view image in full size

confirms that HC3 Robust Standard Errors are essential. This adjustment allows the model to remain a “defensible modeling choice” despite the complex, skewed nature of medical cost data (Waples, 2025).

Become a member
2. Answer to Research Question: Given the Rejection of the Null Hypothesis

Given the rejection of the H0, and the discussion of the regression results above, ‘BMI’, ‘Age’, and ‘Smoker’ status together predict individual health insurance charges with a high degree of accuracy. The model explains approximately 75% of the variation in charges, indicating that these predictors collectively provide a strong and reliable estimate of costs. All predictors within the model demonstrated statistical significance with p-values far below the threshold, at near 0. In alignment with standard regression framing, a significant predictive relationship exists between the identified lifestyle factors and insurance costs. While the diagnostics revealed some skewness in the residuals — suggesting the data is not perfectly normal — the robust F-statistic and narrow confidence intervals confirm that the model has strong explanatory power for organizational risk assessment.

3. How Stakeholders Benefit From OLS Testing Method

OLS regression transforms raw cost data into clear, quantifiable insights that support financial, operational, and strategic decisions. It provides financial predictability by showing exactly how risk factors drive costs — for example, smoking adds roughly $23,800, and each additional year of age adds about $260 — allowing actuaries to price premiums based on real risk and stabilize financial planning. With an R² of 0.75, OLS explains most of the variation in charges, giving leadership clarity on which factors, such as age, BMI, and smoking, have the greatest impact and enabling targeted wellness investments. Its statistically rigorous outputs, including a high F-statistic and near-zero p-values, make policy decisions, such as surcharges or discounts, defensible and reduce regulatory or reputational risk. Finally, OLS diagnostics highlight gaps or missing variables, helping stakeholders refine models, capture nonlinear effects, and strengthen long-term forecasting and data strategy.

F. Parametric Statistical Testing Summary

1. Recommended Course of Action

Regression analysis provides a clear framework for risk segmentation and pricing by categorizing customers into tiers based on cost drivers. High-risk individuals, such as smokers who average an additional $23,800 in charges, can be distinguished from moderate-risk groups like those with high BMI or older age, while lower-risk tiers include non-smokers with healthy BMI. Premium structures and reserve allocations can then be adjusted accordingly to ensure fairness and transparency.

Targeted wellness programs should prioritize smoking cessation initiatives, given smoking is the single largest cost driver, while also developing BMI management strategies such as nutrition counseling and fitness subsidies to reduce long-term costs. Communicating these connections clearly to employees and customers empowers them to understand how lifestyle changes directly reduce charges.

Effective stakeholder communication is essential: executives should be shown that smoking is the most actionable cost driver, finance teams can use RMSE to set realistic error margins in forecasts, and employees and customers should receive transparent education on how age, BMI, and smoking affect charges. In summary, the findings confirm that smoking, BMI, and age are strong predictors of charges. The recommended course of action is to segment risk, invest in targeted wellness programs, document compliance, and continuously refine the model.

2. Limitations

OLS regression effectively demonstrates that ‘Smoker’ status, ‘BMI,’ and ‘Age’ are independent predictors of the dependent variable, medical expenses; however, it has limitations. The errors aren’t perfectly normal, so extreme cases may make confidence intervals less reliable. It also assumes constant variance, linearity, and independence — assumptions that may not hold if, for example, smoking interacts with age. Outliers can skew the results, and the model may overlook other important factors, such as comorbidities or income. Because it’s based on a single dataset at a single point in time, it can’t capture trends or causal changes. Finally, while R² ≈ 0.75 indicates that the three independent predictors account for 75% of the variation of costs, approximately 25% of the variation remains unexplained. In short, OLS is best suited for identifying significant cost drivers and informing strategy, rather than predicting exact charges for individuals. (Bruce & Bruce, 2017)

Part III: Nonparametric Statistical Testing

G. Real-world Organizational Issue Description

1. Research Question

Is there a statistically significant difference in the median annual medical charges between policyholders who are smokers and those who are non-smokers?

H. Analysis

1. Nonparametric Statistical Test: Mann–Whitney U

2. Dataset Variables: ‘Charges’, ‘Smoker’

3. Why Mann-Whitney U Test?

The Mann–Whitney U (MWU) test is an appropriate nonparametric method because it evaluates differences based on the ranks of the data rather than the raw values. By relying on ranks, the test is naturally resistant to outliers — extreme charges simply appear as the highest ranks rather than distorting the analysis. It is often described as a more flexible alternative to the t‑test, since it does not require the data to follow a normal distribution (Statsig, 2025).

The Mann-Whitney U-test is used to analyze the degree of separation/overlap between two sets of observations drawn independently (‘Smokers’ and ‘Nonsmokers’) from the same population, where the measurement is ordinal or continuous (Rajaretnam, 2015). In this case, healthcare ‘Charges’ are continuous but often skewed. It is confirmed through exploratory data analysis that the healthcare ‘Charges’ in the given dataset are right-skewed. In addition to the visualizations from Part I, the Shapiro-Wilk test further confirms that the data is non-normal. The Mann-Whitney U test works by ranking all observations from both groups, smokers and non-smokers, and evaluating whether these ranks differ significantly in their healthcare costs (Geeks for Geeks, 2025).

4. Null and Alternative Hypotheses

Null Hypothesis (H0): There is no relationship between smoking status and the distribution of annual medical charges; specifically, the median medical charges for smokers and non-smokers are equal.

Alternative Hypothesis (H1): There is a statistically significant relationship between smoking status and annual medical charges, such that the distribution of charges (median) differs significantly between smokers and non-smokers

5. Error-free Code in Python Calculation, Results and Output

Press enter or click to view image in full size

Press enter or click to view image in full size

Figure 16. Shapiro-Wilk and Mann-Whitney U Test Calculation, Results, and Output from PyCharm

I. Nonparametric Test Results Evaluation

1. Mann-Whitney U Test Results and Rejection of the Null Hypothesis

The Mann–Whitney U test was used to assess whether smoking status is associated with meaningful differences in annual medical charges. This non-parametric approach is appropriate given the strong right skew in the cost data, allowing the analysis to focus on distributional differences rather than assumptions of normality.

The resulting U‑statistic of 284,133.0 reflects substantial separation between the two groups. It indicates that charges for smokers consistently rank higher than those for non-smokers across the dataset. The p-value of 5.27 \times 10^{-130} is effectively zero which provides overwhelming evidence that the observed differences are not due to random variation.

The effect observation of the median difference validates that the coefficient for smoking status represents a substantial increase in cost. In a regression-aligned interpretation, this means smoking status functions as a statistically significant predictor of the distribution of medical charges. Consequently, the null hypothesis — that smoking status has no explanatory relationship with healthcare costs — is decisively rejected.

Charges vs. Smoker Status Regression Plot

Press enter or click to view image in full size

Figure 17. Regression Plot — Interpretation: The regression line slopes upward from non‑smokers to smokers, confirming that smokers consistently incur higher medical charges.

2. Answer to Research Question: Given the Rejection of the Null Hypothesis

There is a statistically significant relationship between smoking status and annual medical charges. The analysis confirms that smoking status is a significant predictor of the variance in healthcare costs, with smokers’ charges being significantly higher than those of non-smokers.The null hypothesis is rejected, showing that smokers and non-smokers do not share the same distribution of charges. In practical terms, smokers have much higher median charges, confirming that smoker status is a strong driver of cost differences.

HO: Rejected. The data provides overwhelming evidence against the assumption that smoking status has no effect on the distribution of annual medical charges.
H1: Accepted. At least one level of the independent variable (smoking status) explains a non-zero portion of the variance in the dependent variable (medical charges).
3. How Stakeholders Benefit from Mann-Whitney U Test

Choosing the Mann–Whitney U test for smoker versus non-smoker charges directly supports business, compliance, and community needs. For executives, it shows clear evidence that smokers cost more, justifying premium differences or surcharges. Regulators benefit because the test is fair and unbiased, with claims data not skewed, making rating factors easier to defend.

Healthcare providers and advocates gain proof of smoking’s financial impact, strengthening support for cessation programs. Policyholders see transparent evidence explaining higher premiums, which builds trust. Analysts and audit teams value the test for its simplicity, reproducibility, and robustness to outliers, making it easily fit into compliance workflows. Overall, the test focuses on medians, handles skewed data well, and produces results that are easy to explain: smokers cost more, and here’s the statistical proof.

J. Nonparametric Statistical Testing Summary

1. Recommend a course of action based on your findings.

Based on these results, the best next step is to use smoking status as part of pricing and policy decisions because the data shows smokers consistently cost more. This gives insurers and employers a fair, evidence‑based reason to charge higher premiums or add smoker surcharges. The analysis is statistically solid, so regulators can see that the method is transparent and defensible. The findings also highlight the real financial impact of smoking, which supports offering or expanding smoking‑cessation programs in the community.

Different groups should get information in a way that makes sense for them: executives need a clear business explanation for pricing changes, regulators need a clean audit trail showing how the numbers were produced, public‑health leaders can use the results to push for prevention programs, and the community should get a simple explanation of why smoker premiums differ. As a next step, the analysis can be expanded to include other factors like age, BMI, and region to build a more complete picture of what drives healthcare costs.

2. Discuss the limitations of your data analysis.

The Mann–Whitney U test is useful for comparing two groups, such as smokers and non-smokers; however, it only examines differences in their distributions or relative rankings. It doesn’t account for other factors, such as age, BMI, or region, so it can show that smokers pay more, but it doesn’t explain why or how much compared to these other influences. ‘Charges’ is skewed, with very high outliers, and while the test is fairly robust, extreme cases can still distort results, making median differences appear smaller than the actual financial impact.

The simple smoker/non-smoker split also misses nuances, like how much someone smokes or whether they used to smoke, which can matter for risk. Results depend on the dataset, so findings may not apply to all populations or regions. Importantly, the test shows association, not causation — higher charges could be linked to other health or social factors. Finally, the U‑statistic itself isn’t intuitive, so results need to be translated into medians, ranges, and effect sizes to make sense for non-technical stakeholders. Without clear communication, stakeholders may misinterpret the strength of the evidence.

Conclusion

Univariate and bivariate visualizations, descriptive statistics, and parametric and nonparametric testing deliver valuable insights for this major health insurance provider. Results from the OLS with Robust SE parametric test, reflected in the R² and RMSE values, clearly show that BMI, age, and smoking status are strong predictors of healthcare costs. The Mann-Whitney U nonparametric test further highlights the significant cost increase driven by smoking, with smokers incurring notably higher expenses than non‑smokers. These findings underscore the importance of accounting for the financial impact of smoking and reinforce the need to pursue recommended interventions aimed at reducing costs for stakeholders. Most significantly, the statistical testing suggests that the Null Hypothesis (H0) of no relationship can be rejected in favor of the Alternative Hypothesis (H1) for Age, BMI, and Smoker Status, with Smoker Status being the primary cost driver for Insurance Charges.

References

Bobbitt, Zach. (2022, June 11). How to Test for Normality in Python (4 Methods). https://www.statology.org/normality-test-python/

Bruce, P. & Bruce, A. (2017). Practical Statistics for Data Scientists. O’Reilly Media, Inc.

Downey, Allen B. (2025). Think Stats, 3rd Edition. O’Reilly Media, Inc. https://colab.research.google.com/github/AllenDowney/ThinkStats/blob/v3/nb/chap11.ipynb

Geeks for Geeks. (2025, July 23). Linear Regression (Python Implementation). https://www.geeksforgeeks.org/machine-learning/linear-regression-python-implementation/

Geeks for Geeks. (2025, July 24). Mann-Whitney U test. https://www.geeksforgeeks.org/machine-learning/mann-whitney-u-test-2/

Geeks for Geeks (2024). Residual Sum of Squares. https://www.geeksforgeeks.org/maths/residual-sum-of-squares/

Lujan, Alan. Mastering Econometrics: Regressions, Inference and Numerical Optimization. https://github.com/jhu-aap-econ/merino/blob/main/notebooks/Ch8.%20Heteroskedasticity.ipynb

Pinzon, Enrique. (2022, October 6). Heteroskedasticity Robust Stand Errors: Some Practical Considerations. https://blog.stata.com/2022/10/06/heteroskedasticity-robust-standard-errors-some-practical-considerations/

Rajaretnam, T. (2015). Statistics for Social Sciences. SAGE Publications Inc.

Statsig. (2025, June 23). Mann-Whitney U: Non-Parametric A/B Testing. https://www.statsig.com/perspectives/mannwhitney-nonparametric-abtesting

Waples, Josef. (2025, January 8). OLS Regression: The Key Ideas Explained. https://www.datacamp.com/tutorial/ols-regression

file:///Users/meredithsmith/PycharmProjects/PythonProject/PythonProject/PythonProject50/exportToHTML/D599Task2.ipynb.html

Press enter or click to view image in full size

Press enter or click to view image in full size


Press enter or click to view image in full size

Press enter or click to view image in full size

Press enter or click to view image in full size

Press enter or click to view image in full size

Press enter or click to view image in full size
