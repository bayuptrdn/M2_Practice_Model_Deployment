import streamlit as st
import eda, predict

# bikin sidebar menu
with st.sidebar:
    st.title('Page Navigation')
    # input
    page = st.radio('Page', ('EDA', 'Model Demo'))

    st.write('# About')
    st.write('Page ini menampilkan berita heboh') # kalo panjang kesamping pake docstring

if page == "EDA":
    eda.run()               # tarik function eda di page 1 sidebar
else:
    predict.run()           # tarik function predict di page 2 sidebar