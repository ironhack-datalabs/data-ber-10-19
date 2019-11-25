<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Employee Satisfaction
a data visualization project, based on real world data of a consulting company<br/>
<br/>
*Nadav Smith, Ivy Ip, Lena Frommann*

*DATA ft, BER, 11/19*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
<br/>
Our project comprises to evaluate how satisfied employees are with company internal services of different departments.<br/>
Therefore, we used a dataframe that contains  the results of an annual employee survey with the aim to:<br/>
<br/>
• figure out how intense communication flows within the company are<br/>
• the reason why employees contact certain departments<br/>
• how employees rate the support of different departments<br/>

## Questions & Hypotheses
Before starting to code, we defined some general hypotheses:<br/>
<br/>
1. Employee age and seniority level are related to each other and to the general satisfaction score.<br/>
2. The number of times employees contact a certain department, the lower the rating of this department.<br/>
3. The overall satisfaction score increases if the employee is satisfied with the services of the major departments.<br/>
4. The satisfaction score in New Dehli is lower compared to other company locations, because not all departments are avaliable on site.<br/>
<br/>
Also, we formulated questions to answer within our project:<br/>
<br/>
1. How is the overall satisfaction of the employees?<br/>
2. How is the overall satisfaction of the employees affected by the service level of core departments?<br/>
3. Has the company location an impact on employee satisfaction?<br/>
4. Why do the employees contact different departments?<br/>
<br/>

## Dataset
We used a csv dataset based on a published employee survey. However, the data provided was adjusted to not be able to draw conclusions regarding the name of the company or any other confidential information.<br/>
While searching for a suitable dataset for this project, it was impportant for us that the overall topic is easy to understand for our audience and that the data set is well suited for visualization purposes.<br/>

**Employee Satisfaction:** <br/>
The original dataset had 76 columns. Hence it was necessary to reduce the amount of columns to only include those which are necessary for our analysis. The dataset we finally worked with has the following columns after cleaning:<br/>
<br/>
* ID
* location
* gender
* age_category
* seniority_category
* satisfaction_score
* #contact_acct
* rating_acct
* #contact_HR
* rating_HR
* #contact_OM
* rating_OM
* rating_security
* rating_D&R<br/>
shape: (182, 17)

Furthermore, we decided to extract columns from **Employee Satisfaction** to several data frames. First purpose was to make the plotting process easier and extract the reasons why employees contacted the three core departments. The columns of the dataframes are listed below:<br/>

**Contact Reason Accounting** <br/>
* Reason
* Percentage of contacts per reason<br/>
shape: (7, 2)

**Contact Reason HR** <br/>
* Reason
* Percentage of contacts per reason<br/>
shape: (9, 2)

**Contact Reason OM** <br/>
* Reason
* Percentage of contacts per reason<br/>
shape: (8, 2)

Last dataframe extracted will be extracted will be used for examining correlation between overall satisfaction, department ratings and ratings for each particular service provided by a department. 

**effects_of_subquestions_on_ratings**<br/>
* satisfaction_score
* rating_acct
* rating_HR
* rating_OM
* rating_security
* rating_D&R
* accounting_evaluation_breack_down_Q1 (to Q10)
* HR_evaluation_breack_down_Q1 (to Q10)
* Office Management__evaluation_break down_Q1 (to Q10)
* Security_department_evaluation_break down_Q1 (to Q11)
* data&records_department_evaluation_break down_Q1 (to Q3)<br/>
shape: (182, 48)

## Workflow
1. Brainstorm on topic and data<br/>
2. Agree on data set to use<br/>
3. Define hypotheses and questions serving as a guideline for our project<br/>
4. Decide, which data will be used and define the relevant colums<br/>
5. Clean the data<br/>
6. Explore the data<br/>
7. Summarize our key findings and decide what we want to visualize in plots<br/>
8. Start plotting<br/>
9. Summarize our work<br/>
10. Discuss the storyline of our presentation<br/>
11. Make presentation<br/>
12. Upload all deliverables in project folder on GitHub<br/>

## Organization
Using a whiteboard and our notepads, we started with brainstorming in the early project stage to write down our questions, goals. Then we went through the data set based on the questionnaire together, to make sure each group member understands what the columns and questions mean. Thereafter, we did the data cleaning all together. Then, we defined and distributed tasks, to work individually on data exploration and plotting based on three main topics. There was a good balance between group work and individual work. Some tasks could be accomplished more efficiently individually.<br/> 
In the end we worked all together on the final presentation and the jupyter notebook file. <br/>
Throughout the whole project, we had several small team meetings to inform each member about progresses and to define upcoming steps and deadlines. We used the Slack Channel for sharing our jupyter notebook files and code snippets.<br/>
<br/>
Our repository includes:
<br/>
* Jupyter Notebook 1: Data Cleaning
* Jupyter Notebook 2: Contact Reasons 
* Jupyter Notebook 3: Plotting
* Jupyter Notebook 4: effects_of_subquestions_on_ratings<br\>
* original csv file: Satisfaction Survey Admin (raw data)
* cleaned csv file1: Employee Satisfaction
* cleaned csv file2: Contact Reasons
* cleaned csv file3: effects_of_subquestions_on_ratings<br\>>
* text file: Data Description 
* README.md file

## Links

GitHub Repo:<br/>
https://github.com/Lenastartscoding/data-ber-10-19/tree/master/module-2_projects/visualizing-real-world-data-project
Presentation:<br/>
https://docs.google.com/presentation/d/1j9GQBP8QaIKvccMoEkR18_Xs8rhY6zddsv78E9irp-M/edit?usp=sharing