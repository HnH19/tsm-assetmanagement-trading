# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import matplotlib.pyplot as plt
from pypfopt import CLA, plotting 



df = pd.read_excel('hist_pivot.xlsx', parse_dates=True)

# df = raw_data[['Close', 'Date', 'ticker']]
# 
df = df.set_index('Date')

portfolio = df
return_stocks = portfolio.pct_change()
return_stocks



stocks = df.columns
number_of_portfolios = 10000

RF = 0

portfolio_returns = []
portfolio_risk = []
sharpe_ratio_port = []
portfolio_weights = []

for portfolio in range (number_of_portfolios):
    weights = np.random.random_sample((len(stocks)))

    #below line ensures that the sum of our weights is 1
    
    weights = weights / np.sum(weights)
    
    
    
    annualize_return = np.sum((return_stocks.mean() * weights) * 252)
    
    portfolio_returns = np.append(portfolio_returns,annualize_return)
    # portfolio_returns.append(annualize_return)
    #variance
    matrix_covariance_portfolio = (return_stocks.cov())*np.sqrt(252)
    portfolio_variance = np.dot(weights.T,np.dot(matrix_covariance_portfolio, weights))
    portfolio_standard_deviation= np.sqrt(portfolio_variance) 
    portfolio_risk = np.append(portfolio_risk, portfolio_standard_deviation)
    # portfolio_risk.append(portfolio_standard_deviation)
    #sharpe_ratio
    sharpe_ratio = ((annualize_return- RF)/portfolio_standard_deviation)
    
    sharpe_ratio_port = np.append(sharpe_ratio_port, sharpe_ratio)
    # sharpe_ratio_port.append(sharpe_ratio)
    
    #keep weights as well to find out later the weights from the optimized portfolio
    portfolio_weights.append(weights)
    
    
    portfolio_risk = np.array(portfolio_risk)
    portfolio_returns = np.array(portfolio_returns)
    sharpe_ratio_port = np.array(sharpe_ratio_port)
    
        
plt.figure(figsize=(10, 5))
plt.scatter(portfolio_risk, portfolio_returns, c=portfolio_returns / portfolio_risk) 
plt.xlabel('volatility')
plt.ylabel('returns')
plt.colorbar(label='Sharpe ratio')



porfolio_metrics = [portfolio_returns,portfolio_risk,sharpe_ratio_port, portfolio_weights] 
#from Python list we create a Pandas DataFrame
portfolio_dfs = pd.DataFrame(porfolio_metrics)
portfolio_dfs = portfolio_dfs.T
#Rename the columns:
portfolio_dfs.columns = ['Port Returns','Port Risk','Sharpe Ratio','Portfolio Weights']

#convert from object to float the first three columns.
for col in ['Port Returns', 'Port Risk', 'Sharpe Ratio']:
    portfolio_dfs[col] = portfolio_dfs[col].astype(float)
    
    
#portfolio with the highest Sharpe Ratio
Highest_sharpe_port = portfolio_dfs.iloc[portfolio_dfs['Sharpe Ratio'].idxmax()]
#portfolio with the minimum risk 
min_risk = portfolio_dfs.iloc[portfolio_dfs['Port Risk'].idxmin()]







