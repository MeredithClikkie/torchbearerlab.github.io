The Data Analytics Life Cycle

The data analytics life cycle is a process utilized by data analysts to create data-driven decision-making. This structured life cycle helps businesses understand the value of their data to bolster growth, profitability, and innovation. Business understanding, data acquisition, data cleaning, data exploration, data modeling, data mining, and reporting and visualization play an essential role in the data analytics life cycle. In addition to a snapshot of the data analytics life cycle, this paper will discuss data cleaning with Python and some ethical problems in the data cleaning process.

<img width="680" height="668" alt="image" src="https://github.com/user-attachments/assets/f93bde89-4e9d-4709-875d-1a13e0dea632" />

A. The Seven Phases of the Data Analytics Life Cycle

Business Understanding

Understanding, planning, and discovering the business’s objectives, stakeholders, and project scope is foundational to the data analytics life cycle. The business understanding phase aims to understand the objectives that inspire the need for the data analysis. Data analysts communicate with the stakeholders to establish goals and the key questions. (WGU, 2.1.1)

Data analysts can gain expertise in business understanding by communicating with stakeholders and researching the business’s history. For example, within a retail business, data analysts will collaborate with the owner or management staff to plan a time series analysis of when customers purchase certain products throughout the year to understand demand and create a sales forecast. The data analyst and stakeholders will set the project’s goal and define the key questions.

Data Acquisition

Gathering, extracting, querying, and collecting data occur under this data analytics life cycle phase. Data acquisition can be executed by doing online research and/or acquiring reports provided to the organization’s data analyst. The analyst may have to extract data from the business by querying the data. (WGU, 2.1.1)

Expertise in acquiring data requires proficient knowledge of query languages such as SQL. Other data collection avenues are surveys, web scraping, building data pipelines, and utilizing APIs to download data from external sources. An example of data acquisition in a sales forecast prediction project would require obtaining financial records of the retail business to understand its historical revenue trends.

Data Cleaning

Data cleaning, which is also called cleaning, wrangling, scrubbing, and munging data, is often overlooked, thus possibly causing irrelevant results. This phase involves identifying and fixing improperly formatted values, duplicates, missing data, and outliers. Overlooking the data cleaning phase will likely result in an inaccurate project outcome. (WGU, 2.1.1)

Data cleaning expertise consists of having expert knowledge of SQL, Python, R, and/or Excel. A thorough understanding of these tools lets the data analyst know which tool is best for their project to efficiently and effectively modify, transform, and/or reduce data. For example, in a sales forecast prediction project, the analyst will upload a dataset to Excel, Python, or R to check for errors such as duplicates, improperly formatted data, and outliers.

Press enter or click to view image in full size

Press enter or click to view image in full size

Data Exploration

Identifying basic correlations between variables and discovering patterns helps the analyst to understand the data they are working with. Data analysts can utilize exploratory data analysis (EDA) and descriptive statistics to summarize the main characteristics of a data set. This phase creates an understanding of the data structure and identification of patterns, trends, and anomalies. (WGU 2.1.1)

Expertise is gained in data exploration through an extensive knowledge of descriptive statistics to create numerical summaries and data visualizations. For example, the data analyst will develop sales statistics from the data for a sales forecast prediction project. The data can then be presented in a visualization with a line chart to show trends and changes in sales over time.

Predictive Modeling

Predictive modeling, regression models, time series, and data modeling extend exploratory data analysis to mathematical models. This phase involves estimating the likelihood of a future event or future values using historical data, various statistical algorithms, and machine learning techniques. Predictive modeling is important to businesses as it aids them in decision making, risk management, resource optimization, understanding customer insights, having a competitive advantage, cost reduction, and having improved outcomes (geeksforgeeks.org, 2024).

Predictive modeling expertise involves automating the training and use of models using tools such as Python and R to create statistical algorithms. The data analyst will learn from the previous sales data analyzed through EDA and statistical summaries and predict future sales from past trends. For example, in a sales forecast prediction project, the sales data is preprocessed to show sales trends over time to predict future sales revenue. Prediction modeling executed using Python, for example, involves grouping data by sales summaries for each order date, to create a trendline that can expand to include future dates. (geeksforgeeks.org, 2025 April)

Data Mining

Data mining occurs through looking for patterns in large amounts of data with tools like Python and R. This phase determines if groups exist within the data, and if so, the groups are then classified. Data mining is often used interchangeably with machine learning, deep learning, AI, and supervised/unsupervised models. Automated models that learn and improve over time can be created in this phase to simplify and eliminate the need to do unnecessary repeat analysis. (WGU, 2.1.1)

Expertise in data mining involves knowing that data needs to be subset into training and testing datasets to build models. If machine learning runs on the entire dataset, it will become problematic. The goal is to create models using machine learning algorithms that learn, improve, and continually update over time. (geeksforgeeks.org, 2025 April)

Reporting and Visualization

Reporting and visualizing data is where the analyst gets to tell the data story. The reports and visualizations summarize the analysis and provide actionable insights to stakeholders through insightful graphs or interactive dashboards. Reporting and visualization expertise consists of proficient knowledge of graphs and tools such as Tableau. The finished reports provide actionable insights to the stakeholders (WGU, 2.1.1)

For example, with a sales prediction forecast project, a visualization that compares actual and predicted values is a way the data analyst can show the accuracy of their model to stakeholders. One way of creating this type of visualization is by connecting machine learning models to Tableau. The analyst can use Tableau to interpret the results and make clear, understandable, insightful visualizations to provide the sales prediction forecast to the stakeholders. (Geeksforgeeks.org, 2025 April)

The Importance of Understanding the Organizational Goal/Mission of the Organization

Become a member
The data analyst’s knowledge of the organizational goal will help the analyst to identify the business requirement by narrowing down the focus of their data analysis. Understanding the businesses’ goal and mission provides critical information regarding identifying their stakeholders, a timeline for meeting the goal, any potential limitations the organization may have, and the type of resources and budget allotted for the project.

The data analyst should continually learn about their business. This effort will improve the data analyst’s ability to communicate efficiently with stakeholders from different backgrounds. Understanding the mission and goal of the organization will help the analyst to communicate more effectively by being bilingual and versed in the language of analytics and the organization. The data analyst reviews the business question when providing project updates, reports, and visualizations to the stakeholders. (WGU, 3.1.3)

Knowing the goal and mission of the organization helps determine which type of analytics to use, which determines the vital questions that data analysts must have to progress throughout the data analytics cycle. Determining the kind of analytics allows the data analyst to understand he value and difficulty of the analysis. There are four types of analytics. In order of least value and difficulty to most are descriptive, diagnostic, predictive, and prescriptive analytics. Starting with descriptive, the lower end of the diagnostics spectrum also corresponds to the project being more about the organization simply needing information, and to the higher end, desiring optimization insights. (WGU, 1.1.2)

B. Data Cleaning with Python

Discerning the Appropriate Data Cleaning Tool

The decision-making process of selecting the appropriate tool for the data cleaning phase depends on the data cleaning goals, which will determine the techniques, methods, and type of tool that is most appropriate. Things to consider when choosing between Python and R, for example, involve understanding the problems that need to be addressed in the dataset. Is the data in a web app or an installed program? How large is the data? Python would be the appropriate data analytics program/tool to use for cleaning data when the data is in a web app, and if the database is vast. (WGU, 2.2.3)

Addressing Technical Problems with Cleaning Data in Python

Technical problems that will be addressed by using libraries such as pandas or numpy within Python for data cleansing include eliminating/repairing data errors within the dataset. Errors come in the form of improperly formatted values, duplicates, missing data, and outliers. A reduction in data amount will occur when mistakes are addressed and eliminated. The outcome of the data could be dramatically changed. Outliers need to be identified and dealt with to minimize variability in the statistical models. (geeksforgeeks.org, 2025 April)

An Organization’s Need for Cleaning Data in Python

For an organization that has an extensive dataset and uses a web-based app, Python is the appropriate programming language. It is needed to identify and remove missing, irrelevant, and duplicate data. Raw data needs to be cleaned to ensure that the data is accurate and free of errors. After the data goes through the cleaning process, its interpretability is enhanced, thus ensuring correct predictions. Data cleaning is necessary to provide accuracy and take the right actions based on EDA insights. Data cleaning using the correct program and subsequent libraries for Python in relation to the data results in improved model performance, increased accuracy, better representation of the data, improved data quality, and data security. (geeksforgeeks.org, 2025 January)

C. Potential Ethical Risks on Essential Business Functions

Discuss Three Risks of Using Python for Data Cleaning

Three risks for using Python (or any tool) to clean data are that it is time-consuming, error-prone, and can result in overfitting. When dealing with large and complex datasets, data cleaning is very time-consuming, even when using the appropriate language. The risk exists that important information can be lost in the process. Too much data may be removed, which results in overfitting the data. (Webb, 2020)

Three Potential Legal or Ethical Problems of Data Cleaning

Based on the time-consuming, error-prone, and overfitting risks of using Python for data cleaning, potential legal or ethical problems related to the big data of the organization exist. One issue with big data is the issue of privacy. It is difficult for an organization that possesses big data not only to pay to keep data safe but also to keep it safe logistically. Sensitive information such as personal, financial, or health data should be protected and held to any legal or ethical regulations to which the data is subject. The data analyst should take measures to protect customers from identity theft, fraud, or malicious attacks by encrypting, anonymizing, or masking data before cleaning it.

“Insights are only as good as the quality of the data they come from” (Hillier). Applying poor best practice to data cleaning is an ethical concern. Dirty or bad data can lead to poor insights and risk in certain circumstances. Take healthcare records, for example, the analysis project is to tell a data story of the number of patients with a rare contagious illness. If medical records at a local hospital had duplicate records for several patients, and the data analyst skipped over cleaning the data, the numbers would become statistically inflated, leading to an inflated public health concern. (Hillier, 2022)

Bias is one more ethical risk in the data cleaning process. The data analyst needs to be intentional in looking for ways to offset bias. Personal and societal biases can creep in unintentionally, and taking time to step back from the data to ensure bias is non-existent or minimized is necessary. Offsetting bias in the cleaning process is difficult, so it is best to minimize it before data collection. However, if bias is detected in the data cleaning process, it is best to acknowledge bias with transparency, diversify data from various sources, and clean data methodically. Methodical data cleaning includes handling data in a way that does not introduce bias, bases decisions on sound statistical reasoning over gut feeling or convenience, and documents data cleaning steps so others can validate the outcome. (LinkedIn.com, July 6)

Conclusion

The data analytics life cycle does not always occur chronologically. It can skip around and go back to different phases multiple times. Each phase plays an important role, with more time spent in some phases than others. The data analyst must know the organization’s goal and intentionally offset or avoid bias. Cleaning data with Python before moving on to EDA is needed to prevent the final product’s setbacks, delays, or inaccuracies. Risks occur when cleaning big data, such as the risk of eliminating essential data. Ethical risks include committing bias, data leaks, and data integrity. When data analysts carefully and cautiously follow the data analytics life cycle process, stakeholders will benefit from the actionable insights and data assurance of the final outcome.

References

Geeksforgeeks.org. (2025, January 20). ML: Overview of Data Cleaning. https://www.geeksforgeeks.org/data-analysis/data-cleansing-introduction/

Geeksforgeeks.org. (2025, April 8). Sales Forecast Prediction — Python. https://www.geeksforgeeks.org/python/sales-forecast-prediction-python/

Geeksforgeeks.org. (2024, March 18). What is Predictive Modeling? https://www.geeksforgeeks.org/data-science/what-is-predictive-modeling/

Hillier, Will. (2022, December 15). Is Big Data Dangerous? https://careerfoundry.com/en/blog/data-analytics/is-big-data-dangerous/

LinkedIn.com (a). (accessed July 2, 2025). How Can You Choose the Right Data Cleaning Tools for Any Dataset?

LinkedIn.com (b). (accessed July 6, 2025). What Security Measures Should You Take When Cleaning Data for ML?

LinkedIn.com ©. (accessed July 6, 2025). You’re Analyzing Data with Potential Biases. How Can You Ensure an Unbiased Analysis Process?

Webb, Rebecca. (2020, November 25). 12 Challenges of Data Analytics and How to Fix Them. https://www.clearrisk.com/risk-management-blog/challenges-of-data-analytics-0

Western Governors University. (Accessed July 2, 2025). The Data Analytics Journey Lesson: Understanding the Data Analytics Life Cycle.
