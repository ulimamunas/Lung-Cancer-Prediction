import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("#")

st.title("PREDICTION OF LUNG CANCER SEVERITY")

image_path = "pages/foto1.jpg"
st.image(image_path, use_column_width=True, caption='health.wusf.usf.edu')

st.write("""
Lung cancer is a type of cancer that begins in the cells of the lungs. It is one of the most common and deadliest forms of cancer worldwide. There are two main types of lung cancer: non-small cell lung cancer (NSCLC) and small cell lung cancer (SCLC).

NSCLC is the more prevalent form, comprising about 85% of all lung cancer cases. It includes subtypes such as adenocarcinoma, squamous cell carcinoma, and large cell carcinoma. SCLC is a more aggressive type and tends to spread quickly.

The primary cause of lung cd LCcancer is cigarette smoking, with other factors such as exposure to secondhand smoke, environmental pollutants, and genetic predisposition also playing a role. Symptoms may include persistent coughing, chest pain, shortness of breath, and unexplained weight loss.

Early detection is crucial for effective treatment, but lung cancer is often diagnosed at advanced stages when the prognosis is less favorable. Treatment options include surgery, chemotherapy, radiation therapy, targeted therapies, and immunotherapy. Prevention through smoking cessation and minimizing exposure to risk factors remains the most effective way to reduce the incidence of lung cancer.
""")

st.write("## Why do we use this dataset")
st.write("""
1. Current dataset (release in 2023)
2. Relevant to the topic covered
3. Sufficient data required
4. Clear sources
""")

st.write("## Why lung severity needs to be predicted")
st.write("""
1. Care planning
2. Resource management
3. Monitoring patient progress
4. Early warning
5. Clinical decision making
6. Communication with patients and family
7. Research and development
""")

dataset_path = 'cancer patient data sets.csv'
df = pd.read_csv('pages/cancer patient data sets.csv')

st.write("## Dataset Preview")
st.write(df)

st.write("## Data Distribution")
st.write("""
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Severity from Dataset")
    st.write("High: 365")
    st.write("Meidum: 332")
    st.write("Low: 303")

with col2:
    st.write("Training Dataset")
    st.write("High: 250")
    st.write("Medium: 236")
    st.write("Low: 214")

with col3:
    st.write("Testing Dataset")
    st.write("High: 115")
    st.write("Medium: 96")
    st.write("Low: 89")

st.write("## Data Processing")
st.write("""
For dataset processing, using a Logistic Regression Algorithm and get a testing accuracy

Accuracy from this model: 97.33333333333334%
""")
