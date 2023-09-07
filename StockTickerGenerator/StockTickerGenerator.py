# Import necessary libraries
import pandas_datareader as pdr
import datetime
import pandas as pd

# Define a function to get stock data
def getStock(stk):

    # Display a separator
    print("\n************************************************************")

    # Get the current date
    dt = datetime.date.today()

    # Calculate the past date based on user input (requestedDays)
    dtPast = dt + datetime.timedelta(days=-requestedDays)

    # Print a header for the analysis
    print("\nDaily Percent Changes - " + str(dtPast) + " to "
          + str(dt) + " " + "* " + str(stockPick.upper()) + " *")

    # Display a separator
    print("\n*************************************************************")

    # Fetch stock data from Yahoo Finance API
    df = pdr.get_data_yahoo(stk,
                            start=datetime.datetime(
                                dtPast.year, dtPast.month, dtPast.day),
                            end=datetime.datetime(dt.year, dt.month, dt.day))

    # Initialize a new column for percent change in close prices
    df['Close % Change'] = 0.0

    # Get the index of the new column
    closeChangeIndex = len(df.keys()) - 1

    # Iterate through the dataframe to calculate close price changes
    for i in range(0, len(df)):
        closeValuelast = df.iloc[-1]['Close']
        closeValueSecondLast = df.iloc[-2]['Close']
        df.iat[i, closeChangeIndex] = (
            closeValuelast - closeValueSecondLast)/closeValueSecondLast

    # Initialize a new column for percent change in volume
    df['Volume % Change'] = 0.0

    # Get the index of the new column
    volumeChangeIndex = len(df.keys()) - 1

    # Iterate through the dataframe to calculate volume changes
    for i in range(0, len(df)):

        volumeValuelast = df.iloc[-1]['Volume']
        volumeValueSecondLast = df.iloc[-2]['Volume']

        df.iat[i, volumeChangeIndex] = (
            volumeValuelast - volumeValueSecondLast)/volumeValueSecondLast

    # Define a list of columns to keep in the dataframe
    newColumnList = ['Close', 'Volume', 'Volume % Change', 'Close % Change']
    df = df[newColumnList]

    return df

# Start an interactive menu loop
while True:
    print("\n---------------------------------------------------\n")
    print("Stock Report Menu Options")
    print("\n---------------------------------------------------\n")

    print("1. Report changes for a stock ")
    print("2. Quit")

    answer = int(input())
    if answer == 1:

        print("\nPlease enter the stock symbol:")
        stockPick = str(input())

        while True:
            try:
                print("\nPlease enter the number of days for the analysis:")
                requestedDays = int(input())

                df = getStock(stockPick.upper())
                print(df)

                dt = datetime.date.today()

                dtPast = dt + datetime.timedelta(days=-requestedDays)

                firstClosePrice = df.iloc[0]['Close']
                lastClosePrice = df.iloc[-1]['Close']

                firstVolumeValue = df.iloc[0]['Volume']
                lastVolumeValue = df.iloc[-1]['Volume']

                # Calculate percentage changes in close prices and volume
                pctClosePriceChange = (
                    firstClosePrice - lastClosePrice)/lastClosePrice
                pctVolumeChange = (firstVolumeValue -
                                   lastVolumeValue)/lastVolumeValue

                # Round the percentage changes to 3 decimal places
                roundedClosePriceChange = round(pctClosePriceChange, 3)
                roundedVolumePriceChange = round(pctVolumeChange, 3)

                # Display a summary of cumulative changes
                print(
                    "\n----------------------------------------------------------------")
                print("Summary of Cumulative Changes for " + stockPick)
                print("---------------------------------------------------------------")
                print(str(dtPast) + " to " + str(dt))

                print('\n% Volume Change: ' + str(roundedVolumePriceChange))
                print('\n% Close Price Change: ' +
                      str(roundedClosePriceChange))

                break

            except ValueError:
                print(
                    "\n** Your response is not recognized. Please only enter numerical values and try again. **")

    else:
        break
