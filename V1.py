from lunchable import LunchMoney, TransactionInsertObject
import csv
import pandas as pd
import time
from pathlib import Path
import os

# You will find the documentation under this link: 

# Enter your access token below. You can generate it here: https://my.lunchmoney.app/developers
# Replaze XYZ with your token
token = "XYZ"


def main():
    # Loop through the rows of the excel
    df = pd.read_excel(filepath)
    
    for index, row in df.iterrows():

        # Get the accountname and and amount       
        Accountnamecurrent = row['Accountname']
        Amountcurrent = row['Amount']

        # Calls get_assetid() function to get the assetid based on the name of the account
        try:
            IDcurrent = (get_assetid(Accountnamecurrent))
        except:
            print("Something went wrong while getting the ID from the Asset. Did you use the same account name as in LunchMoney?")

        
        # Calls the update_asset() function to update the amount based on the ID gathered previously
        try:

            update_asset(IDcurrent,Accountnamecurrent,Amountcurrent)
        except:
            print("Something went wrong while updating the Asset amount. Did you use total numbers?")
        
        
    print("Update successful. Program will exit in 10 seconds")
    time.sleep(10)


def get_assetid(Accountnamecurrent):
    
    # Get all assets from lunchmoney
    allassets = lunch.get_assets()

    # Builds a dictionary of all assets
    dict = {}
    internalid = 0
    for a in allassets:
        internalid += 1
        dict[internalid] = {}
        for b in a:
            dict[internalid][b[0]] = b[1]

    # Loop through assets to find the ID based on the name
        
    for asset in dict:

        for k,v in dict[asset].items():
            
            if v == Accountnamecurrent:
                foundassetid = asset
                break
                
            else:
                continue

            print(asset)
    assetidtemp = dict[foundassetid]["id"]
    return assetidtemp

       
            



def update_asset(IDcurrent,Accountnamecurrent,Amountcurrent):
    # Updates the asset amount
    print("Updating: " + Accountnamecurrent + " value = " + str(Amountcurrent))
    try:
        lunch.update_asset(IDcurrent,balance=Amountcurrent)
    except:
        print("error updating" + Accountnamecurrent)

# Global variables for token and input excel 

lunch = LunchMoney(access_token=token)
filepath = os.path.dirname(os.path.abspath(__file__)) + "\input.xlsx"
main()


