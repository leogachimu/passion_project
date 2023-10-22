# Phase 2 Project

# BUSINESS ANALYSIS OF HOUSE SALES IN KING COUNTY, WASHINGTON 
## AUTHOR: 
*1. Leonard Gachimu*<br>

Flatiron School Data Science Program

Due date: 11/09/2023

Technical Mentor: **Stella Waithera**

![Forbes](https://imageio.forbes.com/specials-images/imageserve/62437975bb1b55afcd4ab6ab/real-estate-concept/960x0.jpg)

## PROJECT OVERVIEW

This project seeks build a multiple linear regression model for a real estate agency that will help homeowners buy and/or sell homes in King County, Washington.

## BUSINESS PROBLEM

> King County, being the home of Seattle, the most advanced and populous city in Washington and the 13th most populous in the USA, has a competitive real estate industry.

>As such, there is a complex and dynamic relationship among many factors that affect the market value of real estate property. These factors include the weather season, the location of the property, the grade of the house, the presence of a scenic view, the number of floors, the age of the house, various dimensions such as the size of the interior living space, and the size of the lot.

>For a real estate firm, the challenge is to make informed pricing decisions that will account for all the complex interrelated factors. This can lead them to **misadvise home buyers** and sellers as well as **unnecessary loss of business** opportunities and reputation.

>My project seeks to help [Team Howlett Real Estate Agents](https://www.teamhowlett.com/), a real estate agency in King County, make more informed and data-driven pricing strategies for homes in King County.
## BUSINESS UNDERSTANDING
**Specific Factors that Influence the Price of a Home in King County:**
1.	Location-specific conditions include traffic, freeway access, noise, crime, sun exposure, views, parking, neighboring homes, vacant lots, access to quality schools, parks, shops, restaurants.
2.	Condition - the overall condition of the house affects its market value.
3.	Grade is a classification by construction quality which refers to the types of materials used and the quality of workmanship. It is regulated by the King County Local government.
4.	Various dimensions in square feet, such as the size of the interior living space, the lot, the basement, as well the average dimension of neighboring houses.
5.	The number of bedrooms and bathrooms.
6.	Presence of a scenic view.
7.	The age of the house.
8.	If the house is old, whether it has ever been renovated.

## Introducing [Team Howlett Real Estate Agents](https://www.teamhowlett.com/)
This is a real estate agency in King County, Washington, that guides buyer and sellers through the entire real estate transaction, from start to finish.

## BUSINESS OBJECTIVES
To complete this project, my main business objectives will be the following:
>To build a data analytics model for Team Howlett Real Estate Agents, a real estate agency that helps homeowners buy and/or sell homes in King County, Washington.<br>

>To develop a model that will help in identifying the set of attributes that will realize the best value to a home buyer and optimal returns to the home seller.<br>

>To provide insight to homeowners and buyers about:<br>
i.) How weather seasons may affect the sales volume and mean sale price of homes in King County.<br>
ii.) How the grade of a house may affect the sales volume and mean sale price of homes in King County.<br>
iii.) How the number of bedrooms affect the sales volume and mean sale price of homes in King County.<br>

>To find out whether there is a variation in sales volume and mean sale prices across different locations in King County.

## STUDY QUESTIONS
1. What is the relationship between weather season and sales performance?<br>
2. Which is the best weather season to buy a house?<br>
3. Which are the best performing house grades?<br>
4. What is the optimal range of a house grade for different budgets?<br>
5. What is the relationship between number of bedrooms and sales performance?<br>
6. What is the optimal range of bedrooms for different budgets?<br>
7. Which set of variables has the highest influence on the sale price of a house?<br>
8. How are the house prices and house sale volumes distributed around the county?
## DATA UNDERSTANDING
The dataset kc_house_data.csv, has **21,597 rows** and **21 columns**. Below is a description of the variables in the dataset.
| Column           | Description                                                                                       |
|------------------|---------------------------------------------------------------------------------------------------|
| **id**               | Identification for a house                                                                        |
| date             | Date house was sold                                                                               |
| price            | Sale price for a house, which is the target variable                                             |
| bedrooms         | Number of bedrooms                                                                                |
| bathrooms        | Number of bathrooms                                                                               |
| sqft_living      | Size of living area in square feet                                                                |
| sqft_lot         | Size of the lot in square feet                                                                    |
| floors           | Total number of floors (levels) in the house                                                      |
| waterfront       | '1' if the property has a view to a waterfront, '0' if not                                       |
| view             | A rating of Fair, Average, Good, Excellent depending on the view of the property                  |
| condition        | Overall condition of the house                                                                    |
| grade            | An index from 1 to 13 indicating the quality level of construction and design                     |
| sqft_above       | Square footage of the house excluding the basement                                               |
| sqft_basement    | Square footage of the basement                                                                    |
| yr_built         | Year the house was built                                                                          |
| yr_renovated     | Year when the house was last renovated. '0' if it has never been renovated                       |
| zipcode          | 5-digit zip code of the house                                                                     |
| lat              | Latitude coordinate                                                                               |
| long             | Longitude coordinate                                                                              |
| sqft_living15    | Average size of interior living space of the 15 closest houses, in square feet                    |
| sqft_lot15       | Average size of the land lots for the 15 closest houses, in square feet  

## METHODOLOGY
Execution of the project involved the following:

### Data Understanding and Cleaning
I explored the datasets to understand their schema, size, data types, and examine the presence of invalid or inconsistent data such as missing values, duplicates, placeholders, and outliers.

### Data Transformation
I transformed the data into DataFrames using the Pandas library in Python and performed different transformations and analyses to suit.

### Feature Engineering
Based on the avaliable variables, I engineered new variables that would better suit my analysis and modelling.

### Data Analysis 
I analyzed the relationship between the most influential predictor variables and price, which is the response variable. 

### Hypothesis Testing
I tested the statistical significance of the various findings from my analysis.

### Multiple Regression Modelling
I built the best-fitting model for inferring the relationship between predictor variables and the response variable.

### Data Visualization
I used various visualization methods such as bar plots, histograms, and scatter plots to display my findings and facilitate interpretation.

### Data Interpretation
I interpreted the various findings and visualizations to build a recommendation for a real estate agency.

## THE FINDINGS
### 1. The relationship between weather season and sales performance

![Distribution of sales volume by month](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/68d8ca9e-0d1e-4ae6-b955-002a5aeb2ef0)

My analysis reveals that there is a significant variation in the volume of sales across the months in year.<br>
i.) January and February starts off the year with low sales of around **1,000 houses per month**.<br>
ii.) The volume starts to rise in March, where it is about **1,500 houses**.<br>
iii.) From April to July, the volume is about **2,000 houses per month**.<br>
iv.) May has the highest volume at above **2,000 houses**.<br>
v.) The volume starts to decline to around **1,700 houses** in August and **1,500 houses** in September.<br>
vi.) There is a slight increase in October, but the price then drops through November and December.

![Distribution of mean sale price by month](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/a311d00d-af9e-42e3-a0b0-b0fe9fdee95b)

The distribution of mean sale prices over the months in a year also shows that there are significant differences.<br>
i.) The months of January and February have lower mean prices of between **$500,000** and **$525,000**.<br>
ii.) The mean price from March to August is around **$550,000** or higher. April has the highest mean price of above **$550,000**.<br>
iii.) The mean price drops slightly in August and September, rises slightly in October, and then drops again in November and December.<br>
### 2. Relationship between house grade and sales performance

![Distribution of sales volume by grade](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/40bf1241-f1d0-4638-86dd-b8c312847343)

My analysis of sales volume by grade appears to follow a normal distribution with grade 7 having the peak sales volume of about **8,000 houses**. The lower grades of 3, and 4, and the higher grades of 11 and 12 each have sales volumes around **100** or fewer.

![Distribution of mean sale price by grade](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/8f714ddd-5634-42d1-8489-a7ea486936e5)

My analysis has also shown that there is a significant difference in mean sale price among different house grades. Between grade 3 and 8, the mean price is between **$250,000** to **$500,000**. From grade 9 to 13, the mean sale price rises from around **$600,000** to over **$3,500,000**.

### 3. The relationship between number of bedrooms and sales performance
On all social media platforms and social environments, almost everyone wants to know the number of bedrooms when they're scouting for houses. I, therefore, saw the need to find out if there is a relationship between the number of bedrooms and sales perfomance.

My analysis of the relationship between sales and number of bedrooms shows that buyers and sellers have two major factors to consider:<br>
i.) The sales volume, which follows a normal distribution with a peak volume of **8,000 houses** at the median number of 3 bedrooms.<br>

![Distribution of sales volume by number of bedrooms](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/312e4db1-87b3-4928-8b84-3a706b0c7af7)

ii.) The distribution of mean sale price by number of bedrooms, which shows that the peak mean price is **$1,200,000** at 8 bedrooms. For houses with 3 bedrooms, the mean price is only **$465,000**.<br>

![Distribution of mean sale price by number of bedrooms](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/84a74027-035d-44b8-8909-a0af704e18d3)

### 4. The set of variables has the highest influence on the sale price of a house

![Regression Plots of the Best Fitting Multiple Linear Regression Model](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/52e8011b-2116-44f9-a042-52a17d4f7f85)

From my regression modelling, I found out that the five influential factors affecting house sale volume and mean sale price are:

i.) The size of the interior living area in square feet<br>
ii.) The grade of the house, which is a classification by construction quality<br>
iii.) The square footage of the house excluding the basement<br>
iv.) The average size of interior living space for the closest 15 houses, in square feet<br>
v.) The number of bathrooms<br>

### 5. Distribution of house prices and house sale volumes around the county
I created a heatmap that shows that the top 20 locations in count of sales are in the north western region of Seattle.

![Heatmap for the Distribution of Top House Sale Volumes in King County](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/d4da93d0-f81f-45b8-a39a-be310f0f4682)

I also created a heatmap that reveals that all the top 10 mean sale prices came from the north western region of Seattle.

![Heatmap for the Distribution of Top Mean House Sale Price in King County](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/a5064611-c13a-4a46-a3d7-7eca0bf62215)

This trend is to be expected, since Seattle is the most populous and most advanced city in King County and in the Washington State in general. Therefore, the number of homes on sale, the demand for houses, and the ability to purchase more expensive homes is to be found in Seattle.

### 6. 3D Scatter Plots
3D scatter plots of different combinations of the most influential predictor variables show a high correlation among them.

![3D Scatter Plots](https://github.com/leogachimu/dsc-phase-2-project/assets/122081776/3f87234b-5bcb-4dd3-b90d-e2ccbb047aed)

3D scatter plot 1 shows that at different grades, the sale price increases with an increase in both sqft_living and sqft_above. However, the count of sales is denser between grade 6 and 8, and at the lower levels of both sqft_living and sqft_above.

3D scatter plot 2 shows that the sale price increases with an increase in sqft_living, sqft_above, and number of bathrooms. However, the count of sales is denser at the lower levels of all the three variables.

3D scatter plot 3 shows that different grades, the sale price increases with an increase in both sqft_living and sqft_living15. However, the count of sales is denser between grade 5 and 8, and at the lower levels of both sqft_living and sqft_living15.

3D scatter plot 4 shows that different grades, the sale price increases with an increase in both the number of bathrooms and sqft_living. However, the count of sales is denser between grade 6 and 8, and also between 3 and 5 bedrooms at the lower levels of sqft_living.

## CONCLUSION
### The Set of Variables with the Highest Effect on Sales and Mean Sale Price

From my regression modelling, I found out that the five influential factors affecting house sale volume and mean sale price are:<br>
i.) The size of the interior living area in square feet<br>
ii.) The grade of the house, which is a classification by construction quality<br>
iii.) The square footage of the house excluding the basement<br>
iv.) The average size of interior living space for the closest 15 houses, in square feet<br>
v.) The number of bathrooms<br>

### Seasonal Variation of Sales Performance

The northwestern States are characterized by sub-zero degree Winter months, which leads to more people looking to sell their houses so that they can move to warmer regions in the south. There are also fewer potential buyers during the colder months.

My analysis reveals that there is a variation in the volume of sales across the months in year.<br>

i.) January and February starts off the year with low sales of around **1,000 houses per month**.<br>
ii.) The volume starts to rise in March, where it is about **1,500 houses**.<br>
iii.) From April to July, the volume is about **2,000 houses per month**.<br>
iv.) May has the highest volume at above **2,000 houses**.<br>
v.) The volume starts to decline to around **1,700 houses** in August and **1,500 houses** in September.<br>
vi.) There is a slight increase in October, but the price then drops through November and December.

This trend coincides with the seasons in the USA. Winter runs from December to Mid-March, and the Northwestern States being colder, people tend to move to warmer southern states or countries.<br>

Spring runs from mid-March to mid-June, while Summer runs from June to August. During this period, a significant number of people may move back to the northwestern states, thus raising the demand for houses.<br>

Finally, Fall, which runs from September to December, heralds the start of another cold season, at which people start moving out of the northwestern states.<br>

The distribution of mean sale prices over the months in a year also shows that there are significant differences.<br>
i.) The months of January and February have lower mean prices of between **$500,000** and **$525,000**.<br>
ii.) The mean price from March to August is around **$550,000** or higher. April has the highest mean price of above **$550,000**.<br>
iii.) The mean price drops slightly in August and September, rises slightly in October, and then drops again in November and December.<br>

### Grade

Grade is a classification by construction quality which refers to the types of materials used and the quality of workmanship. It is regulated by the King County Local government, and therefore, this is an important factor to anyone looking to buy a house.

My analysis of sales volume by grade appears to follow a normal distribution with grade 7 having the peak sales volume of about 8,000 houses. The lower grades of 3, and 4, and the higher grades of 11 and 12 each have sales volumes around 100 or fewer.

My analysis has also shown that there is a significant difference in mean sale price among different house grades. Between grade 3 and 8, the mean price is between **$250,000** to **$500,000**. From grade 9 to 13, the mean sale price rises from around **$600,000** to over **$3,500,000**.

### Number of Bedrooms

On all social media platforms and social environments, almost everyone wants to know the number of bedrooms when they're scouting for houses. I, therefore, saw the need to find out if there is a relationship between the number of bedrooms and sales perfomance.

My analysis of the relationship between sales and number of bedrooms shows that buyers and sellers have two major factors to consider:

i.) The sales volume, which follows a normal distribution with a peak volume of 8,000 houses at the median number of 3 bedrooms.<br>
ii.) The distribution of mean sale price by number of bedrooms, which shows that the peak mean price is **$1,200,000** at 8 bedrooms. For houses with 3 bedrooms, the mean price is only **$465,000**.

### Distribution of Sales and Mean Sale Prices by Location

The heatmap showing the top 20 in count of sales shows that the north western region of Seattle has the most dense concentration of zipcodes with top 20 in sales volume.

The heatmap showing the locations with top 10 mean prices also reveals that all the top 10 mean sale prices came from the north western region of Seattle.

This trend is to be expected, since Seattle is the most populous and most advanced city in King County and in the Washington State in general. Therefore, the number of homes on sale, the demand for houses, and the ability to purchase more expensive homes is to be found in Seattle.

## RECOMMENDATIONS TO TEAM HOWLETT REALTORS
For a home buyer to realize the best value their home buyer and a seller or for Team Howlett Reators to fetch optimal returns, they should give higher consideration to these five factors:<br>
i.) The size of the interior living area in square feet<br>
ii.) The grade of the house, which is a classification by construction quality<br>
iii.) The square footage of the house excluding the basement<br>
iv.) The average size of interior living space for the closest 15 houses, in square feet<br>
v.) The number of bathrooms

I would advise a buyer to consider buying a house in the offpeak months of January, February, September, October, November, or December, since this is the period they're likely to get a significant discount.
To a seller, I would advise them to consider selling in the peak months from March to August, since this is the period when the demand is high and they're also likely to sell at a significant margin compared to the offpeak months.

There is a significant difference in mean sale price between different house grades. Therefore, if a buyer wants a low-budget house of around $500,000 or less, I would advise them to consider houses between grade 3 and 8. If they have the budget for a more expensive house above $500,000, I would advise them to go for between grade 9 and 13.
For a seller wishing to fetch the highest price in the market, they should go for grade 13 houses. If they want to sell low-priced houses quickly, then they should sell houses with between grades 3 and 8.

If a buyer wants a low-budget house (between $300,000 and $700,000), I would advise them to consider houses with between 1 and 4 bedrooms. If they have the budget for a more expensive house above $800,000, I would advise them to go for between 5 and 10 bedrooms.
For a seller wishing to fetch the highest price in the market, they should go for 8-bedroom houses. If they want to sell low-priced houses quickly, then they should sell houses with between 1 and 4 bedrooms.

If a buyer wants a wider variety of high-grade homes on sale, they should search in Seattle region. However, this is also the region with the highest mean sale price.
Therefore, overall the highest real estate business is to be found in Seattle and the northwestern region of the King County in general.

## STUDY LIMITATIONS

My best multiple linear regression model achieved an R-squared value of 0.546 and an overall p-value of 0.00. These metrics suffice for the present inferential modelling but are lower than the standard required for predictive modelling which would require at least an R-squared of 0.8.

I did not have data about the profitability per sale. Therefore, I could not ascertain whether the distribution of mean sale price or the sales volume correlates with profitability.
Moreover, buildings of better quality (higher grade) cost more to build per unit of measure and therefore, it could be possible that their profitability is not as high as lower-grade houses.

I did not have data about proximity to amenities such as schools, transport infrastructure, and so on, and therefore, I could not determine how they would affect sales performance.

The data is not augmented with data about enabling factors such as the state of the economy in the County and the prevailing interest rates.

## RECOMMENDATIONS FOR FUTURE RESEARCH

Future studies should get data about profitability of the house sales, so as to find out the relationship between sales performance and profitability. This would provde a real estate agency with more solid advice about sales performance.

Future studies should also find out proximity of amenities such as schools, and transport infrastructure. These could be confounding variables that could have skewed the sales performance. Also, the current report does not help a buyer to know if a house of their choice will afford them proximity to these important amenities.

Augmenting the dataset with data about more enabling factors such as the state of the economy in County and the interest rates. This would enable a seller to know the best times to sell and when not to sell. It would also inform a buyer about the best times to buy or take up mortgage.

## FOR MORE INFORMATION

For further analysis and the highlights, kindly visit the following:
1. My Jupyter notebook file titled king_county_house_sales.ipynb in this repository.
2. My presentation pdf in this repository. Kindly, if the pdf does not open the first time, please reload it and it will be rendered.
3. My presentation webpage at this link [https://arcg.is/9LDnb](https://arcg.is/9LDnb) 

