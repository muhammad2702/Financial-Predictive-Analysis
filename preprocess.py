import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 10)
def kendall_correlation(data, num_entries):
    num = np.zeros(num_entries)

#Utizing Kendall Correlation Formula

    for i in range(num_entries):
        for j in range(i):
            print(data[i] - data[j])
            num[i] -= np.sign(data[i] - data[j])

    return num


price_data = pd.read_csv("BTC-USD.csv")
print(price_data)
num_entries = len(price_data)

#Extracting Close Price Data and applying kendall_correlation()

close= price_data.iloc[:len(price_data),4]
print(close)
correlation = kendall_correlation(close,num_entries)

#Adding the new data to the dataframe

price_data['NET'] = correlation

#Caculating the target labels for the price (0 if price goes down and 1 if the price goes up)

array = price_data['Closing Price'].to_numpy()
for i in range(num_entries):
    array[i] = np.where(array[i] > array[i+1], 0, 1)
price_data['Sign'] = array
price_data.to_csv('filtered_prices_2021.csv', index=False)
