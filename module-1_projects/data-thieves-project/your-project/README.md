<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Bike Sharing Network
*Lena Frommann, Georgios Papadopoulos, Niki Zarucha*

*DATA ft, BER, 10/19*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Database](#database)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
We chose to review bike sharing options in different cities worldwide. We therefore considered the city, in which the companies are present and with another, much bigger dataframe, we managed to add additional information to the previous one.

## Questions & Hypotheses
We want to display the bike sharing companies which are the most popular ones within the bike sharing industry.<br/>
We want to figure out, which cities have the most bike sharing opportunities and if those cities are the ones with the highest population.<br/>
Before starting to code, we assumed it is possible, that the more populated cities have less options, because it also depends on the infrastructure, the city offers for bicycles. It needs to be questioned if bikes can be used everywhere.

## Dataset
The sources used are attached below.<br/>
We used an open API and a csv-Datafile from kaggle.<br/>
While selecting data, it was important to us, that geographical data (coordinates) is provided, to be able, to make further investigations based on this in the future. <br/>
**Bike Sharing API:** <br/>
This dataset has the following columns: <br/>
* city
* country
* latitude
* longitude
* company
* href
* id
* name 
* (source)
* (license)
* (gbfs_href)
<br/>
() = Columns that were dropped immediately.

It has the shape (640, 8).

**Population Dataset from Kaggle:** <br/>
This dataset has the following columns: <br/> 
* Country
* AccentCity
* Region
* Population 
* Latitude
* Longitude <br/> 

It has the shape (3.173.958, 7).

## Database
Our Database, the **Bike Sharing Network** has the following columns:  <br/>
* Company
* href
* id
* Name
* City
* Country
* Latitude
* Longitude
* Population

It has the shape (646, 9).

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
* renamed cleaned csv file
* world map html link
* README.md file

## Links
Include links to your repository, slides and kanban board. Feel free to include any other links associated with your project.

[Repository]: <br/>
https://github.com/Nikitsatsiki/data-ber-10-19/tree/master/module-1_projects/data-thieves-project

[Slides]:   
https://docs.google.com/presentation/d/1nSgW6A5Jk74jCGRKpderM9GuxM3DanDWYIIcB2WSyv0/edit?usp=sharing <br/>

Used API: <br/>
CityBikes API Documentation<br/>
http://api.citybik.es/v2/

Used Dataset: <br/>
World Cities Database<br/>
A database of coordinates for countries and cities <br/>
https://www.kaggle.com/max-mind/world-cities-database
