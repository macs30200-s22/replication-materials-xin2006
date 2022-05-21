import pandas as pd
import numpy as np
from scipy.stats import pearsonr
from statsmodels.tsa.stattools import grangercausalitytests

# Load the data frame
df = pd.read_csv(r'Count of crime (classified).csv')

# Granger Causality Tests
def granger(crime_type,lag):
    '''
    Inputs: 
        crime_type: a speficied string refering to a certain type of crime
        lag: the maximum lags considering in the test
    Outputs: 
        The result of Granger Causality Tests
    '''
    
    return grangercausalitytests(df[[crime_type,'Mobility']], maxlag=n)

# Pearson Correlation Coefficients
def pearson(crime_type,lag):
    '''
    Inputs: 
        crime_type: a speficied string refering to a certain type of crime
    Outputs: 
        The result of Pearson Correlation Coefficient
    '''

    return pearsonr(df['Mobility'], df[crime_type])[0]
