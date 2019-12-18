<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# No Show Prediction for Medical Appointments

### A machine learning project, based on medical appointments data

**by Lena Frommann**

**Ironhack, Data Analytics Course, Berlin, 13/12/19**

## Executive Summary

Imagine, you need to schedule a medical appointment in Germany and you get told that the practice is fully booked for the next three month. That is what happens to me whenever I try to get an appointment at short hand. It is frustrating and annoying. The good news is that patient data can be used to optimize appointment bookings and to predict if patients show up to their appointments or not (the later is called **no show**). As I could not find adequate data for German medical appointments, I used medical appointments from a Brazillian city called "Vitória". The project result is a machine learning module that predicts the possibility for patients to not show to their appointments. By further improving the model accuracy and adding more features, this project is the basis to implement a "No Show Alert" into practice management systems. This alert would be an application highlighting patients facing high risk to not show in order to reach out to them prior to their appointments and reschedule if necessary. A visual prototype of the No Show Alert can be found in the presentation, see links below.

## Content

- [Overview](#overview)
- [Data Preparation](#data-preparation)
- [Data Analysis](#data-analysis)
- [Conclusion](#conclusion)
- [Links](#links)


## Overview

The goal of this project is using machine learning to build and train a model to predict if patients show up to medical appointments or not.

Main questions:

    1. Which are the key features that impact patients’ no show?
    2. How can the no show rate be reduced?
    3. How can the prediction of the now show rate be integrated into daily practice management? 

Hypotheses:

    I. Patients at a younger age are more likely to forget their medical appointments or set other priorities. Therefore I
       assume that patients aged between 13 and 25 face a higher risk to not show up to their appointments then people aged
       between 40 and 70.

    II. Patients having health issues where you need to consult a doctor frequently (like e.g. high blood pressure, diabetes)
        are more likely to show up than patients without serious health issues.
        
    III. Patients dealing with a long time span between scheduling the appointment and the actual appointment day are more
         likely to not show up in comparison to patients scheduling and taking the appointment the same day.

    They will be tested through exploratory and visual data analysis as well as through the machine learning feature importance
    method.

Project Structure:

	1. Data Exploration & Cleaning
    2. Data Analysis & Visualization
    3. Model Building
    4. Model Evaluation
    
Tech Stack:

	* Python 3.0
    * Pandas
    * Numpy
    * Matplotlib
    * Seaborn
    * Scikit-Learn

## Data Preparation

### Overview:

* What is your dataset about?
* Where/how did you obtain your dataset?
	* It can be either a public dataset or collected with API/web scraping.
	* Provide a link if possible.
* General description of the dataset such as the size, complexity, data types, etc.

### Data Ingestion

* If you downloaded a dataset (either public or private), describe where you downloaded it and include the command to load the dataset.
* If you obtain the data via API/web scraping, provide the scripts.

### Data Wrangling and Cleaning

* Your full process of data wrangling and cleaning.
* Document your workflow and thinking process.

### Data Storage

* Dump your data to a MySQL database and/or a `.csv` file.

## Data Analysis

### Overview

Overview the general steps you will go through to analyze your data in order to test your hypothesis.

### Data Exploration and Visualization

* Document each step of your data exploration and analysis.
* Print charts to demonstrate the effect of your work. Charts make your presentation look good too.
* If you use ML in your final project, also describe your feature selection process.

### Model Training and Evaluation

* Train your ML model, produce results, and evaluate.
* This is an iterative process. Try your best to improve your model performance by:
	* More data cleaning.
	* Try different models and select one that is the simplest yet produce the best result.
	* Try advanced techniques and see if they improve the result.

## Conclusion

* Summarize your data analysis result.
* State your conclusion of your hypothesis testing.
* Interpret your findings in terms of the human-understandable question you try to answer.
* What are the next steps?

## Links
Kaggle Data Set:<br/>
https://www.kaggle.com/joniarroba/noshowappointments<br/>
GitHub Repo:<br/>
https://github.com/Lenastartscoding/Projects<br/>
Presentation:<br/>
https://docs.google.com/presentation/d/1zTH2fKBsmltrdrncBJ91FU99wYYEtMgfd5vW63spQ0s/edit?usp=sharing