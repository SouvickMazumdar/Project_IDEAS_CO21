import time
from datetime import datetime
import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from IPython.display import HTML, display_html
import duckdb
import os
import csv
def company_list(csv_file):
  df = pd.read_csv(csv_file)
  l = [i.replace(" LTD", "").replace(" LTD.", "").replace(" Pvt.","").replace(" Pvt","").strip() for i in df["Company Name"].to_list()]
  return l
def tofler_func(option_company,flag):

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (for better performance)
    chrome_options.add_argument("--no-sandbox")  # Required if running as root
    chrome_options.add_argument("--disable-dev-shm-usage")
    browser= webdriver.Chrome(options=chrome_options)
    url = 'https://www.tofler.in/'
    browser.get(url)
    try:
        # browser.minimize_window()
        input_company = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#searchbox"))
        )
        input_company.send_keys(option_company)
        time.sleep(1)
        input_company.send_keys(Keys.ARROW_DOWN)
        time.sleep(1)
        input_company.send_keys(Keys.ENTER)
        time.sleep(2)

        # OVERVIEW part
        content=""
        try:
            try:
                browser.find_element(By.XPATH,"/html/body/section[5]/section[2]/div[1]/div[1]/p").click()
            except Exception:
                pass

            content_div = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/section[5]/section[2]/div[1]/div[1]/div[3]"))
            )
            paragraphs = content_div.find_elements(By.TAG_NAME, 'p')
            content = "\n\n".join([paragraph.text for paragraph in paragraphs])
            st.write(f"<h2>Overview of Company - {option_company}</h2>", unsafe_allow_html=True)
            st.write(content)
            os.chdir("Backend")
            os.makedirs(f"{option_company}", exist_ok=True)
            os.chdir(f"{option_company}")

            conn = duckdb.connect(f'{option_company}.duckdb')

            # Function to save DataFrame to DuckDB, appending data to the same table
            def save_dataframe_to_duckdb(df, table_name="data_table"):
                # Check if table exists; if not, create it
                conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} AS SELECT * FROM df WHERE 1=0")
                # Insert data into the table
                conn.execute(f"INSERT INTO {table_name} SELECT * FROM df")


            with open("overview.txt", 'w') as file:
                file.write(content)
            with open("Extract_date.txt", 'w') as file:
                file.write(datetime.now().strftime("%d/%m/%Y"))

            os.chdir("../../")
            if option_company not in company_list("Fetch_list.csv"):
                with open("Fetch_list.csv", 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([option_company])
            os.chdir(f"Backend/{option_company}")
        except Exception:
            pass

        # Registration Details
        reg_d=""
        try:
            reg_div=browser.find_element(By.ID,"registered-details-module")
            reg=reg_div.find_element(By.CLASS_NAME,"registered_box_wrapper")
            child_reg=reg.find_elements(By.TAG_NAME,"div")
            reg_d = []
            for child in child_reg:
                left=child.find_element(By.TAG_NAME,"h3")
                right=child.find_element(By.TAG_NAME,"span")
                reg_d.append([left.text,right.text])
            ext=reg_div.find_element(By.CLASS_NAME,"gap-4")
            child_ext=ext.find_elements(By.TAG_NAME,"div")
            kt=["Type"]
            mt=""
            for child in child_ext:
                mt=mt+child.text+","
            kt.append(mt[0:-1])
            reg_d.append(kt)
            table = pd.DataFrame(reg_d, columns=["TYPE", "Value"])
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Registration Details</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Registration_details")
            stored_data = conn.execute("SELECT * FROM Registration_details").fetchdf()
            # print(stored_data)
        except Exception:
            pass

        # Directors
        dir_table=""
        try:
            director_div=browser.find_element(By.ID,"people-module")
            director=director_div.find_element(By.TAG_NAME,"tbody")
            child_elements=director.find_elements(By.TAG_NAME, "tr")
            dir_table=[]
            # print(len(child_elements),"$"*100)
            for child in child_elements:
                td_child=child.find_elements(By.TAG_NAME,"td")
                des = td_child[0].text
                name = td_child[1].text
                if name.find('\n')!=-1:
                    name=name[0:name.find('\n')]
                din = td_child[2].text
                tenure = td_child[3].text
                dir_table.append([des, name, din, tenure])
            table = pd.DataFrame(dir_table, columns=["Designation", "Name", "DIN/PAN", "Tenure"])
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Directors</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Directors")
        except Exception:
            pass


        # Charges on asset
        asset_table=""
        try:
            tar_ass=browser.find_element(By.XPATH,"/html/body/section[5]/section[13]/div/div[2]/div[1]/div[1]")
            child_asst=tar_ass.find_elements(By.CLASS_NAME,"mobile-hide")
            asset_table=[]
            for child in child_asst:
                sub_child=child.find_element(By.CLASS_NAME,"flex-col")
                sub_child=sub_child.find_elements(By.TAG_NAME,"p")
                one=sub_child[0].text
                two=sub_child[1].find_element(By.TAG_NAME,"span").text
                three=sub_child[2].find_element(By.TAG_NAME,"span").text
                asset_table.append([one,two,three])
            table = pd.DataFrame(asset_table, columns=["Asset Name", "No. of Loans", "Total Amount"])
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Charges on Assets</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Asset")
            stored_data = conn.execute("SELECT * FROM Asset").fetchdf()
            # print(stored_data)
        except Exception:
            pass




        # Key Metrics
        key_table=""
        try:
            key_div=browser.find_element(By.XPATH,"/html/body/section[5]/section[2]/div[3]/div[1]/div[2]/div[2]")
            key_child=key_div.find_elements(By.CLASS_NAME,"flex-col")
            key_table=[]
            for child in key_child:
                one=child.find_element(By.CLASS_NAME,"font-regular").text
                two=child.find_element(By.CLASS_NAME,"text-dark").text
                three=child.find_element(By.CLASS_NAME,"text-sm").text
                if one.find("GET PRO")!=-1 or two.find("GET PRO")!=-1 or three.find("GET PRO")!=-1:
                    key_table=""
                    raise
                key_table.append([one,two,three])
            table = pd.DataFrame(key_table, columns=["KEY", "VALUE", "INC/DEC"])
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Key Metrics</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Metrics")
        except Exception:
            pass

        # Financial Part
        fin_ar=""
        try:
            # browser.find_element(By.ID,"financials-tab").click()
            fin_tab=browser.find_element(By.XPATH,"/html/body/section[5]/section[9]/div/div[2]/div[1]/table/tbody")
            child_elements=fin_tab.find_elements(By.TAG_NAME,"tr")
            # child_elements=child_elements[1:-1]
            fin_ar=[]
            for child in child_elements:
                k=child.find_elements(By.TAG_NAME,"td")
                # print(k)
                one=k[0].text
                two=k[1].text
                three=k[2].text
                four=k[3].text
                five=k[4].text
                six=k[5].text
                if one.find("GET PRO")!=-1 or two.find("GET PRO")!=-1 or three.find("GET PRO")!=-1 or four.find("GET PRO")!=-1 or five.find("GET PRO")!=-1 or six.find("GET PRO")!=-1:
                    fin_ar=""
                    raise
                fin_ar.append([one,two,three,four,five,six])
            fin_table = pd.DataFrame(fin_ar, columns=["", "March 2019", "March 2020", "March 2021", "March 2022",
                                                         "March 2023", ])
            # del fin_table[fin_table.columns[-1]]
            fin_table.index = range(1, len(fin_table) + 1)

            st.markdown('<h2>Financial Highlights</h2>', unsafe_allow_html=True)
            # financial_table_html=create_financial_table(fin_table)
            # components.html(financial_table_html, height=1000)
            st.dataframe(fin_table, use_container_width=True)
            save_dataframe_to_duckdb(fin_table, "Finance")
        except Exception:
            pass
        if content == "" and fin_ar == "" and key_table == "" and reg_d == "" and dir_table == "" and asset_table == "":
            st.markdown('<h2>No Data Found. Try Some other company</h2>', unsafe_allow_html=True)
    except Exception:
        browser.quit()
    finally:
        if flag==1:
            return option_company
