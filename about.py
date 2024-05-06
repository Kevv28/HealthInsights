
import streamlit as st

def about_us():
    st.markdown(
        """
        <style>
            /* CSS for the about us page */
            .about-container {
                max-width: 800px;
                margin: auto;
                padding: 50px 20px;
                background-color: #f9f9f9;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .section-title {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
                color: #333;
            }
            .content {
                line-height: 1.6;
                color: #555;
            }
            .mission-vision-aim {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 30px;
                margin-top: 30px;
            }
            .mission-vision-aim .box {
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
            }
            .mission-vision-aim .box h3 {
                font-size: 20px;
                color: #333;
                margin-bottom: 10px;
            }
            .mission-vision-aim .box p {
                color: #555;
            }
            .icon {
                font-size: 36px;
                margin-bottom: 10px;
                color: #0056b3;
            }
        </style>
        """
        , unsafe_allow_html=True)

    st.title("About HealthInsights")

    st.markdown(
        """
        <div class="about-container">
            <div class="section-title">Our Vision, Mission, and Aim</div>
            <div class="content">
                <p>Welcome to HealthInsights! We are dedicated to providing cutting-edge solutions and insights in the field of healthcare. Our platform is designed to empower individuals to make informed decisions about their health and well-being.</p>
                <div class="mission-vision-aim">
                    <div class="box">
                        <i class="icon fas fa-eye"></i>
                        <h3>Vision</h3>
                        <p>To be a global leader in leveraging technology to revolutionize healthcare accessibility and outcomes.</p>
                    </div>
                    <div class="box">
                        <i class="icon fas fa-rocket"></i>
                        <h3>Mission</h3>
                        <p>To provide innovative tools and resources that enable individuals to proactively manage their health and prevent diseases.</p>
                    </div>
                    <div class="box">
                        <i class="icon fas fa-bullseye"></i>
                        <h3>Aim</h3>
                        <p>To create a healthier world by promoting health literacy, fostering collaboration among healthcare stakeholders, and harnessing the power of data-driven insights.</p>
                    </div>
                </div>
            </div>
        </div>
        """
        , unsafe_allow_html=True)

if __name__ == "__main__":
    about_us()
