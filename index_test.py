import streamlit as st
import joblib
import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

"""
## Welcome to Crypto Hub.
*Precise crypto forecasting*

"""

with open('model_test.pkl','rb') as file:
    fb_model = joblib.load(file)


num_of_days = st.number_input('Enter Number of Days to be Predicted from Today')

if st.button("predict"):
    
    # Extract latest bitcoin/USD data from investing.com
    url = 'https://www.investing.com/crypto/bitcoin/btc-usd-historical-data'

    def scrape_bitcoin_data(url, start_date):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the table containing the historical data
        table = soup.find('table', {'class': 'w-full text-xs leading-4 overflow-x-auto freeze-column-w-1'})

        # Extracting data from the table
        bitcoin_data = []
        if table:
            rows = table.find_all('tr')
            for row in rows[1:]:  # Skipping the header row
                columns = row.find_all('td')
                date_str = columns[0].find('time')['datetime']
                date = datetime.strptime(date_str, '%m/%d/%Y').date()
                if date >= start_date:
                    price = columns[1].text.strip().replace(',', '')  # Removing commas from price for numeric value
                    volume = columns[5].text.strip()
                    change = columns[6].text.strip()
                    bitcoin_data.append({'Date': date, 'Price': price, 'Vol.': volume, 'Change %': change})

        return bitcoin_data

if __name__ == "__main__":
    # CREATE THE INITIAL DATAFRAME
    bitcoin_df = pd.read_csv("bitcoin_data.csv")

    # Convert Date column to time series 
    bitcoin_df['Date'] = pd.to_datetime(bitcoin_df['Date'])

    # Set date column as the index
    bitcoin_df.set_index('Date', inplace=True)

    date_today = pd.Timestamp.today().date()
    # Extract the last date from the current dataset, format it
    last_date = bitcoin_df.tail(1).index[0]

    # # Extract data only if start date is older than today
    if last_date.date() < date_today:
        # start date is one day after the last date
        last_date_plus_one = last_date + pd.DateOffset(days=1)
        start_date = datetime.strptime(last_date_plus_one.strftime('%m/%d/%Y'), '%m/%d/%Y').date()
        bitcoin_data = pd.DataFrame(scrape_bitcoin_data(url, start_date))
        
        # PREPOROCESSING
        # Strip suffix letters from volume column and convert to respective numeric figure
        for index, row in bitcoin_data.iterrows():
            if 'K' in row['Vol.']:
                row_value = round(float(row['Vol.'].strip('K')) * 1000)
                bitcoin_data.at[index, 'Vol.'] = row_value
            elif 'M' in row['Vol.']:
                row_value = round(float(row['Vol.'].strip('M')) * 1000000)
                bitcoin_data.at[index, 'Vol.'] = row_value
            elif 'B' in row['Vol.']:
                row_value = round(float(row['Vol.'].strip('B')) * 1000000000)
                bitcoin_data.at[index, 'Vol.'] = row_value  
                  
        # Remove percentage sign from the 'Change' column
        bitcoin_data['Change %'] = bitcoin_data['Change %'].str.replace('%', '')
        
        # Convert price, volume, and change columns to float
        bitcoin_data[['Price', 'Vol.', 'Change %']] = bitcoin_data[['Price', 'Vol.', 
                                                                    'Change %']].astype(float)
        # Drop duplicate rows
        bitcoin_data.drop_duplicates(inplace=True)
        
        # CONVERTING TO TIME SERIES
        # Convert Date column to time series 
        bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'])
        
        # Sort by date in descending order
        bitcoin_data.sort_values(by='Date', ascending=True, inplace=True)
        
        # Set date column as the index
        bitcoin_data.set_index('Date', inplace=True)
    
        # REMOVING OUTLIERS
        # Filter rows with volume above 50,000,000
        bitcoin_data = bitcoin_data[bitcoin_data['Vol.'] < 50000000]
        # Filter rows with change below -50% and above 50%
        bitcoin_data = bitcoin_data[(bitcoin_data['Change %'] > -50) & (bitcoin_data['Change %'] < 50)]
        
        # Add the data to the previous preprocessed time series
        bitcoin_df = pd.concat([bitcoin_df, bitcoin_data])

        # Update the preprocessed dataset file
        bitcoin_df.to_csv('bitcoin_data.csv')

        # REMOVING TRENDS
        # Difference the price column
        price_diff = bitcoin_df['Price'].diff(periods=1)
        # Replace Price column in a copy of dataset with differenced price
        bitcoin_df_copy = bitcoin_df.copy()
        bitcoin_df_copy['Price'] = price_diff 
        # Drop null values
        bitcoin_df_copy.dropna(inplace=True)
                         
    # BUILDING A TIME SERIES MODEL
    # Fetch the last date in the new bitcoin time series
    last_day = bitcoin_df.index[-1]
    
    # Increment the last date by one day to get the start date for forecasting
    start_date = last_day + pd.DateOffset(days=1)

    # Create a DataFrame with future dates starting from the next day
    future = pd.DataFrame({'ds': pd.date_range(start=start_date, periods=num_of_days)})

    # Generate forecasts
    fb_forecast = fb_model.predict(future)

    # Rename 'ds' as 'Date'
    fb_forecast = fb_forecast.rename(columns = {'ds': 'Date'})
    
    # Set date column as index
    fb_forecast.set_index('Date', inplace=True)

    # REMOVING 1-LAG DIFFERENCING
    for index, row in fb_forecast.iterrows():
        if index == min(fb_forecast.index):
            # Set the first forecasted value to the last observed price in the bitcoin time series
            true_forecast = bitcoin_df.iloc[-1]['Price'] + fb_forecast.iloc[0]['yhat']
            fb_forecast.at[index, 'yhat'] = true_forecast
        else:
            # Update subsequent forecasted values based on the previous adjusted values
            prev_true_forecast = fb_forecast.at[index - pd.DateOffset(days=1), 'yhat']
            current_yhat = fb_forecast.at[index, 'yhat']
            true_forecast = prev_true_forecast + current_yhat
            fb_forecast.at[index, 'yhat'] = true_forecast

    """
    ## Number of Days to be Predicted
    """
    num_of_days

    """
    ## Predicted Bitcoin Prices in USD
    """

    fb_forecast['yhat']
    st.line_chart(fb_forecast['yhat'])