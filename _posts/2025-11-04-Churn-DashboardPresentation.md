Part 2: Dashboard Presentation

1.  Two Elements of Effective Storytelling Used in this Dashboard Presentation

Problem statement

A clearly defined problem statement is crucial to the business, as it is specific, well-scoped, and actionable (Sridhar, 2025). The problem statement for my dashboard is the following: 
What are the key drivers of customer churn compared to those with the longest tenure, and how can executive leaders increase customer retention and revenue?
Ghost Deck
•	synthesis
•	logical train of thought
•	limitations and caveats of the analyses (Udacity).
2.  Introduction
a. Introduction and Background. 
Hello, my name is Meredith Smith, and I’m a data analyst.
I'm working with a telecommunications company to uncover data-backed insights that inform customer retention efforts and strategic decision-making.
b.  Dataset Description
Today, we’ll explore a real-world scenario in which a telecommunications provider needs to predict which customers are most likely to churn.  
This analysis is designed to help executive leaders develop data-driven strategies for retaining customers and protecting revenue.
•	Demographics
•	Churn that occurred within the last month
•	Account and Billing Details
•	Subscription and product features
•	Survey responses regarding telecommunication-related factors were rated on a scale of 1 to 8 in order of importance
Again, the central question driving this dashboard is:
•	What are the key drivers of customer churn compared to those with the longest tenure, and how can executive leaders increase retention and revenue?
•	We’ll walk through insights derived from this data to help the company understand the underlying causes of its 26.5% churn rate, which has resulted in the loss of 2,650 customers and $528,000 in revenue.
3. Data Representations Presentation
a.  Two Presentations

Two data representations from this dashboard that provide insights into the key drivers of customer churn are the Contract and Internet Pie Charts, and the Overall KPIs Text Table.
Representation 1: The Contract & Internet Service Pie Charts 
•	Show customer churn for each contract and internet service type:
o	DSL
o	Fiber Optic
o	None, for customers who do not have internet service with the company
The default view displays the overall churn rate for each internet service type, sliced by color-coded contract slices. 
•	For example, there’s a 44.2 percent churn rate for those who have DSL internet service and a month-to-month plan
•	The chart is color-coded and sliced according to the customer churn for each contract type
o	Month-to-month
o	1 year
o	2 year
b.  Data Representation Explanations.

I chose these two representations to display the data because they both provide key insights that would be overlooked if only a brief glimpse of the data were examined.
Data Representation 1: The Contract & Internet Service Pie Charts(top right)
o	I chose the contract and internet service pie charts to illustrate the high customer churn rate among those with month-to-month contracts, regardless of the type of internet service.
Data Representation 2: The Overall KPIs Text Table (top left)
o	Provides the pertinent numbers the executive leaders need to see: the total number of customers, churned customers, churn rate, and revenue churn. 
4.   Filters

a.  Two Filters

Now, I will show you two filters that modify data: the Internet Service Drop-Down Filter and the Contract Drop-Down Filter.
Filter 1: Internet Service Drop-Down Filter
•	Shows the churn for internet service types across the board
•	Let’s look at customer churn for DSL customers. Customers with DSL internet and month-to-month contracts have the highest churn rate (read from overall KPIs), 
•	It modifies the way the data is represented by showing how the churn rates vary according to the internet type
•	One insight gained from this filter is that DSL internet customers specifically have high churn once GB usage surpasses 6.6 GB
Filter 2: The Contract Drop Down Filter
•	Reflects the churn for contract type across the board
So here. Let’s look at the month-to-month contract:
•	It modifies the way the day is represented by showing the significant high churn of month-to-month contracts, (especially DSL), again noting the pattern after 6.6 GB
•	This insight shows that customers with one or two-year contracts churn less, and it would be beneficial to change costs and promote the one or two-year contracts to increase customer retention
b.   Filter Usability and Data Exploration Enhancement.

Both filters improve usability and data exploration. 
Internet Service Drop Down Filter
•	Increases usability and data exploration by allowing the users to interact with the data, providing insight into what is behind the higher churn rates of each internet type
The Contract Drop Down Filter
•	Increases usability and data exploration by allowing the users to interact with the data, providing insight into what is behind the higher churn rates for each contract type
5.  Design and Accessibility

a.  Addressing Colorblindness.

•	The dashboard is accessible due to the color choice, which limits the use of red and green
•	Blue and orange are more accessible to those with color blindness
b.  Two Additional Design Choices Used to Enhance Accessibility.
•	Tooltips, fonts, bold captions, and print for easy readability
•	Text table -- The Overall KPIs presents data in text form for those who want the quick stats without needing the visuals
o	This text table also serves as a helpful resource to ensure that the filters are reset appropriately
o	The map allows stakeholders to see how their customer churn is represented in each state
6.  Reflection

a.  Effective Storytelling Implementation and Explanation 

Storytelling Element 1: The Problem Statement

•	What are the key drivers of customer churn compared to those with the longest tenure, and how can executive leaders increase customer retention and revenue?
Storytelling Element 2:  The Outcome of the Ghost Deck 

•	Three key drivers behind high customer churn are month-to-month contracts, DSL internet service, and bandwidth usage 
Actionable Recommendations
•	The recommendation and next steps are to optimize prices by adjusting monthly charges to create an incentive for customers to choose 1- or 2-year contracts
•	Also, to level out the charges and costs across bandwidth usage for DSL customers
•	Also, the company needs to  understand why new customers are charged more than ongoing customers
Limitations
•	The analysis is limited in that it only represents customer churn over the past month. 
•	Is there a pattern of increased customer churn, or is this month an exception? We are also not provided with possible external reasons for customer churn, such as competitor pricing or additional individual charges for specific service features. We are also not given information regarding the reasons for the increased equipment failures
b. Lessons Learned
Dashboard Creation Lessons
One key lesson I learned while creating the dashboard is the power of diverse visual representations in bringing data to life. Combining a map, charts, and a text table made the analysis more engaging and accessible, allowing patterns to emerge more clearly.
That said, it was also challenging to convey all the contributing factors behind customer churn within the constraints of the dashboard. For instance, I chose to highlight the relationship between overall costs and the churn rate, rather than the relationship between the top and bottom 5% of tenured customers, due to space limitations. Still, that relationship revealed meaningful insights:
	Top 5%	Bottom 5%	Difference
Avg Monthly Charge	$170.00	$207.88	-37.88
Avg Bandwidth Monthly adj	523.23	414.52	108.71
Yearly Equip Failure Sum	213	179	34
Adj monthly failure	17.75	97.02	-79.27
Avg Monthly Tenure	71	3.446	67.554
Service Options:			
Phone 	456	455	1
Streaming Movies	238	340	-102
Streaming TV	246	314	-68
Multiple	223	276	-53
Device Protection	199	245	-46
Port Modem 	228	239	-11
Online Back	216	225	-9
Tech Support	181	186	-5
Online Security	181	179	2
Tablet 	138	159	-21

As seen from the table above: 
•	Customers with the shortest tenure experienced the highest number of equipment failures, averaging 0.2 failures per month, compared to 0.04 for those with the longest tenure.
•	Long-tenured customers tended to have lower monthly charges, fewer equipment failures, and lower overall data consumption (
Presentation Lessons
From the presentation side, I learned how valuable it is to articulate the rationale behind each visual and filter. Explaining why certain elements were chosen helped clarify the narrative and made the data story more compelling.
How I’ll Apply These Lessons Moving Forward:
•	Use visualizations to explore and reveal insights—often, the most meaningful discoveries happen during the process of building charts and graphs.
•	Expect the unexpected—visuals can surface surprising trends that might be missed in raw data.
•	Revisit and synthesize—the act of preparing a presentation deepens understanding and brings a sense of fulfillment. It’s rewarding to not only uncover actionable insights but also to tell a story that helps others see the value in the data.




References

Crocker, Robert. (Accessed November 3, 2025). Audience Attributes from Dashboard Design. Udacity.
Sridhar, Malavica. (Accessed November 3, 2025). Data Storytelling. Udacity



<img width="468" height="625" alt="image" src="https://github.com/user-attachments/assets/c9a9e116-d34c-4539-a80a-50dccc0f7490" />
