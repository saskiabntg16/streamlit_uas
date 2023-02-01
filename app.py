import streamlit as st
import pandas as pd
from PIL import Image
from sklearn import datasets
from sklearn.svm import GaussianNB
import pickle 

st.write("""
# UAS DWDM Deploy Klasifikasi Iris Menggunakan Streamlit
Nama: Saskia Bintang Maharani
NIM : 2019230047
"""
)

img = Image.open ('iris.png')
st.image(img, use_column_width=False)

st.sidebar.header('Parameter Value')

def input_user():
    PanjangSepal = st.slider('PanjangSepal:', 2.0, 6.0)
    LebarSepal= st.slider('LebarSepal:', 0.0, 5.0)
    PanjangPetal = st.slider('PanjangPetal',0.0, 3.0)
    LebarPetal = st.slider('LebarPetal:', 0.0, 2.0)

data = {'PanjangSepal': PanjangsSepal,
            'LebarSepal': LebarSepal,
            'PanjangPetal': PanjangPetal,
            'LebarPetal': LebarPetal}
     
features = pd.DataFrame(data, index=[0]) 

return features

df = input_user()

dt.subheader('Parameter Inputan')
st.write(df)

iris = datasets.load_iris()
X = iris.data
Y = iris.target
model = GaussianNB()
model.fit(X,Y)

model = pickle.load(open('model.pkl', 'rb'))
prediksi = model.predict(df)
prediksi_proba = model.predict.proba(df)

st.subheader('Label Kelas dan Nomor Indeks Sesuai Inputan')
st.write(iris.target_names)

st.subheader('Prediksi (Hasil Klasifikasi)')
st.write(iris.target_names[prediksi])

st.subheader('Probabilitas Hasil Predikasi(klasifikasi)')
st.write(predikasi_proba)

st.subheader('Prediction Percentages:') 
st.write('**Probablity of Iris Class being Iris-setosa is ( in % )**:',pred_proba[0][0]*100)
st.write('**Probablity of Isis Class being Iris-versicolor is ( in % )**:',pred_proba[0][1]*100)
st.write('**Probablity of Isis Class being Iris-virginica ( in % )**:',pred_proba[0][2]*100)
