import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def ap():
    # Code for Prediction
    heart_diagnosis = ''
    parkinsons_diagnosis = ''
    diab_diagnosis = ''

    def send_to_expert(user_input):
        # Email configurations
        email_sender = 'your_email@gmail.com'
        email_receiver = 'expert_email@example.com'
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'your_email@gmail.com'
        smtp_password = 'your_email_password'

        # Construct email body
        body = ''
        for key, value in user_input.items():
            body += f"{key}: {value}\n"

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = 'Health Assistant: User Input'
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Create SMTP session
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            # Login credentials for sending the mail
            server.login(smtp_username, smtp_password)
            # Send email
            server.sendmail(email_sender, email_receiver, msg.as_string())
            server.quit()
            st.success('Your input has been sent to the expert.')
        except Exception as e:
            st.error(f'Error: {e}')

    # Styling
    st.markdown("""
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f0f0;
            }
            .sidebar .sidebar-content .block-container {
                color: #333;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                font-size: 16px;
            }
            .stButton>button:hover {
                background-color: #45a049;
            }
            .stTextInput>div>div>input {
                border-radius: 5px;
                border: 1px solid #ccc;
                padding: 10px;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Load saved models
    working_dir = os.path.dirname(os.path.abspath(__file__))
    diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))
    heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
    parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

    with st.sidebar as sidebar:
        selected = option_menu(
            'Multiple Disease Prediction System',
            ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction', 'Expert Help'],
            menu_icon='hospital-fill',
            icons=['activity', 'heart', 'person'],
            default_index=0)

    if selected == 'Expert Help':
        st.title('Expert Help')

        # Collect user input
        user_input = {}
        user_input = st.session_state['user_input']
        st.write('Please provide some details:')
        for field in ['Name', 'Age', 'Gender', 'Symptoms', 'Other Details']:
            user_input[field] = st.text_input(field)

        # Send input to expert
        if st.button('Send to Expert'):
            send_to_expert(user_input)

    # Diabetes Prediction Page
    if selected == 'Diabetes Prediction':

        # Page title
        st.title('Diabetes Prediction using ML')

        # Getting the input data from the user
        col1, col2, col3 = st.columns(3)

        with col1:
            min_pregnancies = 0
            max_pregnancies = 100
            Pregnancies = st.number_input('Number of Pregnancies', min_value=min_pregnancies, max_value=max_pregnancies)
            st.write(f"Min: {min_pregnancies}, Max: {max_pregnancies}")

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')

        if st.button('Diabetes Test Result'):
            user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
            user_input = [float(x) for x in user_input]

            diab_prediction = diabetes_model.predict([user_input])

            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)

    # Heart Disease Prediction Page
    if selected == 'Heart Disease Prediction':

        # Page title
        st.title('Heart Disease Prediction using ML')

        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        if st.button('Heart Disease Test Result'):
            user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
            user_input = [float(x) for x in user_input]

            heart_prediction = heart_disease_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'

            st.success(heart_diagnosis)

    # Parkinson's Prediction Page
    if selected == "Parkinsons Prediction":

        # Page title
        st.title("Parkinson's Disease Prediction using ML")

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        if st.button("Parkinson's Test Result"):
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            user_input = [float(x) for x in user_input]

            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)

if __name__ == "__main__":
    ap()
