import config
import robin_stocks.robinhood as r
import matplotlib.pyplot as plt
import pandas as pd


def init():
    r.login(config.username, config.password)
    return r.account.build_holdings()

def returns(holdings):
    total_returns = 0
    for key in holdings:
        total_returns += float(holdings[key]["equity_change"])
    return round(total_returns,2)

def write(holdings):
    cols = list(holdings.keys())
    rows = list(holdings[cols[0]].keys())

    with open("data.csv","w") as f:
        f.write(F"\t,{' , '.join(cols)}\n")
        for row in rows:
            f.write(F"{row},{' , '.join([str(holdings[col][row]) for col in cols])}\n")
        f.write(F"Total Returns ,  {returns(holdings)}")

def graphReturns(holdings):
    stocks = list(holdings.keys())
    returns_ = [float(holdings[stock]["equity_change"]) for stock in stocks]
    plt.bar(stocks,returns_,color="#00c805",width=0.45,label=F"Total Returns: ${returns(holdings)}")
    plt.xlabel("Stocks")
    plt.ylabel("$ Total Returns")
    plt.legend()
    plt.title("Returns per stock")

if __name__ == "__main__":
    holdings = init()
    write(holdings)
    graphReturns(holdings)
    plt.show()

