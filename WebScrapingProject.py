import os

from screener import screener_func

# Adjust working directory if needed
current_directory = os.getcwd()
folder_name = os.path.basename(current_directory)
if folder_name != "Project_IDEAS_CO21":
    os.chdir("../../")


import streamlit as st
import pandas as pd
from tofler import tofler_func
from fetch_tofler import fetch_tofler
from zauba import zauba_func




# Function to load company list from a CSV file
def company_list(csv_file):
    df = pd.read_csv(csv_file)
    return sorted(set([i.title().upper().replace(" PVT.", "").replace(" LTD.", "").replace(" LTD","").replace(" PVT","").strip() for i in
                       df["Company Name"].to_list()]))


# Streamlit page configuration
st.set_page_config("Data Scraper Project")
st.markdown(
    """
  <style>
  .css-d1b1ld.edgvbvh6, .css-1v8iw7l.eknhn3m4 { visibility:hidden; }
  #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stForm.st-emotion-cache-4uzi61.e10yg2by1 > div > div > div > div:nth-child(2) > div > div > div > div > svg { visibility:hidden; }
  </style>
  """, unsafe_allow_html=True
)

# Main title
st.markdown("<h1 style='text-align:center;'>Data Scraping Website</h1>", unsafe_allow_html=True)

# Load data for company selection
all_stocks = company_list("Company_list.csv")
fetched_stocks = company_list("Fetch_list.csv")

# Form 1: Data Source Selection and Company Selection
with st.form("Details_Form"):
    comp = st.radio("From which site do you want to access the data?", ["Tofler", "Zauba","Screener"], key="site_radio")
    data = st.selectbox("Enter the company name:", options=all_stocks, index=None, placeholder="Type Here...",
                        key="company_select")
    if data=="OTHER OPTION" or data=="":
      data = st.text_input("Enter company name here: ")
    submit = st.form_submit_button("Submit")

# Form 2: Stored Data Selection
with st.form("Storage_Form"):
    fetched_data = st.selectbox("Select from stored data for faster results:", options=fetched_stocks, index=None,
                                placeholder="Type Here...", key="stored_data_select")
    submit2 = st.form_submit_button("Search")

# Display Demo Video
process1 = st.empty()
process2 = st.empty()
process1.markdown("<h3 style='text-align:center;'>Demo of How The Website Works</h3>", unsafe_allow_html=True)
process2.video("demo.mp4")

# Handling stored data fetching
if submit2:
    if fetched_data:
        st.write("Fetching details from Storage...")
        try:
            fetch_tofler(fetched_data)
        except Exception as e:
            st.error("Error fetching data. Please try another company.")
            st.write(str(e))

# Handling form data submission
if submit:
    # Fetch details based on selected site
    if data:
        process1.empty()
        process2.empty()
        st.write(f"Fetching details from {comp}...")

        try:
            if comp == "Tofler":
                tofler_func(data, flag=0)
            elif comp == "Zauba":
                zauba_func(data, flag=0)
            elif comp=="Screener":
                screener_func(data,flag=0)
        except Exception as e:
            st.error("Error fetching data. Please try another company.")
            st.write(str(e))
