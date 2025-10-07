import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def run():
    # Elemen Title
    st.title("FIFA Data Exploration")

    # Tampilkan gambar (image) :

    st.image("https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/1506830/capsule_616x353.jpg?t=1712678728", caption= 'source: google image')

    # Header
    st.markdown('## Latar Belakang')

    # Markdown

    st.markdown('''Menurut laporan [FIFA 2022](https://publications.fifa.com/en/annual-report-2021/around-fifa/professional-football-2021/), jumlah pemain sepakbola pada tahun 2021 kurang lebih sebanyak 130.000 pemain. Namun, dalam dataset yang digunakan pada kali ini, hanya mencakup 20.000 pemain saja.
                
                Project kali ini bertujuan untuk memprediksi rating pemain FIFA 2022 sehingga semua pemain sepak bola profesional dapat diketahui ratingnya dan tidak menutup kemungkinan untuk lahirnya talenta/wonderkid baru.
                
                Project ini akan dibuat menggunakan algoritma Linear Regresison dan akan dievaluasi dengan menggunakan metrics **MAE (Mean Absolute Error)**.''')

    # Tampilin Dataset

    st.header('Dataset')

    st.markdown('Rating dan atribut pemain FIFA 2022 yang diambil dari web Sofifa.com')

    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')

    # Rename columns (optional)

    data.rename(columns={'ValueEUR': 'Price', 'Overall': 'Rating'}, inplace=True)

    # Tampilkan dataframe
    st.dataframe(data)

    # EDA
    st.header('Exploratory Data Analysis')

    st.subheader('Player Rating Distribution')
    # Rating Histogram (Visualisasi pertama)
    fig = plt.figure(figsize=(16, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(data['Rating'], kde=True, bins=30)
    plt.title('Histogram of Rating')

    # Menampilkan matplotlib chart
    st.pyplot(fig)

    # Insight Visual
    st.markdown('''Terlihat dari Histogram Plot diatas bahwa `Rating` memiliki distribusi normal dengan mayoritas data berada pada rentang `60` hingga `70`''')

    # Menampilkan visualisasi kedua (weight vs height)
    st.subheader('Weight vs Height Distribution')
    # #Plotly Chart
    fig = px.scatter(data, x='Weight', y='Height', hover_name='Name')
    st.plotly_chart(fig)

    # Visualisasi based on user input
    st.subheader('Player Stat Distribution')

    # nama kolom yg ada Total nya
    nama_kolom = data.columns
    total_cols = [col for col in nama_kolom if 'Total' in col]

    # User input
    option = st.selectbox(
        "Mau pilih visualisasi dari kolom apa?",
        options = total_cols)


    st.write("You selected:", option)

    # Visualisasi :

    fig = plt.figure(figsize=(16, 5))
    plt.subplot(1, 2, 1)
    sns.histplot(data[option], kde=True, bins=30)
    plt.title(f'Histogram of {option}')

    # Menampilkan matplotlib chart
    st.pyplot(fig)

    # Plotly
    fig = px.histogram(data, x=option, hover_name = 'Name')
    st.plotly_chart(fig)

# utk panggil function supaya bisa jalan di streamlit
if __name__ == '__main__':
    run()