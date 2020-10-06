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

        requested = requested_amount
        interest = ponderated_rate/initial_amount
        total_interest = requested+(requested*(interest*(((1+interest)**36))/(((1+interest)**36)-1)))
        compound = 1 + interest
        returna = "Requested Amount : {}".format(requested_amount)
        returnb = "Rate:  {:.1f}%".format(interest*100)
        returnc = "Monthly Repaiments: {:.2f}".format(((requested*(interest*(((1+interest)**36)))/(((1+interest)**36)-1))))
        returnd = "Total Repaiments: {}".format((requested+(requested*(interest*(((1+interest)**36))/(((1+interest)**36)-1)))))

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

        requested = requested_amount
        interest = ponderated_rate/initial_amount
        total_interest = requested+(requested*(interest*(((1+interest)**36))/(((1+interest)**36)-1)))
        compound = 1 + interest
        dflender.dropna(inplace = True)
        returna = "Requested Amount : {}".format(requested_amount)
        returnb = "Rate:  {:.1f}%".format(interest*100)
        returnc = "Monthly Repaiments: {:.2f}".format(((requested*(interest*(((1+interest)**36)))/(((1+interest)**36)-1))))
        returnd = "Total Repaiments: {}".format((requested+(requested*(interest*(((1+interest)**36))/(((1+interest)**36)-1)))))
        dflender.to_csv("../DATA/market_ex.csv")
        print(returna)
        print(returnb)
        print(returnc)
        print(returnd)

        
