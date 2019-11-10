# Project: Business Intelligence with Tableau
Tableau Public: https://public.tableau.com/profile/ivy.ip#!/vizhome/TableauProject-CoffeeProduction/Story

## Data Exploration: Coffee Production Environmental Impact

## Overview

["Coffee is a beverage that puts one to sleep when not drank."](https://www.thebaristalife.com/blogs/blog/barista-lifes-top-117-coffee-quotes) - [Alphonse Allais](https://en.wikipedia.org/wiki/Alphonse_Allais). 

Over 2.25 billion cups of coffee are consumed in the world every day. As a popular beverage and important commidity, a simple cup of coffee is affecting daily life of people as well as our planet. 

In this project, we will explore some data on coffee production environmental impact collected from The Food and Agriculture Organization of the United Nations (FAO) database. FAO provides open resources to a variety of food and agriculture data for over 245 countries from 1961 to the most recent year available, which provides us a single source of data to examine the following aspects relateed to coffee production:

1. Coffee production quantity 
    - Data from 1961 to 2013 (latest avaiable year) is collected. Throughout the past few decades, the forms of growing coffee have changed to maximize the harvest and in recent years new method to tackle the production wastes have been introduced. Therefore we will look into the data with a wide time range. 
2. Gross Coffee Production Values 
    - the value of production at the point of sale (i.e. where it passes out of the Agriculture sector of the economy). This gives us some insight on the development of coffee market price throughout the years which is partially affected by coffee supply/production. 
3. Size of Primary Forest Area 
    - Size of naturally regenerated forest of native species, where there are no clearly visible indications of human activities and the ecological processes are not significantly disturbed. We will explore the impact on forest size from the change of coffee cultivation method. 
4. Pesticide use 
    - Agrochemical usage increases human chemical exposure and contributes in contamination waterways. We will examine the development of such usage along with coffee production trend. 
5. Crop residue amount  
    - The process of separating the coffee beans from the coffee cherries generates enormous volumes of waste material in the form of pulp, residual matter, and parchment. These agricultural wastes also contributes in Greenhouse gas (GHG) emission, e.g. direct and indirect nitrous oxide (N2O) emissions from nitrogen (N) of the residue. We will examine the change of crop residue amount with coffee production. 



## Dataset dimenions
1. Coffee production quantity\n
    - Number of records: 3,975\n
    - Period: 1961-2013\n
    - Unit: 1000 Tonnes
2. Gross Coffee Production Values 
    - Number of records: 1,047
    - Period: 1991-2013
    - Unit: USD/Tonnes
3. Size of Primary Forest Area 
    - Number of records: 1,776
    - Period: 1961-2013
    - Unit: Ha (Converted to sq. km in Tableau)
4. Pesticide use 
    - Number of records: 1,533
    - Period: 1990-2013
    - Unit: Tonnes
5. Crop residue amount  
    - Number of records: 2,612
    - Period: 1961-2013
    - Unit: kg (Converted to 1000 Tonnes in Tableau)



## Approaches 

1. **Define topic**
    - There are data of thousands of food products to select from in FAO database. The initial idea was to explore global food source and utilizations however the choices of food products are too wide and diversed, and hence it would be hard to find unified indexes that are suitable for different products. 
    - Once COFFFE is selected, we decided to explore the enviornmental factors of the coffee production and also listed the different aspects we would like to inspect. 
2. **Identify data required for findings and extract data**
    - With the 5 defined areas that we selected, we dipped deeper into different databases in FAO to extract required data. 
    - Data was downloaded as .csv files from datasets under different categories in FAO pages. Links are provided in the bottom. 
3. **Understand dataset structure & Examine columns**
    - Examine csv files and understand each column. Read through column and values descriptions found in FAO website and ensure correct interpretions.
4. **Data Cleaning**
    - Data is relatively clean and therefore tasks focused on reshaping and combining dataframes. Detail please see jupyter notebook in Coffee Production folder. 
5. **Basic plotting followed by visaul optimization**
    - Import cleaned dataframes into Tableau and join dataframes. Add Calculated Fields for unit conversion. Start with making basic plotting and later on trying out different visualization tools to optimize the results. 
6. **Add captions and annotations to complete storytelling process**
    - Group all worksheets into a story and descibe observations. 



## Data sources
*[The Food and Agriculture Organization of the United Nations](http://www.fao.org/home/en)
*[Food Balance sheet](http://www.fao.org/faostat/en/#data/FBS) 
*[Value of Agricultural Production](http://www.fao.org/faostat/en/#data/QV)
*[Land Use](http://www.fao.org/faostat/en/#data/RL)
*[Pesticides Use](http://www.fao.org/faostat/en/#data/RP)
*[Crop Residues](http://www.fao.org/faostat/en/#data/GA)



## Inspiration
*[The Environmental Impact of Coffee Production: What’s Your Coffee Costing The Planet?](https://www.sustainablebusinesstoolkit.com/environmental-impact-coffee-trade/)
