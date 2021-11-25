#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:37:06 2021

@author: jardieljunior
"""

import pandas as pd
import numpy as np
import historical_prices

class Risk(historical_prices.Equities):
    
    def __init__(self):
        
        self.equities = historical_prices.Equities.__init__(self)
        self.getEquitiesPrices()
        
        
    @staticmethod
    def VaR(df):
        var_df = pd.DataFrame()
        
        for t in df['ticker'].unique():
            df = df.loc[df['ticker']==t]
            
            var_95 = df['return'].quantile(0.05)
            
            result = pd.DataFrame({'ticker': t, 
                                         'VaR 95': var_95}, index=[0])
            
          
            
            var_df = var_df.append(result)
            
            
        return var_df
            
    
    def stress(self):
        
        pass
    
    
    
if __name__ == '__main__':
    
    x = Risk()
    var = x.VaR(x.hist_equities_prices)
    