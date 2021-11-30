#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:38:37 2021

@author: jardieljunior
"""


import yfinance as yf
import os 
import pandas as pd


BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

class Portfolio:
    
    
    def __init__(self):
        
        self.portfolio = pd.read_excel(os.path.join(BASE_PATH, 'portfolio.xlsx'))
        


class Equities(Portfolio):
    
    def __init__(self):
        
        Portfolio.__init__(self)
        
        self.eq_portfolio = self.portfolio.loc[self.portfolio['asset_type']
                                               =='equity']
        
        
    def getEquitiesPrices(self):
        final = pd.DataFrame()
        for t in self.eq_portfolio['ticker'].unique():
            yahoo_data = yf.Ticker(t)
            df = yahoo_data.history(period='max').reset_index()
            df['return'] = df['Close'].pct_change()
            df['ticker'] = t
            final = final.append(df)
            self.hist_equities_prices = final
        self.hist_equities_prices.to_excel('hist_prices.xlsx')
            
            