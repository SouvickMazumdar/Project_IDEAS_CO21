import os
current_directory = os.getcwd()  # Get the current working directory
folder_name = os.path.basename(current_directory)  # Extract the folder name
if folder_name!="Project_IDEAS_CO21":
  os.chdir("../../")
import streamlit as st
import pandas as pd
from tofler import tofler_func
from fetch_tofler import fetch_tofler
from zauba import zauba_func
import time
flag=0
# file=open('auto_data.txt','r+')
# data=file.readlines()
# all_stocks=[i.title().replace(" Pvt.","").replace(" Ltd.","").replace(" Ltd","").replace(" Pvt","").strip() for i in data]
# all_stocks.append("")
# all_stocks.append("Other Option")
# all_stocks=list(sorted(set(all_stocks)))
def company_list(csv_file):
  df = pd.read_csv(csv_file)
  l=[i.title().upper().replace(" PVT.","").replace(" LTD.","").replace(" LTD","").replace(" PVT","").strip() for i in df["Company Name"].to_list()]
  return l
st.set_page_config("Data Scraper Project")
st.markdown("""
<style>
.css-d1b1ld.edgvbvh6
{
  visibility:hidden;
}
.css-1v8iw7l.eknhn3m4
{
  visibility:hidden;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.stAppViewBlockContainer.block-container.st-emotion-cache-13ln4jf.ea3mdgi5 > div > div > div > div.stForm.st-emotion-cache-4uzi61.e10yg2by1 > div > div > div > div:nth-child(2) > div > div > div > div > svg
{
  visibility:hidden;
}

</style>
""",unsafe_allow_html=True)

submit=False
submit2=False
st.markdown("<h1 style='text-align:center;'>Data Scraping Website</h1>",unsafe_allow_html=True)
form1 = st.form("Details")
comp = form1.radio("From which site do you want to access the data?",["Tofler","Zauba"])
all_stocks=company_list("Company_list.csv")
data = form1.selectbox("Enter the company name : (If name is not listed in the list, then write 'Other Option')",options=all_stocks,placeholder="Type Here...",index=None)
submit = form1.form_submit_button("Submit")


form2 = st.form("Storage")
fetched_stocks=company_list("Fetch_list.csv")
fetched_data=""
fetched_data=form2.selectbox("We have few pre stored Data. For faster result search your company here (It may contain older data).",options=fetched_stocks,placeholder="Type Here...",index=None)
submit2 = form2.form_submit_button("Submit")
form2 = st.form("Details2")
process1=st.empty()
process2=st.empty()
process1.markdown("<h3 style='text-align:center;'>Demo of How The Website Works</h3>",unsafe_allow_html=True)
process2.video("demo.mp4")

while submit2:
  if fetched_data is not None:
    # print(fetched_data)
    st.write("Fetching details from Storage")
    try:
      fetch_tofler(fetched_data)
      break
    except Exception:
      st.write("""The site landed onto an error while handling the request.
                        Kindly search again.
                        If still the error pertains, then the company might not be listed on the particular website.
                        Try searching for some other company.
                     """)

while submit:
  if(data=='OTHER OPTION' or data==''):
    data = form1.text_input("Enter company name here: ",)
  else:
    process2.text("")
    process1.text("")
    if comp=="Tofler":
      st.write("Fetching details from "+comp)
      try:
        ret = tofler_func(data,flag)
      except Exception:
        st.write("""The site landed onto an error while handling the request.
                    Kindly search again.
                    If still the error pertains, then the company might not be listed on the particular website.
                    Try searching for some other company.
                 """)
    elif comp=="Zauba":
      st.write("Fetching details from "+comp)
      try:
        pass
      except Exception:
        st.write("""The site landed onto an error while handling the request.
                    Kindly search again.
                    If still the error pertains, then the company might not be listed on the particular website.
                    Try searching for some other company.
                 """)
    break
