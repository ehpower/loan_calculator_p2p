import pandas as pd
import numpy as np

def borrow(amount):
    i = 0
    x = amount
    dflender = pd.read_csv("../DATA/market_example.csv", sep = ";")
    dflender = dflender.sort_values(by="Rate").reset_index(drop=True).copy(deep=True)
    cost_borrowing = []
    while amount > 0:
        if amount == dflender["Available"][i]:
            cost_borrowing.append(amount * dflender["Rate"][i])
            amount -= dflender["Available"][i]
        elif amount < dflender["Available"][i]:
            cost_borrowing.append(amount * dflender["Rate"][i])
            amount -= dflender["Available"][i]
        elif amount > dflender["Available"][i]:
            cost_borrowing.append((amount-(amount-dflender["Available"][i])) * dflender["Rate"][i])
            amount -= dflender["Available"][i]
        i = i+1

    interest = (np.sum(cost_borrowing))/x
    returna = "the total cost of borrwing will be {}".format(np.sum(cost_borrowing))
    returnb = "the total interest will be {}".format(interest)
    return returna, returnb
