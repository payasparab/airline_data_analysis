'''
Title: data_analysis_tools.py
Author: @payasparab (me@payasparab.com) 
Description: Set of tools used to process airline delay and revenue data

Key Methods: 


'''


import pandas as pd
import numpy as np



def import_flight_data():
    '''
    Method to import raw data on flights arrivals
    '''

    #TODO : make it possible to pull directly from web.
    data = pd.read_csv('raw_data.csv')
    data = data.dropna(axis=1, how='all')

    data.columns = [c.strip() for c in data.columns]


    return data


def import_revenue_data():

    '''
    Method to import income statement revenue data from Sharadar    
    '''
    pass

def import_options_data():
    '''
    Method to import options data from Interactive Brokers API
    '''
    pass

