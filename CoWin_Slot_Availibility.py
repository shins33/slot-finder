import json
import requests
import sys
import datetime
from cowin_utilis import *

sel = input("Use Default ? (Default = Port Blair) y or n ? : ")
if sel == 'y':
    dist_id = 2
    date_par = datetime.datetime.today().strftime('%d-%m-%Y')
else:
    dist_id = input("Enter District ID \n or p to search by PIN : ")
    if dist_id == 'p' : pin = input("Enter PIN code: ")
    
    date_par = input("Enter Date as dd-mm-yyyy or t for today: ")


    if date_par == 't':
        date_par = datetime.datetime.today().strftime('%d-%m-%Y')

    elif len(date_par) != 10:
        print("Inalid date format")
        sys.exit()
    else:
        dd = date_par[0:2]
        mm = date_par[3:5]
        yy = date_par[6:]

    if dist_id == 'p': 
        by_pin(pin,date_par)
        sys.exit()

    try:
        dist_id = int(dist_id)
    except:
        print("Enter valid ID")
        sys.exit()

by_id(dist_id,date_par)

#by Shino Winson

