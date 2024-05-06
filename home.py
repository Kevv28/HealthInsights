import streamlit as st

def app():
    # Page title and logo
    st.title("Welcome to HealthInsights")
    st.image("D:\multiple-disease-prediction-streamlit-app\health_insights_group_cover.jpg", use_column_width=True)  # Add the path to your logo image file

    # Custom CSS
    st.markdown(
        """
        <style>
            /* Custom CSS styles */
            .page-container {
                max-width: 800px;
                margin: auto;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
            .section-title {
                font-size: 24px;
                color: #0056b3;
                margin-top: 30px;
                margin-bottom: 15px;
            }
            .section-content {
                font-size: 18px;
                line-height: 1.5;
                margin-bottom: 20px;
            }
            footer {
                text-align: center;
                margin-top: 50px;
                font-size: 14px;
                color: #666;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main content container
    st.markdown("<div class='page-container'>", unsafe_allow_html=True)

    # Introduction
    st.markdown("<p class='section-content'>HealthInsights is your comprehensive health assistant, providing predictions and expert help for various health conditions. Use the navigation menu on the left to explore the features.</p>", unsafe_allow_html=True)

    # About HealthInsights
    st.markdown("<h2 class='section-title'>About HealthInsights</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>HealthInsights is a platform designed to assist users in predicting various health conditions such as diabetes, heart disease, and Parkinson's disease. Our goal is to empower individuals to make informed decisions about their health with the help of machine learning models and expert advice.</p>", unsafe_allow_html=True)

    # Features
    st.markdown("<h2 class='section-title'>Key Features</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>- <strong>Multiple Disease Prediction</strong>: Predict diabetes, heart disease, and Parkinson's disease.</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>- <strong>Expert Help</strong>: Get expert advice by providing your health details.</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>- <strong>Informative Blogs</strong>: Access informative blogs on health-related topics.</p>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>- <strong>About Us</strong>: Learn more about our team and mission.</p>", unsafe_allow_html=True)

    # Prediction Section
    st.markdown("<h2 class='section-title'>Disease Prediction</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>Use the navigation menu to select the disease you want to predict:</p>", unsafe_allow_html=True)
    st.markdown("<ul class='section-content'><li>Diabetes Prediction</li><li>Heart Disease Prediction</li><li>Parkinson's Prediction</li></ul>", unsafe_allow_html=True)

    # Expert Help Section
    st.markdown("<h2 class='section-title'>Expert Help</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>If you need expert advice or assistance, you can provide your health details and get personalized recommendations from our team of experts. Click on the <strong>Expert Help</strong> option in the navigation menu to get started.</p>", unsafe_allow_html=True)

    # Informative Blogs Section
    st.markdown("<h2 class='section-title'>Informative Blogs</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>Explore our collection of informative blogs on various health-related topics. Stay informed and up-to-date with the latest insights and research. Click on the <strong>Blogs</strong> option in the navigation menu to browse our blog posts.</p>", unsafe_allow_html=True)

    # About Us Section
    st.markdown("<h2 class='section-title'>About Us</h2>", unsafe_allow_html=True)
    st.markdown("<p class='section-content'>Learn more about our team, mission, and vision. Discover the people behind HealthInsights and our commitment to improving healthcare outcomes. Click on the <strong>About Us</strong> option in the navigation menu to find out more.</p>", unsafe_allow_html=True)

    # Close main content container
    st.markdown("</div>", unsafe_allow_html=True)

    # Copyright
    st.markdown("<footer>&copy; 2024 HealthInsights. All rights reserved.</footer>", unsafe_allow_html=True)
