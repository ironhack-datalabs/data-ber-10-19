<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Evaluation of Employee Satisfaction
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
We want to display the bike sharing companies which are the most popular ones within the bike sharing industry.<br/>
Our goal is to figure out...<br/>
Before starting to code, we took some general assumptions: ...<br/>
1.<br/>
2.<br/>
3.<br/>
<br/>
In order to work towards a goal, we formulated the following hypothesis which is tested through our data later on.<br/>
<br/>
Hypothesis:<br/>


## Dataset
We used a csv dataset based on a published employee survey. However, the data provided was adjusted to not be able to draw conclusions regarding the name of the company or any other confidential information.<br/>
While searching for a suitable dataset for this project, it was impportant for us that the overall topic is easy to understand for our audience and that the data set is well suited for visualization purposes.<br/>

**Employee Satisfaction:** <br/>
The original dataset had XX columns. Hence it was necessary to reduce the amount of columns to only include those which are necessary for our analysis. The dataset we finally worked with has the following columns after cleaning:<br/>
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
* rating_D&R

shape: (182, 17)

Furthermore, we decided to extract columns from **Employee Satisfaction** to three new data frames. The purpose was to make the plotting process easier and extract the reasons why employees contacted the three core departments. The columns of the dataframes are listed below:<br/>

**Contact Reason Accounting** <br/>
* Reason
* Percentage of contacts per reason
<br/>
shape: (7, 2)

**Contact Reason HR** <br/>
* Reason
* Percentage of contacts per reason
<br/>
shape: (9, 2)

**Contact Reason OM** <br/>
* Reason
* Percentage of contacts per reason
<br/>
shape: (8, 2)

## Workflow
1. Think of possible question to be resolved using data. <br/>
2. Find out, which data is available for this purpose and adjust the questions accordingly.<br/>
3. Decide, which data will be used and chose the relevant colums and rows.<br/>
4. Clean the data and keep columns, that serve our purpose.<br/>
5. Merge our available data into one dataframe.<br/>
6. Make conclusions and plots out of the new dataframe.<br/>
7. Export everything to one csv file.<br/>
8. Rename csv file and read it again for further visualization. <br/>
9. Visualize the bike sharing providers on an interactive world map.

## Organization
We tried to distribute tasks beforehand which we defined through a manual kanban board. Mostly each of us worked individually on the tasks. However, we performed the merge all together.<br/>
In the end we worked all together on the final presentation and the jupyter file. <br/>
We shared the desks and a Slack Channel, to communicate throughout all the project. <br/>
Our repository includes:
* Jupyter Notebook file
* cleaned csv file
* text file with descriptions of data frame columns
* README.md file

## Links

[GitHub Repository]: <br/>
https://github.com/Nikitsatsiki/data-ber-10-19/tree/master/module-1_projects/data-thieves-project

[Presentation]:   
https://docs.google.com/presentation/d/1nSgW6A5Jk74jCGRKpderM9GuxM3DanDWYIIcB2WSyv0/edit?usp=sharing <br/>