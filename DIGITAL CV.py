from pathlib import Path

import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).oarent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/ "main.css"
resume_file = current_dir / "assets" / "Ian Cris Tocle_CV.pdf"
profile_pic = current_dir / "assets" / "PHOTO_IAN CRIS TOCLE"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ian Cris Tocle"
PAGE_ICON = ":wave:"
NAME = "Ian Cris Tocle"
DESCRIPTION = """
Fresh Graduate at Oxford Brookes University | ACCA Student | Accountant | Data Analyst | Musician | YouTuber | Always looking forward to further development
"""
EMAIL = "ic.tocle@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn: https://www.linkedin.com/in/ian-cris-tocle-6315a4235/",
    "Facebook: https://www.facebook.com/iancris.tocle/"
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