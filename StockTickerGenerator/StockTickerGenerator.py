import pandas_datareader as pdr
import datetime 
import pandas as pd

def getStock(stk):
                
    print("\n************************************************************")
    
    dt = datetime.date.today() 
    
    dtPast = dt + datetime.timedelta(days= -requestedDays ) 
    
    print("\nDaily Percent Changes - " + str(dtPast) + " to " 
          + str(dt) + " " + "* " + str(stockPick.upper()) + " *")
    
    print("\n*************************************************************")
    
    df = pdr.get_data_yahoo(stk, 
    
         start= datetime.datetime(dtPast.year, dtPast.month, dtPast.day), 
    
         end  = datetime.datetime(dt.year, dt.month, dt.day)) 
    
    
    df['Close % Change'] = 0.0
    
    
    closeChangeIndex = len(df.keys()) - 1
    
     # iterate through the dataframe and assign one cell at a time.
    
    for i in range(0, len(df)):
        closeValuelast = df.iloc[-1]['Close']
        closeValueSecondLast = df.iloc[-2]['Close']    
        df.iat[i,closeChangeIndex] = (closeValuelast - closeValueSecondLast)/closeValueSecondLast
     
        
    df['Volume % Change'] = 0.0 
    
    volumeChangeIndex = len(df.keys()) - 1
    
    for i in range(0, len(df)):
        
        volumeValuelast = df.iloc[-1]['Volume']
        volumeValueSecondLast = df.iloc[-2]['Volume']    
    
        df.iat[i,volumeChangeIndex] = (volumeValuelast - volumeValueSecondLast)/volumeValueSecondLast
         
    
    newColumnList = ['Close','Volume','Volume % Change', 'Close % Change'  ]
    df = df[newColumnList]
    
    return df

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
    
                dtPast = dt + datetime.timedelta(days= -requestedDays )
              
      
                firstClosePrice = df.iloc[0]['Close']
                lastClosePrice = df.iloc[-1]['Close']
                
                firstVolumeValue = df.iloc[0]['Volume']
                lastVolumeValue = df.iloc[-1]['Volume']
            
                
                pctClosePriceChange = (firstClosePrice - lastClosePrice)/lastClosePrice
                pctVolumeChange = (firstVolumeValue - lastVolumeValue)/lastVolumeValue
                
                roundedClosePriceChange = round(pctClosePriceChange, 3)
                roundedVolumePriceChange = round(pctVolumeChange, 3)
                
                print("\n----------------------------------------------------------------")
                print("Summary of Cummulative Changes for " + stockPick)
                print("---------------------------------------------------------------")
                print(str(dtPast) + " to " + str(dt) )
                
                                
                print('\n% Volume Change: ' + str(roundedVolumePriceChange))
                print('\n% Close Price Change: ' + str(roundedClosePriceChange))
                
                break
            
            except ValueError:
                print("\n** Your response is not recognized. Please only enter numerical values and try again. **")
                
    
                                        
    else:
        break