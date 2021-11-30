#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:37:06 2021

@author: jardieljunior
"""

import pandas as pd
import numpy as np
import historical_prices
import math

class Risk(historical_prices.Equities):
    
    def __init__(self):
        
        self.equities = historical_prices.Equities.__init__(self)
        self.getEquitiesPrices()
        
    
    def portfolioVaR(self):
        
        self.total_portfolio = self.eq_portfolio.copy()
        self.total_portfolio['weights'] = self.total_portfolio['amount']/self.total_portfolio['amount'].sum()
    
    
    @staticmethod
    def VaR(df):
        
        def calculateEWMAVol(ReturnSeries, Lambda=0.94):   
            SampleSize = len(ReturnSeries)
            Average = ReturnSeries.mean()
        
            e = np.arange(SampleSize-1,-1,-1)
            r = np.repeat(Lambda,SampleSize)
            vecLambda = np.power(r,e)
        
            sxxewm = (np.power(ReturnSeries-Average,2)*vecLambda).sum()
            Vart = sxxewm/vecLambda.sum()
            EWMAVol = math.sqrt(Vart)
    
            return (EWMAVol)
        
        
        var_df = pd.DataFrame()
        
        for t in df['ticker'].unique():
            
            temp = df.loc[df['ticker']==t]
            
            vol = temp['return'].std()
            
            vol_ewma = calculateEWMAVol(temp['return'])
            
            avg = temp['return'].mean() 

            var_95 = temp['return'].quantile(0.05)
                    
            y = np.random.normal(avg,vol_ewma, 100000)
            
            
            result = pd.DataFrame({'ticker': t, 
                                         'VaR 95': np.quantile(y, 0.05)}, index=[0])
    
            
            var_df = var_df.append(result)
            
            
        return var_df
    
    
    
    def stress(self):
        
        pass
    
    
    
if __name__ == '__main__':
    
    x = Risk()
    var = x.VaR(x.hist_equities_prices)
    