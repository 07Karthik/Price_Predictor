import streamlit as st
import pickle
import pandas as pd
import numpy as np

# model(extratressregressor) r2_score:-95%, cross_val_score:-74%

def Mobile():
        pipe = pickle.load(open('pipe8.pkl','rb'))

        df = pickle.load(open('X_train.pkl','rb'))

        st.title('Mobile Price Predictor')

        # ['mobile_color', 'disp_size', 'os', 'num_cores', 'mp_speed',
        #        'int_memory', 'ram', 'battery_power', 'mob_width', 'mob_height',
        #        'mob_depth', 'mob_weight', 'res_dim_1', 'res_dim_2', 'p_cam_max',
        #        'p_cam_count', 'f_cam_max', 'f_cam_count', '2G', '3G', '4G', '4GVOLTE',
        #        '5G']
        # mobile color
        color = st.selectbox("Color",df['mobile_color'].unique())

        # dual_sim
        # dual_sim = df['dual_sim'].unique()

        # disp_size
        disp_size = st.number_input('Display Size(in inches)')

        # os
        os = st.selectbox("Operating System",sorted(df['os'].unique()))

        # num_cores
        num_cores = st.selectbox("No.of Cores",sorted(df['num_cores'].unique()))

        # speed of cpu
        mp_speed = disp_size = st.number_input('processor speed',help='2GHz processor')

        # memory
        int_memory = st.selectbox("Internal Memory",sorted(df['int_memory'].unique()))

        # ram
        ram = st.selectbox("RAM",sorted(df['ram'].unique(),reverse=True))

        # battery_power
        battery_power = st.selectbox("Battery",sorted(df['battery_power'].unique(),reverse=True))


        # mob_width
        mob_width = st.number_input('Mobile Width(mm)')

        # mob_height
        mob_height = st.number_input('Mobile Height(mm)')

        # mob_depth
        mob_depth = st.number_input('Mobile Depth(mm)')

        # mob_weight
        mob_weight = st.number_input('Mobile Weight')

        # resolution
        # resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])
        resolution = st.text_input("Enter Resulution")

        # # res_dim_1
        # res_dim_1 = st.number_input('X_resolution')
        # res_dim_1 = int(res_dim_1)  # Cast the input value to an integer

        # # res_dim_2
        # res_dim_2 = st.number_input('Y_resolution')
        # res_dim_2 = int(res_dim_2)

        # p_cam_max
        p_cam_max = st.selectbox("Max rear camera",sorted(df['p_cam_max'].unique(),reverse=True),help='Primay Max camera')

        # p_cam_count
        p_cam_count = st.selectbox("Count of rear cameras",sorted(df['p_cam_count'].unique()))

        # f_cam_max
        f_cam_max = st.selectbox("Max front camera",sorted(df['f_cam_max'].unique()),help='Secondary Max camera')

        # f_cam_count
        f_cam_count = st.selectbox("Toatl no. of front cameras",[1,2],help='total no.of cameras including max camera')

        # '2G', '3G', '4G', '4GVOLTE',
        #        '5G'

        # Network
        network_choices = {
        "2G": df['2G'].unique(),
        "3G": df['3G'].unique(),
        "4G": df['4G'].unique(),
        "4GVOLTE": df['4GVOLTE'].unique(),
        "5G": df['5G'].unique()
        }

        selected_network = st.selectbox("Select Network", network_choices.keys())

        # selected_value = st.selectbox(f"Network_{selected_network}", network_choices[selected_network])
        selected_value = 1
        if selected_network == '2G':
                G2 = 1
                G3 = 0
                G4 = 0
                G4VOLTE = 0
                G5 = 0
        elif selected_network == '3G':
                G2 = 0
                G3 = 1
                G4 = 0
                G4VOLTE = 0
                G5 = 0
        elif selected_network == '4G':
                G2 = 0
                G3 = 0
                G4 = 1
                G4VOLTE = 0
                G5 = 0
        elif selected_network == '4GVOLTE':
                G2 = 0
                G3 = 0
                G4 = 0
                G4VOLTE = 1
                G5 = 0
        else:
                G2 = 0
                G3 = 0
                G4 = 0
                G4VOLTE = 0
                G5 = 1
                

        # 'mobile_color', 'dual_sim', 'disp_size', 'os', 'num_cores', 'mp_speed',
        #        'int_memory', 'ram', 'battery_power', 'mob_width', 'mob_height',
        #        'mob_depth', 'mob_weight', 'res_dim_1', 'res_dim_2', 'p_cam_max',
        #        'p_cam_count', 'f_cam_max', 'f_cam_count', '2G', '3G', '4G', '4GVOLTE',
        #        '5G'
        if st.button('Predict Price'):
                res_dim_1 = int(resolution.split('x')[0])
                res_dim_2 = int(resolution.split('x')[1])


                query = np.array([color,disp_size,os,num_cores,mp_speed,int_memory,ram,battery_power,mob_width,mob_height,mob_depth,mob_weight,res_dim_1,res_dim_2,p_cam_max,p_cam_count,f_cam_max,f_cam_count,G2,G3,G4,G4VOLTE,G5])

                query = query.reshape(1,23)
                
                st.title("The predicted price of this configuration is " + str(int(pipe.predict(query)[0])))

# pip install pandas==1.5.3

button_clicked = st.button("Click me!")

# Use a session state to track whether the button has been clicked
if 'button_click_state' not in st.session_state:
    st.session_state.button_click_state = False

# Check if the button was clicked
if button_clicked:
    st.session_state.button_click_state = True

if st.session_state.button_click_state:
    # after you click the button and the Mobile() function is executed, the app would "forget" that the button was clicked, and the button would reappear.so,you sessions in streamlit
    Mobile()





