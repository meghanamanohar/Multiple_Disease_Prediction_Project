
import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

#loading the diabetes model
# we gotta change the backslashes to forward slashes as spyder can then only understand that it is a path


heartdisease_model=pickle.load(open('C:/Users/User/OneDrive/Documents/Multiple_disease_prediction_project/HeartDisease_model.sav','rb'))     #loading the heart disease model


parkinsons_model=pickle.load(open('C:/Users/User/OneDrive/Documents/Multiple_disease_prediction_project/parkinsons_model.sav','rb'))



# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',

                           ['Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['heart', 'person'],
                           default_index=0)
    
    
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    import streamlit as st
    page_bg_img="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1530026186672-2cd00ffc50fe?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: 100% ;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # page title
    st.title('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('**AGE**')

    with col2:
        sex = st.text_input('**GENDER**')

    with col3:
        cp = st.text_input('**CHEST PAIN TYPES**')

    with col1:
        trestbps = st.text_input('**RESTING BLOOD PRESSURE**')

    with col2:
        chol = st.text_input('**SERUM CHOLESTORAL**')

    with col3:
        fbs = st.text_input('**FASTING BLOOD SUGAR**')

    with col1:
        restecg = st.text_input('**RESTING ECG**')

    with col2:
        thalach = st.text_input('**MAXIMUM HEART RATE**')

    with col3:
        exang = st.text_input('**EXERCISE INDUCED ANGINA**')

    with col1:
        oldpeak = st.text_input('**ST DEPRESSION**')

    with col2:
        slope = st.text_input('**SLOPE OF THE PEAK**')

    with col3:
        ca = st.text_input('**VESSELS (FLOUROSCOPY)**')

    with col1:
        thal = st.text_input('**THAL**')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heartdisease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person IS HAVING heart disease'
            bg_color = 'red'
        else:
            heart_diagnosis = 'The person DOES NOT HAVE any heart disease'
            bg_color = 'green'
        st.markdown(f'<div style="background-color:{bg_color};padding:10px;border-radius:5px;">{heart_diagnosis}</div>', unsafe_allow_html=True)

    



# Parkinsons Disease Prediction Page
if selected == 'Parkinsons Prediction':
    
    import streamlit as st
    page_bg_img="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1559757148-5c350d0d3c56?q=80&w=1931&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: 100% ;
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.title('Parkinsons Disease Prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input('**MDVP (Fo)**')
        
    with col2:
        fhi = st.text_input('**MDVP (Fhi)**')
        
    with col3:
        flo=st.text_input('**MDVP (Flo)**')
        
    with col1:
        jitter_per = st.text_input('**JITTER(%)**')
        
    with col2:
        jitter_abs = st.text_input('**JITTER(Abs)**')
        
    with col3:
        rap = st.text_input('**MDVP:RAP**')
        
    with col1:
        ppq = st.text_input('**MDVP:PPQ**')
        
    with col2:
        ddp = st.text_input('**DDP**')
        
    with col3:
        shimmer = st.text_input('**SHIMMER**')
        
    with col1:
        shimmer_db = st.text_input('**SHIMMER(dB)**')
        
    with col2:
        apq3 = st.text_input('**APQ3**')
        
    with col3:
        apq5 = st.text_input('**APQ5**')
        
    with col1:
        apq = st.text_input('**APQ**')
        
    with col2:
        dda = st.text_input('**DDA**')
        
    with col3:
        nhr = st.text_input('**NHR**')
        
    with col1:
        hnr = st.text_input('**HNR**')
        
    with col2:
        rpde = st.text_input('**RPDE**')
        
    with col3:
        dfa = st.text_input('**DFA**')
        
    with col1:
        spread1 = st.text_input('**SPREAD 1**')
        
    with col2:
        spread2 = st.text_input('**SPREAD 2**')
        
    with col3:
        d2 = st.text_input('**D2**')
        
    with col1:
        ppe = st.text_input('**PPE**')

    parkinsons_diagnosis = '' 
    
    if st.button('Parkinsons Disease Test Result'):
        
        user_input = [fo, fhi, flo, jitter_per, jitter_abs, rap, ppq, ddp, shimmer, shimmer_db, apq3, apq5, apq, dda, nhr, hnr, rpde, dfa, spread1, spread2, d2, ppe]
        
        user_input = [float(x) for x in user_input]
        
        parkinsons_prediction = parkinsons_model.predict([user_input])
        
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis= 'The person IS HAVING parkinsons disease'
            bg_color = 'red'
        else:
            parkinsons_diagnosis = 'The person DOES NOT HAVE parkinsons disease'
            bg_color = 'green'
        st.markdown(f'<div style="background-color:{bg_color};padding:10px;border-radius:5px;">{heart_diagnosis}</div>', unsafe_allow_html=True)


    