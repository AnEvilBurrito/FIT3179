import pandas as pd

fb = pd.read_csv("FB.csv")
aapl = pd.read_csv("AAPL.csv")
msft = pd.read_csv("MSFT.csv")

dateData = fb["Date"]
fbPriceData = fb["Close"] 
aaplPriceData = aapl["Close"]
msftPriceData = msft["Close"]

symbols = ["FB", "AAPL", "MSFT"]

data = []
i = 0 
while i < len(fbPriceData):
    fbPrice, aaplPrice, msftPrice, date = fbPriceData[i], aaplPriceData[i], msftPriceData[i], dateData[i]
    pSet = [fbPrice, aaplPrice, msftPrice] 
    for j in range(len(symbols)):
        symbol = symbols[j]
        p = pSet[j]
        data.append([date, p, symbol])

    i += 1

newDf = pd.DataFrame(data, columns=["Date", "Close",
                                    "Symbol"])
newDf.to_csv("MiniStockData.csv")

