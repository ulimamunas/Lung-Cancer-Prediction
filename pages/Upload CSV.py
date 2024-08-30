import streamlit as st
import joblib
import pandas as pd

st.markdown("# ")
# st.sidebar.markdown("# Upload CSV")

st.title("LUNG CANCER PREDICTION")

LCD_model = joblib.load('pages/LCD model.joblib')

# Membuat pemetaan (kamus) dari singkatan ke nama yang lebih deskriptif
column_mapping = {
    "GD": "Gender",
    "AP": "Air Pollution",
    "AU": "Alcohol Use",
    "DAL": "Dust Allergy",
    "OPH": "OccuPational Hazards",
    "GR": "Genetic Risk",
    "CLD": "Chronic Lung Disease",
    "BD": "Balanced Diet",
    "OB": "Obesity",
    "SMK": "Smoking",
    "PS": "Passive Smoker",
    "CP": "Chest Pain",
    "COB": "Coughing of Blood",
    "FTG": "Fatigue",
    "WL": "Weight Loss",
    "SOB": "Shortness of Breath",
    "WZG": "Wheezing",
    "SD": "Swallowing Difficulty",
    "CFN": "Clubbing of Finger Nails",
    "FC": "Frequent Cold",
    "DC": "Dry Cough",
    "SNR": "Snoring",
}

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
  # Baca data dari file CSV menggunakan pandas
    data = pd.read_csv(uploaded_file)

    # Tampilkan data yang diupload
    st.write("Uploaded Data:")
    st.write(data)

    # Iterasi melalui setiap baris data dan lakukan prediksi
    for index, row in data.iterrows():
        Age = row["Age"]
        
        # Menggunakan pemetaan untuk mendapatkan nama kolom yang sesuai
        Gender = row[column_mapping["GD"]]
        AirPollution = row[column_mapping["AP"]]
        AlcoholUse = row[column_mapping["AU"]]
        DustAllergy = row[column_mapping["DAL"]]
        OccuPationalHazards = row[column_mapping["OPH"]]
        GeneticRisk = row[column_mapping["GR"]]
        ChronicLungDisease = row[column_mapping["CLD"]]
        BalanceDiet = row[column_mapping["BD"]]
        Obesity = row[column_mapping["OB"]]
        Smoking = row[column_mapping["SMK"]]
        PassiveSmoker = row[column_mapping["PS"]]
        ChestPain = row[column_mapping["CP"]]
        CoughingofBlood = row[column_mapping["COB"]]
        Fatigue = row[column_mapping["FTG"]]
        WeightLoss = row[column_mapping["WL"]]
        ShortnessofBreath = row[column_mapping["SOB"]]
        Wheezing = row[column_mapping["WZG"]]
        SwallowingDifficulty = row[column_mapping["SD"]]
        ClubbingFinger = row[column_mapping["CFN"]]
        FrequentCold = row[column_mapping["FC"]]
        DryCough = row[column_mapping["DC"]]
        Snoring = row[column_mapping["SNR"]]

        LCD_diagnosis = LCD_model.predict([[
            Age, Gender, AirPollution, AlcoholUse,
            DustAllergy, OccuPationalHazards, GeneticRisk,
            ChronicLungDisease, BalanceDiet, Obesity, Smoking, 
            PassiveSmoker, ChestPain, CoughingofBlood, 
            Fatigue, WeightLoss, ShortnessofBreath, Wheezing,
            SwallowingDifficulty, ClubbingFinger, FrequentCold,
            DryCough, Snoring, 
        ]])

        if LCD_diagnosis[0] == 3:
            prediction_category = "High"
        elif LCD_diagnosis[0] == 2:
            prediction_category = "Medium"
        else:
            prediction_category = "Low"

        # Simpan hasil prediksi dan kategori ke dalam DataFrame
        data.at[index, "Prediction Category"] = prediction_category

    # Tampilkan hasil prediksi
    st.write("Predictions:")
    st.write(data)