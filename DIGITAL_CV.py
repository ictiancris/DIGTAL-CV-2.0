from pathlib import Path

import streamlit as st
from PIL import Image

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"styles"/"main.css"
resume_file = current_dir/"assets"/"Ian Cris Tocle_CVUPDATE.pdf"
profile_pic = current_dir/"assets"/"IAN CRIS NEW PHOTO.jpeg"
video_1 = current_dir/"assets"/"EXCEL + POWER BI RECEIVLA FINAL.mp4"
video_2 = current_dir/"assets"/"CPV FINAL.mp4"
video_3 = current_dir/"assets"/"MACHINE LEARNING.mp4"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ian Cris Tocle"
PAGE_ICON = ":wave:"
NAME = "Ian Cris Tocle"
DESCRIPTION = """
Filipino, 10/31/2003

Financial Analyst | Accountant | Data Science/Data Analyst | UAE Residence Visa
"""
EMAIL = "ic.tocle@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ian-cris-tocle-6315a4235/",
    "Facebook": "https://www.facebook.com/iancris.tocle/",
    "Facebook": "iancris.tocle@yahoo.com",
}
EDUCATION_AND_CERTIFICATION = {
    "Bachelor's Degree of Applied Accounting Graduate of Oxford Brookes University (OBU)",
    "ACCA Diploma and Advanced Diploma in Accounting and Business",
    "Financial Analyst Certification",
    "IBM Professional Certificate",
    "Google Analytics Professional Certificate",
    "Microsoft Power BI Certificate (On going)"
}
PROJECTS = {
    "Google Data Analytics Capstone Project",
    "IBM Data Analytics Capstone Project",
    "Machine Learning Auto-Attendance + AI Facial Recognition (Python)",
    "Budgeting and Forecasting (Excel Template)",
    "Aged Receivable and Payable Analysis (Excel Template)",
    "Power BI Dashboard and Reports Analysis",
    "Cheque Payment Voucher Template (Excel/VBA)",
    "Tableau - Data Visualization",
    "Full-Depth Financial Report and Research Analysis Thesis (OBU)",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello there!")

#---LOAD CSS, PDF & PROFILE PIC---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Define your email address and password
MY_EMAIL = "iancris.tocle@yahoo.com"
MY_PASSWORD = "TRICviolin2003"

# Define the recipient email address
TO_EMAIL = "iancris.tocle@yahoo.com"

# Define the email message template
MESSAGE_TEMPLATE = """
From: {name} <{email}>
Subject: {subject}

{message}
"""

#---CREATE SIDEBAR MENU---
menu_items = ["About Me", "Education and Certifications", "Projects", "Skills", "Contact Me"]
choice = st.sidebar.selectbox("Select an option", menu_items)

#---HERO SECTION---
hero_container = st.container()
with hero_container:
    st.image(profile_pic, width=150, use_column_width='always')
    st.markdown(f"<h1 style='text-align: center;'>{NAME}</h1>", unsafe_allow_html=True)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("📧", EMAIL)

#---SHOW SELECTED CONTENT---
if choice == "About Me":
    st.write(DESCRIPTION)
elif choice == "Education and Certifications":
    st.write("##")
    st.subheader("EDUCATION AND CERTIFICATIONS")
    st.write(
        """
         - Bachelor's Degree of Applied Accounting Graduate of Oxford Brookes University (OBU)
         - ACCA Diploma and Advanced Diploma in Accounting and Business
         - Financial Analyst Certification
         - IBM Professional Certificate
         - Google Analytics Professional Certificate
         - Microsoft Power BI Certificate (On going)
        """
        )

elif choice == "Projects":
    st.write("#")
    st.subheader("Projects")
    st.write(
        """
        - Google Data Analytics Capstone Project
        - IBM Data Analytics Capstone Project
        - Machine Learning Auto-Attendance + AI Facial Recognition (Python)
        - Budgeting and Forecasting (Excel Template)
        - Aged Receivable and Payable Analysis (Excel Template)
        - Power BI Dashboard and Reports Analysis
        - Cheque Payment Voucher Template (Excel/VBA)
        - Tableau - Data Visualization
        - Full-Depth Financial Report and Research Analysis Thesis (OBU)


        """
    )
    video_1 = open(video_1, "rb")
    video_2 = open(video_2, "rb")
    video_3 = open(video_3, "rb")

    st.write("##")
    with st.expander("VIDEOS"):
        st.video(video_1)
        st.video(video_2)
        st.video(video_3)
elif choice == "Skills":
    st.write("#")
    st.subheader("SKILLS")
    st.write(
        """
        - Financial Data Analysis
        - Power BI and Tableau Data Visualizations
        - Python Framework and Libraries (Jupyter-IDE)
        - HTML-CSS-Javascript/Power Page/Wordpress (VSCode)
        - Public Speaking - (Gavels and PBS)
        - MS Office Excel/Word/Powerpoint/Outlook
        - Photo / Video Editing
        - PC Networking / Gaming


        """
    )
    st.expander("Language")
    st.write(
            """
            - Filipino
            - English
            """
            )
elif choice == "Contact Me":
    st.write("##")
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    
    st.write("## Contact Me")
    st.write("Use the form below to send me a message:")
    name = st.text_input("Name")
    email = st.text_input("Email")
    subject = st.text_input("Subject")
    message = st.text_area("Message")
    if st.button("Submit"):
        # Create the email message
        message_text = MESSAGE_TEMPLATE.format(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        message = MIMEMultipart()
        message["From"] = MY_EMAIL
        message["To"] = TO_EMAIL
        message["Subject"] = subject
        message.attach(MIMEText(message_text, "plain"))

        # Send the email using SMTP
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login(MY_EMAIL, MY_PASSWORD)
            smtp.sendmail(MY_EMAIL, TO_EMAIL, message.as_string())
        st.write("Message sent!")
    
 






