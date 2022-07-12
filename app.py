import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

st.title('Laptop Predictor')
company = st.selectbox('Brand',df['Company'].unique())
type = st.selectbox('Type',df['TypeName'].unique())
weight = st.number_input('Weight of the laptop',min_value=1.0,max_value=6.0)
ram = st.selectbox('Ram',[2,4,8,16,32,64])
touchscreen = st.selectbox('Touchscreen',["yes","no"])
ips = st.selectbox('Ips Panel',["yes","no"])
hd = st.selectbox('HD',['yes','no'])
screen_size = st.number_input('Inches',min_value=10.0,max_value=18.0)
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU',df['brand'].unique())
hdd = st.selectbox('HDD(IN GB)',[0,128,256,512,1024,2048])
ssd = st.selectbox('SSD(IN GB)',[0,128,256,512,1024])
gpu = st.selectbox('GPU',df['check'].unique())
os = st.selectbox('OS',df['OpSys'].unique())

if st.button('Predict price'):
    if touchscreen == 'Yes':
        touchscreen = 1
    else :
        touchscreen = 0
    if ips == 'Yes':
        ips = 1
    else :
        ips = 0
    if hd == 'Yes':
        hd = 1
    else:
        hd = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) +(Y_res**2))**0.5/screen_size
    inp = np.array([company,type,ram,os,weight,touchscreen,ips,hd,ppi,cpu,2.5,hdd,ssd,gpu])
    inp = inp.reshape(1,14)
    output = int(np.exp(model.predict(inp))[0])
    st.title('Approx Price in INR is  '+ str(output))