import sklearn
import pickle
import pandas as pd

model = pickle.load(open("predict_fare//flight_rf.pkl", "rb"))


def getFlightPrice(Dep_Time, Arrival_Time, Source, Destination, Stops, Airline):

    Journey_day = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").day)
    Journey_month = int(pd.to_datetime(
        Dep_Time, format="%Y-%m-%dT%H:%M").month)

    Dep_hr = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").hour)
    Dep_min = int(pd.to_datetime(Dep_Time, format="%Y-%m-%dT%H:%M").minute)

    Arr_hr = int(pd.to_datetime(Arrival_Time, format="%Y-%m-%dT%H:%M").hour)
    Arr_min = int(pd.to_datetime(Arrival_Time, format="%Y-%m-%dT%H:%M").minute)

    dur_hr = abs(Dep_hr-Arr_hr)
    dur_min = abs(Dep_min-Arr_min)

    if(Airline == "Air India"):
        Air_India = 1
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "GoAir"):
        Air_India = 0
        GoAir = 1
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "IndiGo"):
        Air_India = 0
        GoAir = 0
        IndiGo = 1
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "Jet Airways"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 1
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "Jet Airways Business"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 1
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "Multiple Carriers"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 1
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "Multiple Carriers Prem Eco"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 1
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "SpiceJet"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 1
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "Trujet"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 1
        Vistara = 0
        Vistara_Premium_economy = 0

    elif(Airline == "Vistara"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 1
        Vistara_Premium_economy = 0

    elif(Airline == "Vistara_Premium_economy"):
        Air_India = 0
        GoAir = 0
        IndiGo = 0
        Jet_Airways = 0
        Jet_Airways_Business = 0
        Multiple_Carriers = 0
        Multiple_Carriers_Prem_Eco = 0
        SpiceJet = 0
        Trujet = 0
        Vistara = 0
        Vistara_Premium_economy = 1

    if(Source == 'Chennai'):
        S_Chennai = 1
        S_New_Delhi = 0
        S_Kolkata = 0
        S_Mumbai = 0

    elif(Source == "New Delhi"):
        S_Chennai = 0
        S_New_Delhi = 1
        S_Kolkata = 0
        S_Mumbai = 0

    elif(Source == "Kolkata"):
        S_Chennai = 0
        S_New_Delhi = 0
        S_Kolkata = 1
        S_Mumbai = 0

    elif(Source == "Mumbai"):
        S_Chennai = 0
        S_New_Delhi = 0
        S_Kolkata = 0
        S_Mumbai = 1

    if(Destination == "Cochin"):
        D_Cochin = 1
        D_Hyderabad = 0
        D_Kolkata = 0
        D_New_Delhi = 0

    elif(Destination == "Hyderabad"):
        D_Cochin = 0
        D_Hyderabad = 1
        D_Kolkata = 0
        D_New_Delhi = 0

    elif(Destination == "Kolkata"):
        D_Cochin = 0
        D_Hyderabad = 0
        D_Kolkata = 1
        D_New_Delhi = 0

    elif(Destination == "New Delhi"):
        D_Cochin = 0
        D_Hyderabad = 0
        D_Kolkata = 0
        D_New_Delhi = 1

    '''['Total_Stops', 'Price', 'Journey_day', 'Journey_month', 'Dep_hour',
       'Dep_minute', 'Arrival_hour', 'Arrival_minute', 'Duration_hour',
       'Duration_minute', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
       'Jet Airways Business', 'Multiple carriers',
       'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
       'Vistara Premium economy', 'Chennai', 'Kolkata', 'Mumbai', 'New Delhi',
       'Cochin', 'Hyderabad', 'Kolkata', 'New Delhi']'''

    price = model.predict([[Stops, Journey_day, Journey_month, Dep_hr, Dep_min,
                          Arr_hr, Arr_min, dur_hr, dur_min, Air_India, GoAir,
                          IndiGo, Jet_Airways, Jet_Airways_Business,
                          Multiple_Carriers, Multiple_Carriers_Prem_Eco,
                          SpiceJet, Trujet, Vistara, Vistara_Premium_economy,
                          S_Chennai, S_Kolkata, S_Mumbai, S_New_Delhi, D_Cochin,
                          D_Hyderabad, D_Kolkata, D_New_Delhi]])

    return round(price[0], 2)
