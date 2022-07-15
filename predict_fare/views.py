from django.shortcuts import render, HttpResponse
from predict_fare import prediction
# Create your views here.


def predict(request):
    if request.method == "POST":
        Dep_Time = request.POST['Dep_Time']
        Arrival_Time = request.POST['Arrival_Time']
        Source = request.POST['Source']
        Destination = request.POST['Destination']
        Stops = request.POST['Stops']
        Airline = request.POST['Airline']

        price = prediction.getFlightPrice(
            Dep_Time, Arrival_Time, Source, Destination, Stops, Airline)
        text = "Your flight price is: " + str(price)
        return render(request, 'predict_ui.html', {'prediction_text': text})
    return render(request, 'predict_ui.html')
