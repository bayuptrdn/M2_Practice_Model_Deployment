import streamlit as st
import pandas as pd
import pickle
import json
import numpy as np

# Load all files

with open('model_lin_reg.pkl', 'rb') as file_1:
  model_lin_reg = pickle.load(file_1)

with open('model_scaler.pkl', 'rb') as file_2:
  model_scaler = pickle.load(file_2)

with open('model_encoder.pkl','rb') as file_3:
  model_encoder = pickle.load(file_3)

with open('list_num_cols.txt', 'r') as file_4:
  list_num_cols = json.load(file_4)

with open('list_cat_cols.txt', 'r') as file_5:
  list_cat_cols = json.load(file_5)

def run():
    # Judul
    st.title('Predict Player Rating')
    # User inputs

    with st.form(key = 'player'):
        # input
        st.header('Masukan Data Pemain')
    
        # input name
        name = st.text_input('Masukan nama pemain',
                            placeholder= 'ex: Xabi Alonso')
        age = st.number_input('Masukan usia pemain', min_value= 0, max_value= 100,
                            value = 20)
        height = st.number_input('Masukan tinggi badan pemain', min_value= 0, max_value= 300,
                                value = 170)
        weight = st.number_input('Masukan berat badan pemain', min_value= 0, max_value= 300,
                                value = 70, help='Berat badan dalam kg')
        price = st.number_input('Masukan harga pemain', min_value= 0,
                                value = 500000, help = 'Harga dalam Euro')               
        st.write('___')
    # workrate
        attacking_wr = st.selectbox('Attacking work rate', 
                                ['Low', 'Medium', 'High'])
        defensive_wr = st.selectbox('Defensive work rate', 
                                ['Low', 'Medium', 'High'])
        st.write('___')  
    # total columns
        pace = st.slider('Pace total', min_value= 0, max_value= 100,
                    value = 50)
        shooting = st.slider('Shooting total', min_value= 0, max_value= 100,
                    value = 50)
        passing = st.slider('Passing total', min_value= 0, max_value= 100,
                    value = 50)
        dribbling = st.slider('Dribbling total', min_value= 0, max_value= 100,
                    value = 50)
        defending = st.slider('Defending total', min_value= 0, max_value= 100,
                    value = 50)
        physicality = st.slider('Physicality total', min_value= 0, max_value= 100,
                    value = 50)
        # Submit button
        submit = st.form_submit_button('Predict')

    if submit:
    
        data_inf = {
            'Name': name,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Price': price,
            'AttackingWorkRate': attacking_wr,
            'DefensiveWorkRate': defensive_wr,
            'PaceTotal': pace,
            'ShootingTotal': shooting,
            'PassingTotal': passing,
            'DribblingTotal': dribbling,
            'DefendingTotal': defending,
            'PhysicalityTotal':physicality
        }

        data_inf = pd.DataFrame([data_inf])
        st.dataframe(data_inf)

        # Split between numerical columns and categorical columns

        data_inf_num = data_inf[list_num_cols]
        data_inf_cat = data_inf[list_cat_cols]

        # Feature Scaling and Feature Encoding

        ## Feature Scaling
        data_inf_num_scaled = model_scaler.transform(data_inf_num)

        ## Feature Encoding
        data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

        ## Concate
        data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

        # Predict using Linear Regression

        y_pred_inf = model_lin_reg.predict(data_inf_final)

        st.write('# Prediction: ', round(y_pred_inf[0], 1))

if __name__ == '__main__':
    run()