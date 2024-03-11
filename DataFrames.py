import pandas as pd 
import matplotlib.pyplot as plt 
from AlphaDash import get_stock_data

stock_data = get_stock_data('AAPL')

df = pd.DataFrame(stock_data['Time Series (Daily)']).T
df['4. close'] = df['4. close'].astype(float)

df['4. close'].plot(title='Stock Closing Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()