# Zindi Challenge for Predicting the Burned Area of Wildfires in Zimbabwe

## 1.0 Overview and Objectives
Each year, thousands of fires blaze across the African continent. Some of the fires occur naturally while others are man-made. But whatever the cause, these fires result in massive damage, such as the loss of lives and property and air pollution through smoke and carbon dioxide emission.

The occurence, rage, and spread of a wildfire is influenced by various factors such as the quantity and dryness of vegetation and wood, humidity, precipitation, solar radiation, temperature, wind, land elevation, and so on.

To better understand the dynamics that influence the magnitude of these fires across Zimbabwe, Zindi has hosted a competition for predicting the burned area in different locations in Zimbabwe over 2014 to 2017.

### 1.1 Problem Statement
From history, wildfires have caused devastating damage and therefore, there is a need to predict where and when they will occur in future across Zimbabwe.

### 1.2 Project Objective
To determine the monthly percentage of burned area in specific square areas across Zimbabwe, over the years 2014 to 2017. 

### 1.3 Perfomance Evaluation
The evaluation metric for this competition is [Root Mean Squared Error](https://zindi.africa/learn/zindi-error-metric-series-what-is-root-mean-square-error-rmse) (RMSE).

We need to predict the proportion of the burned area per squared area, with values ranging from 0 to 1. The lower the RMSE, the better the prediction.

## 2.0 Architecture Diagram
The diagram below illustrates the workflow I followed, from  ETL, transformation, modelling, and evaluation.

![The Data Science Process](https://github.com/user-attachments/assets/3c55dc32-7f75-4158-946b-507dfd9913bc)

## 3.0 ETL Process
### 3.1 Data Source
All the data used in this project was provided by Zindi, which they extracted from the [Google Earth Engine](https://developers.google.com/earth-engine/datasets/). No external data was used. 
Three data csv files were provided for this project:<br>

***a.) Train.csv***<br>
This contains the target feature (burned area) along with 28 other features. It has 29 columns and 83,148 rows. Here is a description of the data features.
1. **ID**: The IDs take the form of [area ID]_yyyy-mm-dd. There are 533 area squares each with a unique ID ranging from 0 to 532
2. **lat**: Latitude of the center of the area
3. **lon**: Longitude of the center of the 
4. **burn_area**: This is the percentage of the burnt area. Zindi has split up Zimbabwe into 533 equal areas, centered around the locations provided in the lat/lon columns. The target variable, burn_area, is the percentage of the area that has been burned in a given month.
5. **climate_aet**: Actual evapotranspiration, derived using a one-dimensional soil water balance model
6. **climate_def**: Climate water deficit, derived using a one-dimensional soil water balance model
7. **climate_pdsi**: Palmer Drought Severity Index
8. **climate_pet**: Reference evapotranspiration (ASCE Penman-Montieth)
9. **climate_pr**: Precipitation accumulation
10. **climate_ro**: Runoff, derived using a one-dimensional soil water balance model
11.**climate_soil**: Soil moisture, derived using a one-dimensional soil water balance model
12. **climate_srad**: Downward surface shortwave radiation
13. **climate_swe**: Snow water equivalent, derived using a one-dimensional soil water balance model
14. **climate_tmmn**: Minimum temperature
15. **climate_tmmx**: Maximum temperature
16. **climate_vap**: Vapor pressure
17. **climate_vpd**: Vapor pressure deficit
18. **climate_vs**: Wind-speed at 10m
19. **elevation**: Land elevation
20. **landcover_0**: Water Bodies: at least 60% of area is covered by permanent water bodies
21. **landcover_1**: Evergreen Needleleaf Vegetation: dominated by evergreen conifer trees and shrubs (>1m). Woody vegetation cover >10%.
22. **landcover_2**: Evergreen Broadleaf Vegetation: dominated by evergreen broadleaf and palmate trees and shrubs (>1m). Woody vegetation cover >10%.
23. **landcover_3**: Deciduous Needleleaf Vegetation: dominated by deciduous needleleaf (larch) trees and shrubs (>1m). Woody vegetation cover >10%.
24. **landcover_4**: Deciduous Broadleaf Vegetation: dominated by deciduous broadleaf trees and shrubs (>1m). Woody vegetation cover >10%.
25. **landcover_5**: Annual Broadleaf Vegetation: dominated by herbaceous annuals (<2m). At least 60% cultivated broadleaf crops.
26. **landcover_6**: Annual Grass Vegetation: dominated by herbaceous annuals (<2m) including cereal croplands.
27. **landcover_7**: Non-Vegetated Lands: at least 60% of area is non-vegetated barren (sand, rock, soil) or permanent snow/ice with less than 10% vegetation.
28. **landcover_8**: Urban and Built-up Lands: at least 30% impervious surface area including building materials, asphalt, and vehicles.
29. **precipitation**: Merged microwave/IR precipitation estimate

***b.) Test.csv***<br>
This file contains all of the columns in the train data except the burn_area column. This is the dataset on which we need to apply our models and predict the target feature. 
The dataset contains 28 columns and 25,584 rows. 

***c.) variable_definitions.csv***<br>
This file describes the variables found in train and test.

### 3.2 Loading
I first uploaded the three data files to a Google Drive subfolder named Competitions which is in a folder named Data_Sc_Software_Eng. I then installed and imported the necessary Python modules for loading the data into dataframes in a Google Colab notebook.

### 3.3 Transformation
Exploration of the data revealed that it had no missing values, duplicates, or odd values that would necessitate transformation. 

To enable more effective analysis and modelling, I created the following columns:<br>
i.) 'date' column by splitting the ID (eg 127_2017-01-03) to get the date string which I then converted to datetime type.<br>
ii.) 'month' column generated from the date column.<br>
iii.) 'year' column generated from the date column.<br>
iv.) The real area ID 'real_id' generated by splitting the ID (eg 127_2017-01-03) to get the area ID

I finally transformed the dataframe into a time series by setting the date column as the index.

## 4.0 Data Modelling
### 4.1 Exploratory Data Analysis
#### 4.1.1 Correlation

![Correlation of predictor variables with the target variable](https://github.com/user-attachments/assets/6403875e-31fb-4025-a01d-7afc322c5f6e)

A plot of the correlation coefficients showed that some predictor features have significant positive correlation with the burned area, some have significant negative correlation, while about a third of them have near zero correlation.<br>

**Top 5 positively correlated features:**<br>
| Feature | Correlation                                                       |
|----------|-----------------------------------------------------------------|
| climate_def       | 0.279511                                                |
| climate_vs        | 0.261562                                                 |
| climate_pet        | 0.168871                                |
| climate_vpd        | 0.219974 |
| climate_srad        | 0.160517 |

**Top 5 negatively correlated features:**<br>
| Feature | Correlation                                                       |
|----------|-----------------------------------------------------------------|
| climate_tmmn       | -0.099436                                                |
| precipitation        | -0.169218                                                 |
| climate_pr        | -0.170532                                |
| climate_aet        | -0.211806 |
| climate_vap        | -0.221348 |

#### 4.1.2 Trend and Seasonality Analysis
Analysis and visualization of the data shows that the mean burned area has monthly and yearly seasonality. 
Time series decomposition of some of the areas reveals that the burned area has a trend, seasonal, and random noise components.

![time_series_decomposition_of_burned_area_in_area_0_train_data](https://github.com/user-attachments/assets/cd3a1b0f-64e5-436c-89ca-45705acd4509)

![Q_Q_plot_of_area78_residuals](https://github.com/user-attachments/assets/eafae6a8-b555-478b-ba7a-e290084c5333)


Observations from the time series decomposition of area IDs 0 and 78:
1. The trend appears relatively stable with small variations.
2. The seasonal component is regular and yearly.
3. The residuals are relatively normally distributed, suggesting that the trend and seasonal components have captured most of the information in the data. Also, working with a p-value of 0.05, Augmented Dickey-Fuller (ADF) Test on the residuals shows that they are stationary and therefore, not statistically significant. 

## 4.2 Models Used
To test the performance of different time series models, I split the train data into train and validation sets. The new train data had all the data from January 2001 to December 2011 while the validation data had all the data from January 2012 to December 2013.

The country is divided into 533 areas and each area has its own historical data. Therefore, to build a time series model, I needed to filter the data per area, build and test the models in a loop, and finally append the RMSE values to a list.

**1. Simple Auto ARIMA model**
Given the seasonal nature of the series, I first built a simple Auto ARIMA model with the seasonal parameter set to True. The overall mean RMSE on the validation set was **0.017446834635150756**

**2. Tuned Auto ARIMA model**
Auto ARIMA allows hyperparameter tuning of autoregressive, differencing, and moving average terms (p, q, and d), test for stationarity of the differencing term, error handling, the seasonal period, and so on. To ensure a robust and efficient process, I initialized Auto ARIMA model with the following parameter settings:<br>
   **m=12** to set the seasonal period.<br>
   **start_p=0**, **start_q=0** to start the parameter search from zero.<br>
   **max_order=5** to limit the maximum combined order of the non-seasonal AR and MA terms (p, q, and d).<br>
   **test='adf'** to use the Augmented Dickey-Fuller test to check stationarity.<br>
   **error_action='ignore'**, **suppress_warnings=True**, and **stepwise=True** to control the tuning process and prevent unnecessary errors/warnings.<br>
   **trace=False** to suppress output tracing.

However, from my tests, I realized that some areas such as 270 and 271 have insufficient variability of burned area data, making it impossible for the model to test and determine an appropriate differencing term, d. Almost all the areas that failed the auto ARIMA model test have only one non-zero value and 155 zeros out of a total of 156 rows.
Therefore, in my modelling, I introduced a try and except block so that areas whose data could not be modelled would be imputed with 0 as the prediction.

The overall mean RMSE on the validation set was **0.015127896730155988**

**3. SARIMAX with specific specific seasonal and non-seasonal terms and exogenous variables**

The SARIMAX (Seasonal Autoregressive Integrated Moving Average + exogenous variables) model stands out as a powerful tool for [modeling and forecasting both trends and seasonal variations in temporal data, while incorporating exogenous variables into the analysis to improve prediction accuracy](https://datascientest.com/en/sarimax-model-what-is-it-how-can-it-be-applied-to-time-series).
*Justification for Exogenous variables:*
The plot of correlation coefficients shows that some features have significant positive correlation while others have significant negative correlation.

Climatic and geographical features may also have individual and combined effects on the occurrence and spread of wildfires. For example, an interaction between climate water deficit (climate_def) and windspeed (climate_vs) could provide insights into how wind speed in dry conditions might affect burned areas. In addition, wild fire depends on some environmental processes that take a long time - for example, there may be more fuel if the previous growing season was a good one.

I therefore, used some of the top correlated features, lagged features, and interaction terms as exogenous variables in a SARIMAX model. I also incorporated a try and except block so that areas whose data could not be modelled would either be modelled using Auto ARIMA or imputed with 0 as the prediction.

The overall mean RMSE on the validation set was **0.015369110259848365**

**4. Univariate SARIMAX with train-test split, constant p, d, and q terms, and Kalman Filter**

I built a univariate SARIMAX model, trained on the burned area data only, but I incorporated a Kalman Filter to help reduce noise in the predictions. I also incorporated a try and except block so that areas whose data could not be modelled would either be modelled using Auto ARIMA or imputed with 0 as the prediction.
I applied the p, d, and q terms obtained from tuning a sample of the areas.

The overall mean RMSE on the validation set was **0.013922985862969662** 

**5. Univariate SARIMAX with train-test split, tuned p, d, and q terms, and Kalman Filter**

I finally built a univariate SARIMAX model with a Kalman Filter, but instead of constant p, q, and d terms, I tuned these terms for each area before training the SARIMAX model.

The overall mean RMSE on the validation set was **0.014198299113235276**

Up to the competition deadline, the univariate SARIMAX model with a Kalman Filter and constant p, d, and q terms gave the lowest RMSE. 

I therefore, retrained this model on the whole train dataset and made predictions on the provided test data.

## 5.0 Inference 
Input data should first be transformed to a time series and added a 'real_id' column following the transformation steps explained in section 3.3 of this documentation. The validation (test) data should also be transformed following the same procedure.

The submission model should be inputted with train data that has a numerical 'burn_area' column, where each row represents the percentage of burned area in each area across Zimbabwe in a specific month. 
The model will make predictions that match the length of the test set per area in a loop and generate a list of series dataframes for each area.

In a separate algorithm, the generated list of predictions will be concatenated into one dataframe in such a manner that, predictions for all areas in a certain month will be grouped together chronologically. This will result in a dataframe whose 'ID' column values match the 'ID' column of the test set. 

The model's performance is evaluated by computing the RMSE of the predictions compared to the actual burned area values. 

## 6.0 Run Time
All the scripts and models were run on a Google Colab CPU. 
Expected run times:
1. Simple Auto ARIMA model: **31 minutes**
2. Tuned Auto ARIMA model: **207 minutes**
3. SARIMAX Model with Exogenous variables: **27 minutes**
4. Univariate SARIMAX with train-test split, constant p, d, and q terms, and Kalman Filter: **17.5 minutes**
5. Univariate SARIMAX with train-test split, tuned p, d, and q terms, and Kalman Filter: **184.5 minutes** 
6. Univariate SARIMAX, constant p, d, and q terms, and Kalman Filter trained on the whole train data (the final submission model): **24.5 minutes**

## 7.0 Performance Metrics
### 7.1 Metrics and KPIs
The evaluation metric for this competition is [Root Mean Squared Error](https://zindi.africa/learn/zindi-error-metric-series-what-is-root-mean-square-error-rmse) (RMSE). The RMSE is the square root of the average squared difference between predicted and actual values (the residuals). Squaring the residuals ensures that all values are positive, thus avoiding them canceling out, while finding the square root ensures that the overall result has the same units as the original data. 

In this challenge, we need to predict the proportion of the burned area per squared area, with values ranging from 0 to 1. The lower the RMSE, the better the prediction.

I did not use any other evaluation metric in ETL and modelling.

**Performance of Auto ARIMA and SARIMAX models**

| Model No. | Model Name                                                        | RMSE with Train-Test Split                    |
|----------|-----------------------------------------------------------------|------------------------------|
| 1        | Simple Auto ARIMA                                                | 0.017446834635150756         |
| 2        | Tuned Auto ARIMA                                                 | 0.015127896730155988         |
| 3        | SARIMAX with exogenous variables                                 | 0.015369110259848365         |
| 4        | Univariate SARIMAX with constant p, d, and q terms and Kalman Filter | 0.013922985862969662         |
| 5        | Univariate SARIMAX with tuned p, d, and q terms and Kalman Filter | 0.014198299113235276         |

### 7.2 Public and private score scores
When trained on the whole train data, my best performing model had these scores:<br>
Public Score- **0.017791797**<br>
Private Score - **0.017090329**

## 8.0 Error Handling and Logging
Analysis of the train data revealed that some areas such as area ID 270 and 271 have insufficient variability of burned area data, making it impossible for the time series models to tune and determine an appropriate differencing term, d, when train-test splitting is applied.

I analyzed all the areas that could not be modelled and realized that out of 156 rows, almost all have only 1 non-zero value and 155 zeros for burned area. For such areas, the most effective solution is a naive prediction of zero burned area. I therefore, incorporated try and except blocks in my models so that areas whose data could not be modelled would be imputed with 0 as the prediction.

However, on retraining the models on the full train data, I realized that only area 35 could not be modelled using SARIMAX but it could be modelled using Auto ARIMA. I therefore, introduced a try and except block in the best-performing SARIMAX model to model this area using Auto ARIMA.

## 9.0 Maintenance and Monitoring
### 9.1 Infrastructural requirements
Reproducibility of modelling and performance is only guaranteed when the train and test datasets are transformed as outlined in section 3.3 and when the same versions of Python libraries are imported. 

I have therefore, generated a requirements file that shows the Python libraries that I used and their versions. 
I also communicate that I built all my scripts on a Google Colab, whose runtime was the CPU. 

### 9.2 Scaling
Given the differences in the nature and seasonal variability of burned area data for different areas, continuous tests would be needed to help decide how to handle odd areas. 

In the model that I submitted, only area 35 could not be modelled using SARIMAX but it could be modelled using Auto ARIMA. I therefore, introduced a try and except block to handle the area using Auto ARIMA.

However, as revealed by my earlier analysis, some areas may have a constant value in all the historical data, affecting time series modelling. A method of predicting such areas will need to be decided upon, which can include imputing with the mode, median, mean, the last value in the historical data, and so on.

Another important challenge in scaling is on deciding the optimal autoregressive, differencing, and moving-average (p,d,q) terms. Different areas have different optimal terms but from my modelling and submission, auto tuning the terms for each area did not necessarily give the best performance. Between auto tuning the terms and trial-and-error terms is a dilemma I could not solve. 

Data Science modelling is both an art and a science, and my best performing model applied the modelling terms that I obtained from a sample of the areas. Scaling would therefore need both auto tuning and trial-and-error sampling.

## 10.0 Further Recommendations
I have accompanied this notebook with an additional notebook that shows the different regressor and time series models that I tried. I tried RidgeCV, RandomForest regressor, Principal Component Analysis, XGBoost regressor, Facebook Prophet, VAR (Vector Autoregressive) models and a simple neural network. I also ran cross-validation of the regressor models. 

They all returned RMSE lower than the SARIMAX model that I used to submit predictions. 

**Performance of regressor and other time series models**
| Model No. | Model Name                                                        | RMSE with Train-Test Split                    |
|----------|-----------------------------------------------------------------|------------------------------|
| 1        | RidgeCV trained with all features                                | 0.026804579066879393         |
| 2        | RidgeCV with all features and standardization                    | 0.026804357891580918         |
| 3        | RidgeCV with  multicollinearity reduction                        | 0.027366536987648862         |
| 4        | RidgeCV with  multicollinearity reduction and standardization | 0.02736881921974534         |
| 5        | RandomForestRegressor with hyperparameter tuning (>=100 estimators) | 0.02285804382129087         |
| 6        | RandomForestRegressor with hyperparameter tuning (>=10 estimators)  | 0.017446834635150756         |
| 7        | RandomForestRegressor trained on PCA transformed data               | 0.024915630133727183         |
| 8        | XGBoost                                 | 0.0223199139035291         |
| 9        | FBProphet | 0.014736724817954457         |
| 10        | VAR with selected features | 0.06510061730326468         |

I would therefore, recommend more advanced models to be trained on the train data to observe whether the performance will improve. These include univariate and multivariate LSTM (Long Short-Term Memory Network), Gradient Boosting Machines (GBM), LightGBM, ensembling of different models, or advanced neural networks.

For univariate models such as ARIMA and SARIMAX, I would recommend more combinations of exogenous variables, lagged features, and interaction terms to be tried. The long computation time hindered me from trying all possible combinations. 

I would also recommend more historical data to be obtained for training the models. Currently, each area has 156 rows of data in the training set, and this is not enough for sufficient training. It is also the reason why the time series models would fail to determine the seasonal variability of the burned area in some areas. 

## Contributors
Leonard Gachimu
