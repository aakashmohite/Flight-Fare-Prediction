from django.contrib import admin
from django.urls import path
from predict_fare import views

app_name = 'TaskApp'
urlpatterns = [
    path('', views.predict, name='Predict'),
]
