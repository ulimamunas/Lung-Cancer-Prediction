import streamlit as st
import joblib
import numpy as np

st.markdown("# ")

st.title("PREDICTION OF LUNG CANCER SEVERITY")

LCD_model = joblib.load('pages/LCD model.joblib')

COB, DAL, PS, OPH, AP, CLD, SOB, DC, SD, SNR =  "COB", "DAL", "PS", "OPH", "AP", "CLD", "SOB", "DC", "SD", "SNR"

GD, AU, GR, BD, OB, SMK, CP, FTG, WL, WZG, CFN, FC = "GD", "AU", "GR", "BD", "OB", "SMK", "CP", "FTG", "WL", "WZG", "CFN", "FC"

name = st.text_input("Name:", )

Age = st.number_input("Age:", value=0, step=1)

# validasi input umur
if Age < 0:
    st.warning("Please enter a non-negative age!")
    st.stop()

gender = ["Male", "Female"]
selected_gender = st.selectbox("Gender:", gender)

if gender == "Male":
    gender = 1
else: 
    gender = 2


AirPollution = st.radio(
    "Air Pollution",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=AP,
    horizontal=True)
AlcoholUse = st.radio(
    "Alcohol Use",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=AU,
    horizontal=True)
DustAllergy = st.radio(
    "Dust Allergy",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=DAL,
    horizontal=True)
OccuPationalHazards = st.radio(
    "OccuPational Hazards",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=OPH,
    horizontal=True)
GeneticRisk = st.radio(
    "Genetic Risk",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=GR,
    horizontal=True)
ChronicLungDisease = st.radio(
    "Chronic Lung Disease",
    ("1", "2", "3", "4", "5", "6", "7"), key=CLD,
    horizontal=True)
BalanceDiet = st.radio(
    "Balance Diet",
    ("1", "2", "3", "4", "5", "6", "7"), key=BD,
    horizontal=True)
Obesity = st.radio(
    "Obesity",
    ("1", "2", "3", "4", "5", "6", "7"), key=OB,
    horizontal=True)
Smoking = st.radio(
    "Smoking",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=SMK,
    horizontal=True)
PassiveSmoker = st.radio(
    "Passive Smoker",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=PS,
    horizontal=True)
ChestPain = st.radio(
    "Chest Pain",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9"), key=CP,
    horizontal=True)
CoughingofBlood = st.radio(
    "Coughing of Blood",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9"), key=COB,
    horizontal=True)
Fatigue = st.radio(
    "Fatigue",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9"), key=FTG,
    horizontal=True)
WeightLoss = st.radio(
    "Wight Loss",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=WL,
    horizontal=True)
ShortnessofBreath = st.radio(
    "Shortness of Breath",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9"), key=SOB,
    horizontal=True)
Wheezing = st.radio(
    "Wheezing",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=WZG,
    horizontal=True)
SwallowingDifficulty = st.radio(
    "Swallowing Difficulty",
    ("1", "2", "3", "4", "5", "6", "7", "8"), key=SD,
    horizontal=True)
ClubbingFinger = st.radio(
    "Clubbing Finger",
    ("1", "2", "3", "4", "5", "6", "7", "8", "9"), key=CFN,
    horizontal=True)
FrequentCold = st.radio(
    "Frequent Cold",
    ("1", "2", "3", "4", "5", "6", "7"), key=FC,
    horizontal=True)
DryCough = st.radio(
    "Dry Cough",
    ("1", "2", "3", "4", "5", "6", "7"), key=DC,
    horizontal=True)
Snoring = st.radio(
    "Snoring",
    ("1", "2", "3", "4", "5", "6", "7"), key=SNR,
    horizontal=True)

Age, AirPollution, DustAllergy = int(Age), int(AirPollution), int(DustAllergy)
OccuPationalHazards, ChronicLungDisease = int(OccuPationalHazards), int(ChronicLungDisease)
PassiveSmoker, CoughingofBlood, ShortnessofBreath = int(PassiveSmoker), int(CoughingofBlood), int(ShortnessofBreath)
SwallowingDifficulty, DryCough, Snoring = int(SwallowingDifficulty), int(DryCough), int(Snoring)

Gender = int(gender)
AlcoholUse = int(AlcoholUse)
GeneticRisk = int(GeneticRisk)
BalanceDiet = int(BalanceDiet)
Obesity = int(BalanceDiet)
Smoking = int(Smoking)
ChestPain = int(ChestPain)
Fatigue = int(Fatigue)
WeightLoss = int(WeightLoss)
Wheezing = int(Wheezing)
ClubbingFinger = int(ClubbingFinger)
FrequentCold = int(FrequentCold)


if st.button('See prediction'):
    LCD_diagnosis = LCD_model.predict([[
        Age, Gender, AirPollution, AlcoholUse,
        DustAllergy, OccuPationalHazards, GeneticRisk,
        ChronicLungDisease, BalanceDiet, Obesity, Smoking, 
        PassiveSmoker, ChestPain, CoughingofBlood, 
        Fatigue, WeightLoss, ShortnessofBreath, Wheezing,
        SwallowingDifficulty, ClubbingFinger, FrequentCold,
        DryCough, Snoring, 
    ]])

    if LCD_diagnosis == [3]:
        LCD_diagnosis_category = "High"
        st.success(LCD_diagnosis_category)
        st.write(f"{name}, the severity of your lung cancer is {LCD_diagnosis_category}, please contact doctor")
    elif LCD_diagnosis == [2]:
        LCD_diagnosis_category = "Medium"
        st.success(LCD_diagnosis_category)
        st.write(f"{name}, the severity of your lung cancer is {LCD_diagnosis_category}, please contact doctor")
    else: # should be [1], which indicates low
        LCD_diagnosis_category = "Low"
        st.success(LCD_diagnosis_category)
        st.write(f"{name}, the severity of your lung cancer is {LCD_diagnosis_category}, please be careful")

    