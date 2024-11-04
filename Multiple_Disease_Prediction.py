import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models

diabetes_model=pickle.load(open("C:/Users/jjaya/OneDrive/Desktop/Disease Prediction App/ML models/Diabetes Prediction", "rb"))
heart_disease_model=pickle.load(open("C:/Users/jjaya/OneDrive/Desktop/Disease Prediction App/ML models/Heart Disease Prediction", "rb"))
parkinsons_disease_model=pickle.load(open("C:/Users/jjaya/OneDrive/Desktop/Disease Prediction App/ML models/Parkinson's Disease Prediction", "rb"))
breast_cancer_model=pickle.load(open("C:/Users/jjaya/OneDrive/Desktop/Disease Prediction App/ML models/Breast Cancer Prediction", "rb"))

# Sidebar for navigation

with st.sidebar:
    select = option_menu('Multiple Disease Prediction',
                         ["Diabetes Prediction",
                          "Heart Disease Prediction",
                          "Parkinson's Disease Prediction",
                          "Breast Cancer Prediction"],
                         default_index=0,
                         icons=["droplet-fill","heart-pulse-fill","person-fill","thermometer-half"],
                         styles={
                             "container":{"padding":"10px"}
                         }
                         )

# Diabetes prediction page

if select=="Diabetes Prediction":

    # Page title
    st.title("Diabetes Prediction")

    # Getting the input from the user
    # Columns for input fields
    col1,col2,col3=st.columns(3)

    with col1:
        Pregnancies=st.text_input("Number of Pregnancies")
    with col2:
        Glucose=st.text_input("Glucose Level")
    with col3:
        BloodPressure=st.text_input("Blood Pressure Value")
    with col1:
        SkinThickness=st.text_input("Skin Thickness Value")
    with col2:
        Insulin=st.text_input("Insulin Level")
    with col3:
        BMI=st.text_input("BMI Value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value")
    with col2:
        Age=st.text_input("Age of Person")

    # Code for prediction
    diab_diagnosis=""

    if st.button("Diabetes Test Result"):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_predict = diabetes_model.predict([user_input])

        if diab_predict[0]==1:
            diab_diagnosis="Person is Diabetic"
        else:
            diab_diagnosis="Person is Not Diabetic"

    st.success(diab_diagnosis)


# Heart disease prediction page

if select=="Heart Disease Prediction":

    # Page title
    st.title("Heart Disease Prediction")

    # Getting the input from the user
    # Columns for input fields
    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input("Age Of Person")
    with col2:
        gender=st.selectbox("Select Gender",("Male","Female"))
        sex=0
        if gender=="Male":
            sex=1
        elif gender=="Female":
            sex=0
    with col3:
        chest_pain=st.selectbox("Chest Pain Type",("STEMI","NSTE-ACS","Stable Angina","Noncardiac"))
        cp=0
        if chest_pain=="STEMI":
            cp=0
        elif chest_pain=="NSTE-ACS":
            cp=1
        elif chest_pain=="Stable Angina":
            cp=2
        else:
            cp=3
    with col1:
        trestbps=st.text_input("Resting Blood Pressure Value")
    with col2:
        chol=st.text_input("Serum Cholestoral in mg/dl")
    with col3:
        fbs=st.text_input("Fasting Blood Sugar > 120 mg/dl")
    with col1:
        restecg=st.text_input("Resting Electrocardiographic Value")
    with col2:
        thalach=st.text_input("Maximum Heart Rate achieved")
    with col3:
        exang=st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak=st.text_input("ST depression induced by exercise")
    with col2:
        slope=st.text_input("Slope of the peak exercise ST segment")
    with col3:
        ca=st.text_input("Major vessels colored by flourosopy")
    with col1:
        thalassemia=st.selectbox("Thalassemia Type",("Normal","Fixed Defect","Reversable Defect"))
        thal=0
        if thalassemia=="Normal":
            thal=0
        elif thalassemia=="Fixed Defect":
            thal=1
        elif thalassemia=="Reversable Defect":
            thal=2

    # Code for prediction
    heart_diagnosis=""

    if st.button("Heart Disease Test Result"):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_predict = heart_disease_model.predict([user_input])

        if heart_predict[0]==1:
            heart_diagnosis="Person have Heart Disease"
        else:
            heart_diagnosis="Person dont have Heart Disease"

    st.success(heart_diagnosis)


# Parkinson's Disease Prediction

if select == "Parkinson's Disease Prediction":

    # page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        parkinsons_prediction = parkinsons_disease_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)


# Breast Cancer Prediction

if select == "Breast Cancer Prediction":

    # page title
    st.title("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        diagnosis = st.selectbox("Diagnosis", ("Male", "Female"))
        sex = 0
        if diagnosis == "Male":
            sex = 1
        elif diagnosis == "Female":
            sex = 0

    with col2:
        radius_mean = st.text_input('Radius Mean')

    with col3:
        texture_mean = st.text_input('Texture Mean')

    with col4:
        perimeter_mean = st.text_input('Perimeter Mean')

    with col5:
        area_mean = st.text_input('Area Mean')

    with col1:
        smoothness_mean = st.text_input('Smoothness Mean')

    with col2:
        compactness_mean = st.text_input('Compactness Mean')

    with col3:
        concavity_mean = st.text_input('Concavity Mean')

    with col4:
        concave_points_mean = st.text_input('Concave Points Mean')

    with col5:
        fractal_dimension_mean = st.text_input('Fractal Dimension Mean')

    with col1:
        radius_se = st.text_input('Radius Se')

    with col2:
        texture_se = st.text_input('Texture Se')

    with col3:
        perimeter_se = st.text_input('Perimeter Se')

    with col4:
        area_se = st.text_input('Area Se')

    with col5:
        smoothness_se = st.text_input('Smoothness Se')

    with col1:
        compactness_se = st.text_input('Compactness Se')

    with col2:
        concavity_se = st.text_input('Concavity Se')

    with col3:
        concave_points_se = st.text_input('Concave Points Se')

    with col4:
        symmetry_se = st.text_input('Symmetry Se')

    with col5:
        fractal_dimension_se = st.text_input('Fractal Dimension Se')

    with col1:
        radius_worst = st.text_input('Radius Worst')

    with col2:
        texture_worst = st.text_input('Texture Worst')

    with col3:
        perimeter_worst = st.text_input('Perimeter Worst')

    with col4:
        area_worst = st.text_input('Area Worst')

    with col5:
        smoothness_worst = st.text_input('Smoothness Worst')

    with col1:
        compactness_worst = st.text_input('Compactness Worst')

    with col2:
        concavity_worst = st.text_input('Concavity Worst')

    with col3:
        concave_points_worst = st.text_input('Concave Points Worst')

    with col4:
        symmetry_worst = st.text_input('Symmetry Worst')

    with col5:
        fractal_dimension_worst = st.text_input('Fractal Dimension Worst')

    # code for Prediction
    breast_cancer_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        user_input = [diagnosis,radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,
                      fractal_dimension_mean,radius_se,texture_se,perimeter_se,area_se,smoothness_se,compactness_se,concavity_se,
                      concave_points_se,symmetry_se,fractal_dimension_se,radius_worst,texture_worst,perimeter_worst,area_worst,
                      smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst,fractal_dimension_worst]

        breast_cancer_prediction = breast_cancer_model.predict([user_input])

        if breast_cancer_prediction[0] == 1:
            breast_cancer_diagnosis = "The person has Parkinson's disease"
        else:
            breast_cancer_diagnosis = "The person does not have Parkinson's disease"

    st.success(breast_cancer_diagnosis)








