# Employee’s Performance:

Employee performance and the desire to optimise a labourforce towards higher productivity, is a topic at the lips of every business owner/runner. Traditional forms of encouraging employees towards higher productivity have been explored in length. Companies today spend a good amount of money in assessing productivity across different operational units, teams and departments as well. 

In assessing employee data, companies can then utilise this information to make strategies that create some kind of competitive edge within the labour force, and respective field of operations. 

The labour force being one of the key drivers of overall company revenue, it is important to have a full understanding of what kind of insights we can collect from the assumed, as well as researched performance indicators; hence why the selected dataset for this project centres around HR performance analytics. The dataset can be accessed directly on the [Kaggle platform]([url](https://www.kaggle.com/datasets/sanjanchaudhari/employees-performance-for-hr-analytics)).

# General (initial overview) assessment of the dataset:

The datasets contain 14 columns, most of the columns are related to traditional key indicators or measures, but do not have any modern measures/features. The data set has around 17,417 rows.  Actual shape of the dataset being (17417, 13).  The data-type ranges from numeric (8 columns) to object (5 columns). The overall memory usage stats slightly over 1,7 mbs 
 
From the overview, we can see that the average number of trainings falls close to the min. The data also shows us that majority of the labourforce falls below 40 years of age. Only 25% of the labourforce are  40 and above. The average rating fall above the average (2.5). Most people do not meet a KPI score of more than 80, and most have not won any performance related award. The average training score is 63%. 

Two columns have missing entries. The columns are education and previous-year_rating. As expected, only the employee ID column had a clean record of unique values. The number of unique values in most columns. It would be interesting to look into the individual unique values per column to see why the specific unique values exist for identified measures/metric. 
There are 70.7% more males than females in this dataset. 69.1% of employees have a bachelor's degree, 29.1% have a master's or higher, and 1.7% of employees have secondary school education or lower.  Over 55.99% of recruitment takes place via undisclosed processes, while 42.2% is done via sourcing. Only 1.8% is via referral programmes. Sales & Marketing (31.3%) and Operations (20.2%) are the largest departments.

There is a moderate (0.6) correlation between age and length of service. Most of the correlation on the heatmap falls on the negative side, but there is a very weak positive correlation of number of training with training scores and awards. There is also a very weak positive correlation of age with awards, and ratings. Average score does have a small impact on awards, ratings and KPIs. 

# Possible areas of exploration (aspects interesting to look into):

When it comes to the distribution of employees across departments, the data is very unevenly distributed, as earlier alluded to.  With this information, it would be interesting to see how KPI expectations and ratings vary between larger departments, and smaller departments. How training is distributed across the departments would be insightful to take a deeper dive into.

With that in mind: 

   		Hypothesis 1; we can theorise that larger departments will have to take up more training due workload related factors. 

   		Hypothesis 2: Meeting KPI targets might be easier for larger departments 

   		Hypothesis 3: there is a correlation between larger departments and awards

Most people hold a bachelor's degree or higher, it would be interesting to see if education levels contribute to rating and training scores, as well KPI goals being met.

	  	Hypothesis 4: education is directly tied to the scores and KPI goals

There is a higher number of male hired as opposed to females, it would be important to have a look at how the female scores and KPI performances defer from those of men: 

	  	Hypothesis 5: there is a gap in the scoring, and awarding of females

The project will also analyse how the skewed regional distribution plays a role in the overall metrical measures of performance, and how the different hiring channels contribute (if at all) to overall performance. 


