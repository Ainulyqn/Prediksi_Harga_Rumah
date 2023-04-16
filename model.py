#import package
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import time

#import the data
data = pd.read_csv("Data Clean.csv")
image = Image.open("img/rumah.jpg")
st.title("Selamat Datang Di Apliksi Prediksi Harga Rumah")
st.image(image, use_column_width=True)

#mengecek dasta
st.write("Ini adalah aplikasi untuk mengetahui berapa kisaran harga rumah yang Anda pilih menggunakan pembelajaran mesin dengan metode regresi linear. Mari kita coba dan lihat!")
check_data = st.checkbox("Lihat data sederhana")
if check_data:
    st.write(data[1:10])
st.write("Sekarang mari kita cari tahu berapa harganya saat kita memilih beberapa parameter di bawah ini.")

#input parameter
sqft_liv = st.slider("Luas rumah yang di inginkan?(satuan sqft)",int(data.sqft_living.min()),int(data.sqft_living.max()),int(data.sqft_living.mean()) )
sqft_abo = st.slider("Luas bangunan yang ada di atas tanah?(satuan sqft)",int(data.sqft_above.min()),int(data.sqft_above.max()),int(data.sqft_above.mean()) )
bath     = st.slider("Berapa banyak kamar mandi?",int(data.bathrooms.min()),int(data.bathrooms.max()),int(data.bathrooms.mean()) )
view = st.slider("view?",int(data.view.min()),int(data.view.max()),int(data.view.mean()) )
sqft_bas   = st.slider("Luas bangunan yang ada di bawah tanah?(satuan sqft)",int(data.sqft_basement.min()),int(data.sqft_basement.max()),int(data.sqft_basement.mean()) )
condition  = st.slider("kondisi?",int(data.condition.min()),int(data.condition.max()),int(data.condition.mean()) )

#memisahkan data
X = data.drop('price', axis = 1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=.2, random_state=45)

#modelling step
#Linear Regression model
#import your model
model=LinearRegression()
#fitting and predict your model
model.fit(X_train, y_train)
model.predict(X_test)
errors = np.sqrt(mean_squared_error(y_test,model.predict(X_test)))
predictions = model.predict([[sqft_liv,sqft_abo,bath,view,sqft_bas,condition]])[0]
akurasi= np.sqrt(r2_score(y_test,model.predict(X_test)))

# =============================================================================
# #RandomForestModel
#model2 = RandomForestRegressor(random_state=0)
#model2.fit(X_train,y_train)
#model2.predict(X_test)
#errors = np.sqrt(mean_squared_error(y_test,model2.predict(X_test)))
#predictions = model2.predict([[sqft_liv,sqft_abo,bath,view,sqft_bas,condition]])[0]
#akurasi= np.sqrt(r2_score(y_test,model2.predict(X_test)))
# =============================================================================

# =============================================================================
# #DecissionTreeModel
#model3 = DecisionTreeRegressor(random_state= 45)
#model3.fit(X_train,y_train)
#model3.predict(X_test)
#errors = np.sqrt(mean_squared_error(y_test,model3.predict(X_test)))
#predictions = model3.predict([[sqft_liv,sqft_abo,bath,view,sqft_bas,condition]])[0]
#akurasi= np.sqrt(r2_score(y_test,model3.predict(X_test)))
# =============================================================================

#cek prediksi harga rumah
if st.button("Hasil Prediksi"):
    st.header("Prediksi harga rumah Anda adalah USD {}".format(int(predictions)))
    st.subheader("Rentang prediksi Anda adalah USD {} - USD {}".format(int(predictions-errors),int(predictions+errors)))
    st.subheader("Akurasi : {}".format(akurasi))


#simpan model 
import pickle
filename = 'Prediksi-Harga-Rumah.sav'
pickle.dump(model, open(filename,'wb')) 
