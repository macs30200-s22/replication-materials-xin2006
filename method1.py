import numpy as np
import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt 
import csv
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.api as sm

count = pd.read_csv('type_crime.csv')

def sarima(type_str):
    '''
    Produce the predicted pattern using SARIMA model
    
    Input: 
        type_str: the string that specify the type of crime,
                    including 'Total Crime','Domestic Crime', 'Non-domestic Crime', 
                    'Crime against persons', 'Crime against property'.
    Output: a dataframe consisting of month and count
        
    '''

    crime_all=pd.DataFrame(count,
                       columns=['Month', type_str])
    crime_all.index = pd.to_datetime(crime_all['Month'])
    crime_all.drop(columns='Month',inplace=True)
    model=sm.tsa.statespace.SARIMAX(crime_all[type_str],order=(1, 1, 1),seasonal_order=(1,1,1,12))
    results=model.fit()
    crime_all['forecast']=results.predict(start="2020-03-01",end="2022-03-01",dynamic=True)
    crime_all[[type_str,'forecast']].plot(figsize=(12,8))
    plt.xlabel('Month', size=18)
    plt.ylabel('Monthly Count', size=15)
    plt.vlines("2020-03-26",ymin=9000, ymax=23000, color='grey', linestyles = "dashed", label='S')
    plt.vlines("2020-05-01",ymin=9000, ymax=23000, color='grey', linestyles = "dashed", label='S')
    plt.vlines("2020-11-16",ymin=9000, ymax=23000, color='grey', linestyles = "dashed", label='S')
    plt.vlines("2021-01-20",ymin=9000, ymax=23000, color='grey', linestyles = "dashed", label='S')