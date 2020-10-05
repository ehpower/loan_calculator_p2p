import pandas as pd
import numpy as np

def borrow(amount):
    i = 0
    initial_amount = amount
    dflender = pd.read_csv("../DATA/market_example.csv", sep = ";")
    dflender = dflender.sort_values(by="Rate").reset_index(drop=True).copy(deep=True)
    cost_borrowing = []
    if (amount > 15000) or (amount < 100):
        return "Quantity not accepted"

    elif amount > dflender["Available"].sum():
        return "insufficient funds"
    else:
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
    requested = initial_amount
    interest = ((np.sum(cost_borrowing))/initial_amount)
    returna = "Requested Amount : {}".format(requested)
    returnb = "Rate:  {:.1f}%".format(interest*100)
    returnc = "Monthly Repaiments: {:.2f}".format((interest*requested)/12)
    returnd = "Total Repaiments: {}".format((requested* interest)+requested)

    print(returna, returnb, returnc, returnd)
