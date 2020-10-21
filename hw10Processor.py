import pandas as pd

fb = pd.read_csv("FB.csv")
aapl = pd.read_csv("AAPL.csv")
msft = pd.read_csv("MSFT.csv")
nflx = pd.read_csv("NFLX.csv")
goog = pd.read_csv("GOOG.csv")

dateData = fb["Date"]
fbPriceData = fb["Close"] 
aaplPriceData = aapl["Close"]
msftPriceData = msft["Close"]
nflxPriceData = nflx["Close"]
googPriceData = goog["Close"]

symbols = ["FB", "AAPL", "MSFT", "NFLX", "GOOG"]

data = []
i = 0 
while i < len(fbPriceData):
    fbPrice, aaplPrice, msftPrice, date = fbPriceData[i], aaplPriceData[i], msftPriceData[i], dateData[i]
    nflxPrice, googPrice = nflxPriceData[i], googPriceData[i]
    pSet = [fbPrice, aaplPrice, msftPrice, nflxPrice, googPrice] 
    for j in range(len(symbols)):
        symbol = symbols[j]
        p = pSet[j]
        data.append([date, p, symbol])

    i += 1

newDf = pd.DataFrame(data, columns=["Date", "Close",
                                    "Symbol"])
newDf.to_csv("MiniStockData.csv")

