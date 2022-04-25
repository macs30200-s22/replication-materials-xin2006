# MACSS 30200 replication-materials-xin2006
Xin Li

## Introduction
In the project, my research question is “How containment measures in the context of Covid-19 pandemic impact the crime rate and pattern in Chicago?”. The project aims to explore the change of criminal activity in the City of Chicago that caused by the containment measures regarding social distancing, such as lockdowns and WFH in the COVID-19 pandemic. By obtaining the monthly data about crime count, COVID-19 policy, and mobility trend, I would perform quantitative analysis based on time series to figure out how, when, and to what extend does the crime impacted by the social distancing.

## Initial Findings:
After collecting the crime data from 2015 to 2022 and counting the monthly amount of each type of crime, it can be observed that there is a seasonality in the time series data from crime. Then I use the SARIMA model to forecast the crime rate in the pandemic (2020 to present) and compare the predicted pattern with the actual rate. The results are shown in the following graphs. From the graphs, my initial findings are that the change of domestic crime rate is not so significant, and the non-domestic crime, crime against persons and crime against property declined since 2020, while the deceptive crime increased drametically during the end of 2020 and the start of 2021. 

<img src="./Plot/Domestic Crime.png">
<img src="./Plot/Non-domestic Crime.png">
<img src="./Plot/Crime against Persons.png">
<img src="./Plot/Crime against property.png">
<img src="./Plot/Deceptive Crime.png">

  
The initial findings of the difference between predicted crime and acrual crime rate provide the evidence that the crime rate and pattern is changed in the period of COVID-19, and the change is different from types of crime. And the initial findings enable me to further explore to what degree does crime rate is affected by the containment measures and people's mobility in the pandemic.

## Data and Code
The orignial crime data comes from [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g).  

The montly count for crime of different type are shown in the table [Count of crime (classified).csv](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/Count%20of%20crime%20(classified).csv).  
  
My code for cleaning crime data and conducting the SARIMA model is .The code is written in Python 3 and the files [Crimes2015_17.csv] and [Crimes_2018_2022.4.xlsx] are required in running the code.

In my final paper for the class, I would cite the data of crime count and the graphs given by code of SARIMA model.
