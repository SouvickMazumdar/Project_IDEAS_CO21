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
def screener_func(option_company,flag):

    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without GUI)
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (for better performance)
    chrome_options.add_argument("--no-sandbox")  # Required if running as root
    chrome_options.add_argument("--disable-dev-shm-usage")
    browser= webdriver.Chrome(options=chrome_options)
    url = 'https://www.screener.in/'
    browser.get(url)
    try:
        # browser.minimize_window()
        input_company = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/main/div[2]/div/div/div/input"))
        )
        input_company.send_keys(option_company)
        time.sleep(1)
        # input_company.send_keys(Keys.ARROW_DOWN)
        # time.sleep(1)
        input_company.send_keys(Keys.ENTER)
        time.sleep(2)

        # About part
        content=""
        try:
            try:
                browser.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[1]/div[1]/div[2]/button").click()
            except Exception:
                pass

            content_div = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/div[3]/div[3]/div[1]/div[1]/div[2]/p"))
            )
            # paragraphs = content_div.find_elements(By.TAG_NAME, 'p')
            content = content_div.text
            # content = "\n\n".join([paragraph.text for paragraph in paragraphs])
            st.write(f"<h2>Overview of Company - {option_company}</h2>", unsafe_allow_html=True)
            st.write(content)
            os.chdir("Backend")
            os.makedirs(f"{option_company}", exist_ok=True)
            os.chdir(f"{option_company}")
            if os.path.exists(f'{option_company}.duckdb'):
                os.remove(f'{option_company}.duckdb')

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
            with open("Source_data.txt", 'w') as file:
                file.write("Screener")

            os.chdir("../../")
            if option_company not in company_list("Fetch_list.csv"):
                with open("Fetch_list.csv", 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([option_company])
            os.chdir(f"Backend/{option_company}")
        except Exception:
            pass

        # Basic Details
        basic_d=""
        try:
            reg_div=browser.find_element(By.XPATH,"/html/body/main/div[3]/div[3]/div[2]/ul")
            child_elements=reg_div.find_elements(By.ID,"li")
            str1=""
            for child in child_elements:
                str1=str1+child.text+"\n\n"


            # print("hello1")
            # reg=reg_div.find_element(By.CLASS_NAME,"registered_box_wrapper")
            child_reg=reg_div.find_elements(By.CLASS_NAME,"flex-space-between")
            # print("hello2")
            basic_d = []
            for child in child_reg:
                # print(child.text)
                left=child.find_element(By.CLASS_NAME,"name")
                right=child.find_element(By.CLASS_NAME,"nowrap")
                # print(left.text)
                # print(right.text)
                # print("*********")
                basic_d.append([left.text,right.text])
            table = pd.DataFrame(basic_d, columns=["TYPE", "Value"])
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Basic Details</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Basic_details")
            # stored_data = conn.execute("SELECT * FROM Registration_details").fetchdf()
            # print(stored_data)
        except Exception:
            pass


        # PROS
        # Pros="/html/body/main/section[2]/div/div[1]/ul"
        pro_con_table = ""
        try:
            # print("hello1")
            pro_div = browser.find_element(By.XPATH, "/html/body/main/section[2]/div/div[1]/ul")
            # print("hello2")
            # director = pro_div.find_element(By.TAG_NAME, "tbody")
            child_elements_pro = pro_div.find_elements(By.TAG_NAME, "li")
            # print("hello3")
            con_div = browser.find_element(By.XPATH, "/html/body/main/section[2]/div/div[2]/ul")
            # director = pro_div.find_element(By.TAG_NAME, "tbody")
            # print("hello4")
            child_elements_con = con_div.find_elements(By.TAG_NAME, "li")
            # print("hello5")
            pro_con_table = []
            pro_lis=[]
            con_lis=[]
            # print(len(child_elements),"$"*100)
            for child in child_elements_pro:
                pro_lis.append(child.text)
            for child in child_elements_con:
                con_lis.append(child.text)
            # print("Pro: ",pro_lis)
            # print("Con: ",con_lis)
            st_pr=len(pro_lis)
            st_cn=len(con_lis)
            max_st=max(st_pr,st_cn)
            # print(max_st)
            for i in range(max_st):
                if i<st_pr and i<st_cn:
                    pro_con_table.append([pro_lis[i],con_lis[i]])
                elif i>=st_pr:
                    pro_con_table.append(["",con_lis[i]])
                elif i>=st_cn:
                    pro_con_table.append([pro_lis[i],""])
            # print(pro_con_table)
            table = pd.DataFrame(pro_con_table, columns=["Pro","Con"])
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Pros and Cons</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Pros_and_Cons")
        except Exception:
            pass


        # Quarterly results
        quat_table=""
        try:
            # print("Hello0")
            top_thead= browser.find_element(By.ID, "quarters")
            top2_head=top_thead.find_element(By.CLASS_NAME,"responsive-text-nowrap")
            t_head=top2_head.find_element(By.TAG_NAME,"thead")
            # director = pro_div.find_element(By.TAG_NAME, "tbody")
            # print("Hello1")
            child_elements_t_head = t_head.find_elements(By.TAG_NAME, "th")
            # print("Hello2")
            column_names=[]
            for i in child_elements_t_head:
                column_names.append(i.text)
            # print("Head",column_names)
            t_body=top2_head.find_element(By.TAG_NAME,"tbody")
            # print("Hello3")
            child_elements_t_body=t_body.find_elements(By.TAG_NAME,"tr")
            # print("Hello4")
            quat_table = []
            for i in child_elements_t_body:
                childs=i.find_elements(By.TAG_NAME,"td")
                l_row=[]
                for j in childs:
                    # l_row.append(j.text)
                    l_row.append(j.text.replace("&nbps", "").replace("+", ""))
                quat_table.append(l_row)
            # print(len(quat_table))
            # print(len(quat_table[0]))
            # print("Body: ",quat_table)
            table = pd.DataFrame(quat_table, columns=column_names)
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Quarterly Details (in Cr)</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Quarterly_Results")
        except Exception as e:
            # print(e)
            pass

        # Profit Loss results
        PL_table = ""
        try:
            # print("Hello0")
            top_thead = browser.find_element(By.ID, "profit-loss")
            top2_head = top_thead.find_element(By.CLASS_NAME, "responsive-text-nowrap")
            t_head = top2_head.find_element(By.TAG_NAME, "thead")
            # director = pro_div.find_element(By.TAG_NAME, "tbody")
            # print("Hello1")
            child_elements_t_head = t_head.find_elements(By.TAG_NAME, "th")
            # print("Hello2")
            column_names = []
            for i in child_elements_t_head:
                column_names.append(i.text)
            # print("Head",column_names)
            t_body = top2_head.find_element(By.TAG_NAME, "tbody")
            # print("Hello3")
            child_elements_t_body = t_body.find_elements(By.TAG_NAME, "tr")
            # print("Hello4")
            PL_table = []
            for i in child_elements_t_body:
                childs = i.find_elements(By.TAG_NAME, "td")
                l_row = []
                for j in childs:
                    # l_row.append(j.text)
                    l_row.append(j.text.replace("&nbps", "").replace("+", ""))
                PL_table.append(l_row)
            # print(len(quat_table))
            # print(len(quat_table[0]))
            # print("Body: ",quat_table)
            table = pd.DataFrame(PL_table, columns=column_names)
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Profit & Loss Details (in Cr)</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Profit_and_Loss")
        except Exception as e:
            # print(e)
            pass

        # Balance results
        balance_table = ""
        try:
            # print("Hello0")
            top_thead = browser.find_element(By.ID, "balance-sheet")
            top2_head = top_thead.find_element(By.CLASS_NAME, "responsive-text-nowrap")
            t_head = top2_head.find_element(By.TAG_NAME, "thead")
            # director = pro_div.find_element(By.TAG_NAME, "tbody")
            # print("Hello1")
            child_elements_t_head = t_head.find_elements(By.TAG_NAME, "th")
            # print("Hello2")
            column_names = []
            for i in child_elements_t_head:
                column_names.append(i.text)
            # print("Head",column_names)
            t_body = top2_head.find_element(By.TAG_NAME, "tbody")
            # print("Hello3")
            child_elements_t_body = t_body.find_elements(By.TAG_NAME, "tr")
            # print("Hello4")
            balance_table = []
            for i in child_elements_t_body:
                childs = i.find_elements(By.TAG_NAME, "td")
                l_row = []
                for j in childs:
                    # l_row.append(j.text)
                    l_row.append(j.text.replace("&nbps", "").replace("+", ""))
                balance_table.append(l_row)
            # print(len(quat_table))
            # print(len(quat_table[0]))
            # print("Body: ",quat_table)
            table = pd.DataFrame(balance_table, columns=column_names)
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Balance Sheet Details (in Cr)</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Balance_Sheet")
        except Exception as e:
            # print(e)
            pass
        # Ratio results
        ratio_table = ""
        try:
            # print("Hello0")
            top_thead = browser.find_element(By.ID, "ratios")
            top2_head = top_thead.find_element(By.CLASS_NAME, "responsive-text-nowrap")
            t_head = top2_head.find_element(By.TAG_NAME, "thead")
            # director = pro_div.find_element(By.TAG_NAME, "tbody")
            # print("Hello1")
            child_elements_t_head = t_head.find_elements(By.TAG_NAME, "th")
            # print("Hello2")
            column_names = []
            for i in child_elements_t_head:
                column_names.append(i.text)
            # print("Head",column_names)
            t_body = top2_head.find_element(By.TAG_NAME, "tbody")
            # print("Hello3")
            child_elements_t_body = t_body.find_elements(By.TAG_NAME, "tr")
            # print("Hello4")
            ratio_table = []
            for i in child_elements_t_body:
                childs = i.find_elements(By.TAG_NAME, "td")
                l_row = []
                for j in childs:
                    # l_row.append(j.text)
                    l_row.append(j.text.replace("&nbps", "").replace("+", ""))
                ratio_table.append(l_row)
            # print(len(quat_table))
            # print(len(quat_table[0]))
            # print("Body: ",quat_table)
            table = pd.DataFrame(ratio_table, columns=column_names)
            table.index = range(1, len(table) + 1)
            st.markdown('<h2>Ratios Details (in Cr)</h2>', unsafe_allow_html=True)
            # st.markdown(f'<div class="output-box">{content_dir}</div>', unsafe_allow_html=True)
            st.dataframe(table, use_container_width=True)
            save_dataframe_to_duckdb(table, "Ratios")
        except Exception as e:
            # print(e)
            pass
        except Exception:
            pass
        if content == "" and basic_d == "" and pro_con_table == "" and PL_table == "" and ratio_table == "" and balance_table == "" and quat_table=="":
            st.markdown('<h2>No Data Found. Try Some other company</h2>', unsafe_allow_html=True)
    except Exception:
        browser.quit()
    finally:
        if flag==1:
            return option_company
