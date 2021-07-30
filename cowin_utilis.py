import json
import requests
import sys
import datetime


def by_pin(pin,date_par):
    pin_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode="+str(pin)+"&date="+ str(date_par) + ".json"
    try:
        jpdata = requests.get(pin_url)
        res = jpdata.status_code
    except requests.exceptions.RequestException as e:
        print("Error Occured")
        print(e)
        sys.exit()


    if res == 200:
        jpdata = jpdata.text
        pdata = json.loads(jpdata)
        #print(len(data["centers"]))
        if len(pdata["sessions"]) == 0:    ## execute this if there is no slot availbale
            print("No slots available")
            sys.exit()
        #print(pdata["sessions"])

        print("State :",pdata['sessions'][0]["state_name"],end=" / ")
        print("District :",pdata['sessions'][0]["district_name"])
        

        for session in pdata['sessions']:
            print(session["name"])
            if not session["min_age_limit"] == 18:continue
            print("Address :",session["address"])
            print("Block :",session["block_name"])
            
            print("Date :",session["date"])
            print("Availibility :",session["available_capacity"],end=" >> ")
            print("Dose 1 :",session["available_capacity_dose1"],end=" / ")
            print("Dose 2 :",session["available_capacity_dose2"])
            print("Age :",session["min_age_limit"])
            print("Vaccine :",session["vaccine"])
            print("slot timing :") 
            for slot in session["slots"]: print(slot, end="  ")
            print("")
            print("End of session")



def test():
    print("Shino cool")




def by_id(dist_id,date_par):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id="+str(dist_id)+"&date="+date_par+".json"
    print(url)
    try:
        jdata = requests.get(url)
        res = jdata.status_code
    except requests.exceptions.RequestException as e:
        print("Error Occured")
        print(e)
        sys.exit()


    if res == 200:
        jdata = jdata.text
        data = json.loads(jdata)
        #print(len(data["centers"]))
        if len(data["centers"]) == 0:    ## execute this if there is no slot availbale
            print("No slots available")
            sys.exit()
        print(data["centers"][0]["state_name"])
        for center in data['centers']:
            print(center["name"])
            for session in center["sessions"]:
                if not session["min_age_limit"] == 18:continue
                print("Date :",session["date"])
                print("Availibility :",session["available_capacity"],end=" >> ")
                print("Dose 1 :",session["available_capacity_dose1"],end=" / ")
                print("Dose 2 :",session["available_capacity_dose2"])
                print("Age :",session["min_age_limit"])
                print("Vaccine :",session["vaccine"])
                print("slot timing :") 
                for slot in session["slots"]: print(slot, end="  ")
                print("")
                print("End of session")
                print("#################################")
            print("NEXT CENTER")
            print("    ")



#Vaccine Availibility Search tool. by Shino Winson
