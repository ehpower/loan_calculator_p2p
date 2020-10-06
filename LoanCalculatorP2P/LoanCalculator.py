import pandas as pd
import numpy as np

def borrow(amount, update = True):
    i = 0
    initial_amount = amount
    dflender = pd.read_csv("../DATA/market_ex.csv", sep = ",")
    dflender = dflender.sort_values(by="Rate").reset_index(drop=True).copy(deep=True)
    requested_amount = 0
    number_borrowers = 0
    ponderated_rate = 0
    cost_borrowing = []
    if (amount > 15000) or (amount < 100):
        return "Quantity not accepted"
    elif amount > dflender["Available"].sum():
        return "Insufficient funds"
    elif update == False:
        while amount > 0:
            if amount == dflender["Available"][i]:
                requested_amount += dflender["Available"][i]
                amount -= dflender["Available"][i]
                ponderated_rate += dflender["Rate"][i]*dflender["Available"][i]
                number_borrowers +=1
            elif amount > dflender["Available"][i]:
                requested_amount += dflender["Available"][i]
                amount -= dflender["Available"][i]
                ponderated_rate += dflender["Rate"][i]*dflender["Available"][i]
                number_borrowers +=1
            elif amount < dflender["Available"][i]:
                requested_amount += amount
                ponderated_rate += dflender["Rate"][i] * amount
                amount -= dflender["Available"][i]
                number_borrowers +=1
            i = i+1

        rate = ponderated_rate/initial_amount
        interest_per_period = rate/12
        denominador = ((1 + interest_per_period)**36)-1
        payment_per_month = requested_amount*((interest_per_period*(1 + interest_per_period)**36)/denominador)
        total_payment = payment_per_month*36
        returna = "Requested Amount : {}".format(requested_amount)
        returnb = "Rate:  {:.1f}%".format(rate*100)
        returnc = "Monthly Repaiments: {:.2f}".format(payment_per_month)
        returnd = "Total Repaiments: {}".format(total_payment)

        print(returna)
        print(returnb)
        print(returnc)
        print(returnd)
    #This section returns the information necessary for the borrower.
    #Now we will update the dataframe so that the lenders are removed from the DF.
    elif update == True:
        while amount > 0:
            if amount == dflender["Available"][i]:
                requested_amount += dflender["Available"][i]
                amount -= dflender["Available"][i]
                ponderated_rate += dflender["Rate"][i]*dflender["Available"][i]
                dflender["Available"][i] = np.nan
            elif amount > dflender["Available"][i]:
                requested_amount += dflender["Available"][i]
                amount -= dflender["Available"][i]
                ponderated_rate += dflender["Rate"][i]*dflender["Available"][i]
                dflender["Available"][i] = np.nan
            elif amount < dflender["Available"][i]:
                requested_amount += amount
                to_subtract = amount
                ponderated_rate += dflender["Rate"][i] * amount
                amount -= dflender["Available"][i]
                dflender["Available"][i] = dflender["Available"][i] - to_subtract
            i = i+1

        rate = ponderated_rate/initial_amount
        interest_per_period = rate/12
        denominador = ((1 + interest_per_period)**36)-1
        payment_per_month = requested_amount*((interest_per_period*(1 + interest_per_period)**36)/denominador)
        total_payment = payment_per_month*36
        returna = "Requested Amount : {}".format(requested_amount)
        returnb = "Rate:  {:.1f}%".format(rate*100)
        returnc = "Monthly Repaiments: {:.2f}".format(payment_per_month)
        returnd = "Total Repaiments: {}".format(total_payment)
        dflender.dropna(inplace = True)
        dflender.to_csv("../DATA/market_ex.csv")
        print(returna)
        print(returnb)
        print(returnc)
        print(returnd)
        
