from django.urls import path
from .views import Heart_Disease_Prediction_View,dashboard,Diabetes_Disease_Prediction_View,Kidney_Disease_Prediction_View,Liver_Disease_Prediction_View
urlpatterns=[

    path('heart/',Heart_Disease_Prediction_View,name="heart"),
    path('liver/',Liver_Disease_Prediction_View,name="liver"),
    path('diabetes/',Diabetes_Disease_Prediction_View,name="diabetes"),
    path('kidney/',Kidney_Disease_Prediction_View,name="kidney"),
    path('dashboard/',dashboard,name='dashboard')
]