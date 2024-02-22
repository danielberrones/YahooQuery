import yahooquery
import matplotlib.pyplot as plt
import pandas as pd

symbol = 'tsla'
output = yahooquery.Ticker(symbol)

close = output.history()['close']
close = close.reset_index()
close['date'] = pd.to_datetime(close['date']) 

plt.figure(figsize=(10, 6))
plt.plot(close['date'],close['close'],marker='o') 
plt.show()
