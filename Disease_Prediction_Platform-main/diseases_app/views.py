from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import HeartDiseasePrediction, KidneyDiseasePrediction, DiabetesDiseasePrediction, LiverDiseasePrediction
from django.contrib import messages
# Create your views here.
import numpy
import joblib
from django.core.mail import send_mail


@login_required(login_url='login')
def Heart_Disease_Prediction_View(request):
    heart_model = joblib.load('data_science\heart\model.pkl')

    result = None
    predicted_result_for_heart_disease = None
    if request.method == "POST":
        user = request.user
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        chest_pain_type = request.POST.get('chest_pain_type')
        resting_bp = request.POST.get('resting_bp')
        cholestrol = request.POST.get('cholestrol')
        fasting_blood_sugar = request.POST.get('fasting_blood_sugar')
        resting_electrocardiographic_results = request.POST.get(
            'resting_electrocardiographic_results')
        thalach = request.POST.get('thalach')
        exercise_included_angina = request.POST.get('exercise_included_angina')
        oldpeak = request.POST.get('oldpeak')
        slope = request.POST.get('slope')
        ca = request.POST.get('ca')
        thal = request.POST.get('thal')

        features = [age, sex, chest_pain_type, resting_bp, cholestrol, fasting_blood_sugar,
                    resting_electrocardiographic_results, thalach, exercise_included_angina, oldpeak, slope, ca, thal]

        float_conversion = [float(val) for val in features]

        prediction_features = [numpy.array(float_conversion)]

        prediction = heart_model.predict(prediction_features)
        predicted_result_for_heart_disease = prediction[0]
        prediction = HeartDiseasePrediction.objects.create(
            user=user, age=age, sex=sex, chest_pain_type=chest_pain_type, resting_bp=resting_bp, cholestrol=cholestrol,
            fasting_blood_sugar=fasting_blood_sugar, resting_electrocardiographic_results=resting_electrocardiographic_results, thalach=thalach, exercise_included_angina=exercise_included_angina, oldpeak=oldpeak, slope=slope, ca=ca, thal=thal, predicted_result_for_heart_disease=predicted_result_for_heart_disease)

        # prediction = prediction.save()
        prediction.save()
        print(predicted_result_for_heart_disease, prediction)
        messages.success(request, "Predicted Successfully!!!")

    context = {
        'result': result,
        'predicted_result': predicted_result_for_heart_disease
    }
    return HttpResponse("Result")


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'main_index.html')


@login_required(login_url='login')
def Kidney_Disease_Prediction_View(request):
    kidney_model = joblib.load('data_science\kidney\model.pkl')

    result = None
    predicted_result_for_kidney_disease = None
    if request.method == "POST":
        user = request.user
        age = request.POST.get('age')
        blood_pressure = request.POST.get('blood_pressure')
        specific_gravity = request.POST.get('specific_gravity')
        albumin = request.POST.get('albumin')
        sugar_degree = request.POST.get('sugar_degree')
        red_blood_cells = request.POST.get('red_blood_cells')
        blood_glucose_random = request.POST.get('blood_glucose_random')
        blood_urea = request.POST.get('blood_urea')
        serum_creatinine = request.POST.get('serum_creatinine')
        sodium = request.POST.get('sodium')
        potassium = request.POST.get('potassium')
        heamoglobin = request.POST.get('heamoglobin')
        packed_ceel_volume = request.POST.get('packed_ceel_volume')
        white_blood_cell_volume = request.POST.get('white_blood_cell_volume')
        red_blood_cell_count = request.POST.get('red_blood_cell_count')
        appetite = request.POST.get('appetite')
        anemia = request.POST.get('anemia')

        features = [age, blood_pressure,
                    specific_gravity, albumin, sugar_degree, red_blood_cells, blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium, heamoglobin, packed_ceel_volume, white_blood_cell_volume, red_blood_cell_count, appetite, anemia]

        float_conversion = [float(val) for val in features]

        prediction_features = [numpy.array(float_conversion)]

        prediction = kidney_model.predict(prediction_features)
        predicted_result_for_kidney_disease = prediction[0]
        prediction = KidneyDiseasePrediction.objects.create(
            user=user, age=age, blood_pressure=blood_pressure, specific_gravity=specific_gravity, albumin=albumin, sugar_degree=sugar_degree,
            red_blood_cells=red_blood_cells, blood_glucose_random=blood_glucose_random, blood_urea=blood_urea, serum_creatinine=serum_creatinine, sodium=sodium, potassium=potassium, heamoglobin=heamoglobin, packed_ceel_volume=packed_ceel_volume, white_blood_cell_volume=white_blood_cell_volume, red_blood_cell_count=red_blood_cell_count, appetite=appetite, anemia=anemia, predicted_result_for_kidney_disease=predicted_result_for_kidney_disease)

        # prediction = prediction.save()
        prediction.save()
        print(predicted_result_for_kidney_disease, prediction)
        messages.success(request, "Predicted Successfully!!!")

    context = {
        'result': result,
        'predicted_result': predicted_result_for_kidney_disease
    }
    return HttpResponse("Result")


@login_required(login_url='login')
def Diabetes_Disease_Prediction_View(request):
    diabetes_model = joblib.load('data_science\diabetes\model.pkl')

    result = None
    predicted_result_for_diabetes_disease = None
    if request.method == "POST":
        user = request.user
        Pregnancies = request.POST.get('Pregnancies')
        Glucose = request.POST.get('Glucose')
        BloodPressure = request.POST.get('BloodPressure')
        SkinThickness = request.POST.get('SkinThickness')
        Insulin = request.POST.get('Insulin')
        BMI = request.POST.get('BMI')
        DiabetesPedigreeFunction = request.POST.get('DiabetesPedigreeFunction')
        Age = request.POST.get('Age')

        features = [Pregnancies, Glucose, BloodPressure,
                    SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        float_conversion = [float(val) for val in features]

        prediction_features = [numpy.array(float_conversion)]

        prediction = diabetes_model.predict(prediction_features)
        predicted_result_for_diabetes_disease = prediction[0]
        prediction = DiabetesDiseasePrediction.objects.create(
            user=user, Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure, SkinThickness=SkinThickness, Insulin=Insulin, BMI=BMI, DiabetesPedigreeFunction=DiabetesPedigreeFunction, Age=Age, predicted_result_for_diabetes_disease=predicted_result_for_diabetes_disease
        )

        # prediction = prediction.save()
        prediction.save()
        print(predicted_result_for_diabetes_disease, prediction)
        messages.success(request, "Predicted Successfully!!!")

    context = {
        'result': result,
        'predicted_result': predicted_result_for_diabetes_disease
    }
    return HttpResponse("Result")


@login_required(login_url='login')
def Liver_Disease_Prediction_View(request):
    liver_model = joblib.load('data_science\liver\model.pkl')

    result = None
    predicted_result_for_liver_disease = None
    if request.method == "POST":
        user = request.user
        Age = request.POST.get('Age')
        Gender = request.POST.get('Gender')
        Total_Bilirubin = request.POST.get('Total_Bilirubin')
        Direct_Bilirubin = request.POST.get('Direct_Bilirubin')
        Alkaline_Phosphotase = request.POST.get('Alkaline_Phosphotase')
        Alamine_Aminotransferase = request.POST.get('Alamine_Aminotransferase')
        Aspartate_Aminotransferase = request.POST.get(
            'Aspartate_Aminotransferase')
        Total_Protiens = request.POST.get('Total_Protiens')
        Albumin = request.POST.get('Albumin')
        Albumin_and_Globulin_Ratio = request.POST.get(
            'Albumin_and_Globulin_Ratio')

        features = [Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio
                    ]
        float_conversion = [float(val) for val in features]

        prediction_features = [numpy.array(float_conversion)]

        prediction = liver_model.predict(prediction_features)
        predicted_result_for_liver_disease = prediction[0]
        prediction = DiabetesDiseasePrediction.objects.create(
            user=user, Age=Age, Gender=Gender, Total_Bilirubin=Total_Bilirubin, Direct_Bilirubin=Direct_Bilirubin, Alkaline_Phosphotase=Alkaline_Phosphotase, Alamine_Aminotransferase=Alamine_Aminotransferase, Aspartate_Aminotransferase=Aspartate_Aminotransferase, Total_Protiens=Total_Protiens, Albumin=Albumin, Albumin_and_Globulin_Ratio=Albumin_and_Globulin_Ratio,predicted_result_for_liver_disease=predicted_result_for_liver_disease

        )

        # prediction = prediction.save()
        prediction.save()
        print(predicted_result_for_liver_disease, prediction)
        messages.success(request, "Predicted Successfully!!!")

    context = {
        'result': result,
        'predicted_result': predicted_result_for_liver_disease
    }
    return HttpResponse("Result")
