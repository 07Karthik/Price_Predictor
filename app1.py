import streamlit as st
import pickle
import pandas as pd
import numpy as np

# for laptop we use the model is randomforest r2_score:-89%
def Laptop():
    pipe = pickle.load(open('pipe.pkl','rb'))

    df = pickle.load(open('df.pkl','rb'))

    st.title('Laptop Price Predictor')

    # brand
    company = st.selectbox("Brand",df['Company'].unique())

    # type of laptop
    type = st.selectbox("Type",df['TypeName'].unique())

    # ram
    ram = st.selectbox("RAM(in GB)",[2,4,6,8,12,16,24,32,64])

    # weight
    weight = st.number_input('Weight of the Laptop')

    # touchscreen
    touchscreen = st.selectbox("TouchScreen",['No','Yes'])

    # IPS
    ips = st.selectbox('IPS',['No','Yes'])

    # screen size
    screen_size = st.number_input("Screen Size")

    # resolution
    resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

    #cpu
    cpu = st.selectbox('CPU',df['Cpu brand'].unique())

    hdd = st.selectbox('HDD(in GB)',[0,128,256,512,1024,2048])

    ssd = st.selectbox('SSD(in GB)',[0,8,128,256,512,1024])

    gpu = st.selectbox('GPU',df['Gpu brand'].unique())

    os = st.selectbox('OS',df['os'].unique())

    if st.button('Predict Price'):
        # query
        ppi = None
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])
        ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size
        query = np.array([company,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

        query = query.reshape(1,12)
        st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))

        # st.markdown('<b><font color="orange" size="30">The predicted price of this configuration is: </font></b>', unsafe_allow_html=True)

        # st.title(str(int(np.exp(pipe.predict(query)[0]))))


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
        resolution = st.text_input("Enter Resulution")

        # p_cam_max
        p_cam_max = st.selectbox("Max rear camera",sorted(df['p_cam_max'].unique(),reverse=True),help='Primay Max camera')

        # p_cam_count
        p_cam_count = st.selectbox("Count of rear cameras",sorted(df['p_cam_count'].unique()))

        # f_cam_max
        f_cam_max = st.selectbox("Max front camera",sorted(df['f_cam_max'].unique()),help='Secondary Max camera')

        # f_cam_count
        f_cam_count = st.selectbox("Toatl no. of front cameras",[1,2],help='total no.of cameras including max camera')

        # Network
        network_choices = {
        "2G": df['2G'].unique(),
        "3G": df['3G'].unique(),
        "4G": df['4G'].unique(),
        "4GVOLTE": df['4GVOLTE'].unique(),
        "5G": df['5G'].unique()
        }

        selected_network = st.selectbox("Select Network", network_choices.keys())
        # selected_value = 1
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
        if st.button('Predict Mobile Price'):
                res_dim_1 = int(resolution.split('x')[0])
                res_dim_2 = int(resolution.split('x')[1])


                query = np.array([color,disp_size,os,num_cores,mp_speed,int_memory,ram,battery_power,mob_width,mob_height,mob_depth,mob_weight,res_dim_1,res_dim_2,p_cam_max,p_cam_count,f_cam_max,f_cam_count,G2,G3,G4,G4VOLTE,G5])

                query = query.reshape(1,23)
                
                st.title("The predicted price of this configuration is " + str(int(pipe.predict(query)[0])))

# pip install pandas==1.5.3



# Define two buttons with unique keys
button_clicked1 = st.button("Click For Mobile Price Predictor!", key="button1")
button_clicked2 = st.button("Click For Laptop Price Predictor!", key="button2")

# Use a session state to track whether each button has been clicked
if 'button1_click_state' not in st.session_state:
    st.session_state.button1_click_state = False

if 'button2_click_state' not in st.session_state:
    st.session_state.button2_click_state = False

# Check if each button was clicked
if button_clicked1:
    st.session_state.button1_click_state = True
    st.session_state.button2_click_state = False

if button_clicked2:
    st.session_state.button2_click_state = True
    st.session_state.button1_click_state = False

# Display content based on button clicks
if st.session_state.button1_click_state:
    # Clear previous content
    st.empty()
    # Display content for the first button
    Mobile()

if st.session_state.button2_click_state:
    # Clear previous content
    st.empty()
    # Display content for the second button
    Laptop()



