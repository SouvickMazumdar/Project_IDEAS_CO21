import streamlit as st
import duckdb
import os

def fetch_tofler(option_company):
    try:
        os.chdir(f"Backend/{option_company}")
        conn = duckdb.connect(f'{option_company}.duckdb')
        try:
            with open("Extract_date.txt", 'r') as file:
                content=file.read()
            st.write(f"<h2>Last Update Done on - {content}</h2>", unsafe_allow_html=True)
        except Exception:
            pass
        # OVERVIEW part
        try:
            with open("overview.txt", 'r') as file:
                content=file.read()
            if content is None or content =="":
                raise
            st.write(f"<h2>Overview of Company - {option_company}</h2>", unsafe_allow_html=True)
            st.write(content)
        except Exception:
            pass

        # Registration Details
        try:
            stored_data = conn.execute("SELECT * FROM Registration_details").fetchdf()
            if stored_data is None or content =="":
                raise
            stored_data.index = range(1, len(stored_data) + 1)
            st.markdown('<h2>Registration Details</h2>', unsafe_allow_html=True)
            st.dataframe(stored_data, use_container_width=True)
        except Exception:
            pass

        # Directors
        try:
            stored_data = conn.execute("SELECT * FROM Directors").fetchdf()
            if stored_data is None or content =="":
                raise
            stored_data.index = range(1, len(stored_data) + 1)
            st.markdown('<h2>Directors</h2>', unsafe_allow_html=True)
            st.dataframe(stored_data, use_container_width=True)
        except Exception:
            pass


        # Charges on asset
        try:
            stored_data = conn.execute("SELECT * FROM Asset").fetchdf()
            if stored_data is None or content =="":
                raise
            stored_data.index = range(1, len(stored_data) + 1)
            st.markdown('<h2>Charges on Assets</h2>', unsafe_allow_html=True)
            st.dataframe(stored_data, use_container_width=True)
        except Exception:
            pass

        # Key Metrics
        try:
            stored_data = conn.execute("SELECT * FROM Metrics").fetchdf()
            if stored_data is None or content =="":
                raise
            stored_data.index = range(1, len(stored_data) + 1)
            st.markdown('<h2>Key Metrics</h2>', unsafe_allow_html=True)
            st.dataframe(stored_data, use_container_width=True)
        except Exception:
            pass

        # Financial Part
        try:
            stored_data = conn.execute("SELECT * FROM Finance").fetchdf()
            # print(stored_data)
            if stored_data is None or content =="":
                raise
            stored_data.index = range(1, len(stored_data) + 1)
            st.markdown('<h2>Financial Highlights</h2>', unsafe_allow_html=True)
            st.dataframe(stored_data, use_container_width=True)
        except Exception:
            pass
    except Exception:
        st.markdown('<h2>No Data Found. Try Finding the latest information.</h2>', unsafe_allow_html=True)