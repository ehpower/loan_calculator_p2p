import pandas as pd
import numpy as np

def borrow(amount, dflender):
    i = 0
    cost_borrowing = []
    while amount > 0:
        if amount == dflender["cash_available"][i]:
            cost_borrowing.append(amount * dflender["rate"][i])
            amount -= dflender["cash_available"][i]
        elif amount < dflender["cash_available"][i]:
            cost_borrowing.append(amount * dflender["rate"][i])
            amount -= dflender["cash_available"][i]
        elif amount > dflender["cash_available"][i]:
            cost_borrowing.append((amount-(amount-dflender["cash_available"][i])) * dflender["rate"][i])
            amount -= dflender["cash_available"][i]
        i = i+1

    return(np.sum(cost_borrowing))
