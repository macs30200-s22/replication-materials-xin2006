[![DOI](https://zenodo.org/badge/480984639.svg)](https://zenodo.org/badge/latestdoi/480984639)

# MACSS 30200 replication-materials-xin2006

## The impact of COVID-19 containment measures on crime rates: A case study of Chicago.   

Xin Li   

The code is written in Python 3.8.8 and all of its dependencies can be installed by running the following in the terminal (with the requirements.txt file included in this repository):

```
pip install -r requirements.txt
```


## Project Introduction
As a social process to be reckoned with, crime is a field that has been explored by many researchers for years, especially regarding trend and casual factors such as population density and employment. In the context of COVID-19, was crime frequency in Chicago affected by the containment measures such as stay-at-home orders that limit people’s mobility? The paper aims to investigate the question using the crime incidents reported by Chicago Data Portal for measuring crime rates and the daily mobility data provided by Apple Report of mobility trend. The analysis relies on methods including SARIMAX model, Granger Causality Test, Pearson Correlation Coefficients and takes the type of crime into consideration. The results suggest that compared to pre-pandemic level, the crime rate in Chicago declined markedly as individuals’ mobility being limited due to COVID-19 containment measures, especially for the first year after the outbreak, and the specific effect was heterogenous by type of crime.     

## Data Processing

The orignial crime data comes from [Chicago Data Portal](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g). 
Use the ```Crime Data.ipynb```

 to process the original crime data including data cleaning and crime grouping. The monthly count for crime of different type after cleaning are shown in the table [type_crime.csv](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/type_crime.csv).     

## Model Conducting

You can then use [method1.py](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/method1.py) and [method2.py](https://github.com/macs30200-s22/replication-materials-xin2006/blob/main/method2.py) to reproduce the findings related to the relationship between mobility and crime rates. To run the code, the file type_crime.csv needs to be downloaded in the same path.  

## Findings
Firstly, from the comparison of observed and forecast pattern, there is an overall decrease of crime frequency, but the specific change varies from types of crime, which is shown in the following plots. Secondly, the mobility in response of containment measures under COVID-19 is tested to be one of the reasons for the change of crime rates in Chicago with heterogeneous effects by crime type. 


<img src="./Plot/Domestic Crime.png">
<img src="./Plot/Non-domestic Crime.png">
<img src="./Plot/Crime against Persons.png">
<img src="./Plot/Crime against property.png">


### Citation
In my final paper for the class, I cite the data of mobility and crime count, and the graphs given by code of SARIMA model, listed in the section after "5.Conclusion".
