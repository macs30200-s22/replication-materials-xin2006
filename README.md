# MACSS 30200 replication-materials-xin2006

The impact of COVID-19 containment measures on crime rates: A case study of Chicago.   
Xin Li   

## Introduction
As a social process to be reckoned with, crime is a field that has been explored by many researchers for years, especially regarding trend and casual factors such as population density and employment. In the context of COVID-19, was crime frequency in Chicago affected by the containment measures such as stay-at-home orders that limit people’s mobility? The paper aims to investigate the question using the crime incidents reported by Chicago Data Portal for measuring crime rates and the daily mobility data provided by Apple Report of mobility trend. The analysis relies on methods including SARIMAX model, Granger Causality Test, Pearson Correlation Coefficients and takes the type of crime into consideration. The results suggest that compared to pre-pandemic level, the crime rate in Chicago declined markedly as individuals’ mobility being limited due to COVID-19 containment measures, especially for the first year after the outbreak, and the specific effect was heterogenous by type of crime.    

## Findings
After collecting the crime data from 2015 to 2022 and counting the monthly amount of each type of crime, it can be observed that there is a seasonality in the time series data from crime. Then I use the SARIMA model to forecast the crime rate in the pandemic (2020 to present) and compare the predicted pattern with the actual rate. The results are shown in the following graphs. From the graphs, my initial findings are that the change of domestic crime rate is not so significant, and the non-domestic crime, crime against persons and crime against property declined since 2020, while the deceptive crime increased drametically during the end of 2020 and the start of 2021. 

<img src="./Plot/Domestic Crime.png">
<img src="./Plot/Non-domestic Crime.png">
<img src="./Plot/Crime against Persons.png">
<img src="./Plot/Crime against property.png">
<img src="./Plot/Deceptive Crime.png">

  
The initial findings of the difference between predicted crime and acrual crime rate provide the evidence that the crime rate and pattern is changed in the period of COVID-19, and the change is different from types of crime. And the initial findings enable me to further explore to what degree does crime rate is affected by the containment measures and people's mobility in the pandemic.

## Data and Code
The code is written in Python 3.9.7 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

pip install -r requirements.txt

The orignial crime data comes from [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g). The data [Crimes2015_17.csv] and [Crimes_2018_2022.4.xlsx] are required to run the code, which can be directly download from the Chicago portal with the selection of Date. They are too large to be uploaded here in the Github.  

The monthly count for crime of different type are shown in the table [Count of crime (classified).csv](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/Count%20of%20crime%20(classified).csv).  
  
My code and results of running the code for cleaning crime data and conducting the SARIMA model is shown in the jupyter notebook [Crime Data Process and Analysis.ipynb](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/Crime%20Data%20Process%20and%20Analysis.ipynb). The code for the Granger Causality Tests and Pearson Correlation Coefficients is shown in [method2.py](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/method2.py)

In my final paper for the class, I cite the data of mobility and crime count, and the graphs given by code of SARIMA model, listed in the section after "5.Conclusion".
