import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading saved models
heart = pickle.load(open('heart_disease.pkl','rb'))

diabetes = pickle.load(open('diabetes.pkl','rb'))

breastcancer = pickle.load(open('breast_cancer.pkl','rb'))

liver = pickle.load(open('liver_disease.pkl','rb'))

parkinsons = pickle.load(open('parkinsons_disease.pkl','rb'))


# sidebar for navigation

with st.sidebar:
    
    selected = option_menu('Multi-Disease Prediction System',
                           # title of the page
                           ['Heart Disease Prediction',
                            'Diabetes Prediction',
                            'Breast Cancer Prediction',
                            'Liver Disease Prediction',
                           'Parkinsons Prediction'],
                           # titles in sidebar
                           icons=['heart','activity','person','file-person-fill','people-fill'],
                           # icns for the titles in sidebar
                           default_index=0)
    
# Heart Prediction Page
if(selected == "Heart Disease Prediction"):
    
    # page title
    st.title("Heart Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('1) Age')
        
    with col2:
        sex = st.text_input('2) Sex')
        
    with col3:
        cp = st.text_input('3) Chest pain types')
        
    with col1:
        trestbps = st.text_input('4) Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('5) Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('6) Fasting Blood Sugar')
        
    with col1:
        restecg = st.text_input('7) Resting ECG results')
        
    with col2:
        thalach = st.text_input('8) Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('9) Excersice Induced Angina')
        
    with col1:
        oldpeak = st.text_input('10) ST depression induced by excersice')
        
    with col2:
        slope = st.text_input('11) Slope of peak excersice ST segment')
        
    with col3:
        ca = st.text_input('12) Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('13) thal: 0-normal; 1-fixed defect; 2-reversable defect')
        
     # code for prediction
    heart_diagnosis = ''
     
     # creating  a button for prediction
    if st.button("Heart Disease Test Result"):
        heart_prediction = heart.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, 
                                           slope, ca, thal]])
         
        if(heart_prediction[0] == 1):
            heart_diagnosis = "The person is suffering from Heart disease"
        else:
            heart_diagnosis = "The person is Healthy"
    
    st.success(heart_diagnosis)
    
    
# Diabetes Prediction Page
if(selected == "Diabetes Prediction"):
    
    # page title
    st.title("Diabetes Prediction using ML")
    col1, col2 = st.columns(2)
    
    with col1:
        Pregnancies = st.text_input('1) Number of pregnancies')
        
    with col2:
        Glucose = st.text_input('2) Glucose level')
        
    with col1:
        BloodPressure = st.text_input('3) Blood Pressure value')
        
    with col2:
        SkinThickness = st.text_input('4) Skin Thickness value')
        
    with col1:
        Insulin = st.text_input('5) Insulin level')
        
    with col2:
        BMI = st.text_input('6) BMI level')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('7) Diabetes Pedigree Function')
        
    with col2:
        Age = st.text_input('8) Age of a person')
        
        
     # code for prediction
    diabetes_diagnosis = ''
     
     # creating  a button for prediction
    if st.button("Diabetes Test Result"):
        diabetes_prediction = diabetes.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, 
                                                 BMI, DiabetesPedigreeFunction, Age]])
         
        if(diabetes_prediction[0] == 1):
            diabetes_diagnosis = "The person is Dabetic"
        else:
            diabetes_diagnosis = "The person is Healthy"
    
    st.success(diabetes_diagnosis)
    

# Breast Cancer Prediction Page
if(selected == "Breast Cancer Prediction"):
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        meanradius = st.text_input('1) Mean radius')
        
    with col2:
        meantexture = st.text_input('2) Mean texture')
        
    with col3:
        meanperimeter = st.text_input('3) Mean perimeter')
        
    with col4:
        meanarea = st.text_input('4) Mean area')
        
    with col1:
        meansmoothness = st.text_input('5) Mean smoothness')
        
    with col2:
        meancompactness = st.text_input('6) Mean compactness')
        
    with col3:
        meancavity = st.text_input('7) Mean cavity')
        
    with col4:
        meanconcavepoints = st.text_input('8) mean concave points')
        
    with col1:
        meansymmetry = st.text_input('9) mean symmetry')
        
    with col2:
        meanfractaldimension = st.text_input('10) mean fractal dimension')
    
    with col3:
        radiuserror = st.text_input('11) radius error')
        
    with col4:
        textureerror = st.text_input('12) texture error')
        
    with col1:
        perimetererror = st.text_input('13) perimeter error')
        
    with col2:
        areaerror = st.text_input('14) area error')
        
    with col3:
        smoothnesserror = st.text_input('15) smoothness error')
        
    with col4:
        compactnesserror = st.text_input('16) compactness error')
        
    with col1:
        concavityerror = st.text_input('17) concavity error')
        
    with col2:
        concavepointserror = st.text_input('18) concave points error')
        
    with col3:
        symmetryerror = st.text_input('19) symmetry error')
        
    with col4:
        fractaldimensionerror = st.text_input('20) fractal dimension error')
        
    with col1:
        worstradius = st.text_input('21) worst radius')
        
    with col2:
        worsttexture = st.text_input('22) worst texture')
        
    with col3:
        worstperimeter = st.text_input('23) worst perimeter')
        
    with col4:
        worstarea = st.text_input('24) worst area')
        
    with col1:
        worstsmoothness = st.text_input('25) worst smoothness')
        
    with col2:
        worstcompactness = st.text_input('26) worst compactness')
        
    with col3:
        worstconcavity = st.text_input('27) worst concavity')
        
    with col4:
        worstconcavepoints = st.text_input('28) worst concave points')
        
    with col1:
        worstsymmetry = st.text_input('29) worst symmetry')
        
    with col2:
        worstfractaldimension = st.text_input('30) worst fractal dimension')
    
        
        
     # code for prediction
    breastcancer_diagnosis = ''
     
     # creating  a button for prediction
    if st.button("Breast Cancer Test Result"):
        breastcancer_prediction = breastcancer.predict([[meanradius, meantexture, meanperimeter, meanarea, meansmoothness,
                                                         meancompactness, meancavity, meanconcavepoints, meansymmetry, meanfractaldimension,
                                                         radiuserror, textureerror, perimetererror,areaerror, smoothnesserror,
                                                         compactnesserror, concavityerror, concavepointserror, symmetryerror, fractaldimensionerror,
                                                         worstradius, worsttexture, worstperimeter, worstarea, worstsmoothness,
                                                         worstcompactness, worstconcavity, worstconcavepoints, worstsymmetry, worstfractaldimension]])
         
        if(breastcancer_prediction[0] == 1):
            breastcancer_diagnosis = "The Breast Cancer is Begnin"
        else:
            breastcancer_diagnosis = "The Breast Cancer is Malignant"
    
    st.success(breastcancer_diagnosis)
    
    
# Liver Disease Prediction Page
if(selected == "Liver Disease Prediction"):
    
    # page title
    st.title("Liver Disease Prediction using ML")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('1) Age')
        
    with col2:
        Gender = st.text_input('2) Gender')
        
    with col3:
        Total_Bilirubin = st.text_input('3) Total_Bilirubin')
        
    with col1:
        Direct_Bilirubin = st.text_input('4) Direct_Bilirubin')
        
    with col2:
        Alkaline_Phosphotase = st.text_input('5) Alkaline_Phosphotase')
        
    with col3:
        Alamine_Aminotransferase = st.text_input('6) Alamine_Aminotransferase')
        
    with col1:
        Aspartate_Aminotransferase = st.text_input('7) Aspartate_Aminotransferase')
        
    with col2:
        Total_Protiens = st.text_input('8) Total_Protiens')
        
    with col3:
        Albumin = st.text_input('9) Albumin')
        
    with col1:
        Albumin_and_Globulin_Ratio = st.text_input('10) Albumin_and_Globulin_Ratio')
        
        
     # code for prediction
    liver_disease_diagnosis = ''
     
     # creating  a button for prediction
    if st.button("Liver Disease Test Result"):
        liver_disease_prediction = liver.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, 
                                                   Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
         
        if(liver_disease_prediction[0] == 1):
            liver_disease_diagnosis = "The person is suffering from Liver disease"
        else:
            liver_disease_diagnosis = "The person is Healthy"
    
    st.success(liver_disease_diagnosis)
    
    
# Parkinsons Disease Prediction Page
if(selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinsons Disease Prediction using ML")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        Fo = st.text_input('1) MDVP:Fo(Hz)')
        
    with col2:
        Fhi = st.text_input('2) MDVP:Fhi(Hz)')
        
    with col3:
        Flo = st.text_input('3) MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('4) MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('5) MDVP:Jitter(Abs)')
        
    with col1:
        RAP = st.text_input('6) MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('7) MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('8) Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('9) MDVP:Shimmer')
        
    with col5:
        MDVP_Shimmer = st.text_input('10) Shimmer(dB)')
    
    with col1:
        APQ3 = st.text_input('11) Shimmer:APQ3')
        
    with col2:
        APQ5 = st.text_input('12) Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('13) MDVP:APQ')
        
    with col4:
        DDA = st.text_input('14) Shimmer:DDA')
        
    with col5:
        NHR = st.text_input('15) NHR')
        
    with col1:
        HNR = st.text_input('16) HNR')
        
    with col2:
        RPDE = st.text_input('17) RPDE')
        
    with col3:
        DFA = st.text_input('18) DFA')
        
    with col4:
        spread1 = st.text_input('19) spread1')
        
    with col5:
        spread2 = st.text_input('20) spread2')
        
    with col1:
        D2 = st.text_input('21) D2')
        
    with col2:
        PPE = st.text_input('22) PPE')
        
        
     # code for prediction
    parkinsons_diagnosis = ''
     
     # creating  a button for prediction
    if st.button("Parkinsons Test Result"):
        parkinsons_prediction = parkinsons.predict([[Fo, Fhi, Flo, Jitter_percent, Jitter_Abs,
                                                     RAP, PPQ, DDP, Shimmer, MDVP_Shimmer,
                                                     APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                     DFA, spread1, spread2, D2, PPE]])
         
        if(parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person is suffering from Parkinsons disease"
        else:
            parkinsons_diagnosis = "The person is Healthy"
    
    st.success(parkinsons_diagnosis)
 

    
        
     
        
    
    
    