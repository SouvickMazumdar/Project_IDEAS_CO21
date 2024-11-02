# User Manual

## Overview
This web application allows users to easily retrieve and display business data from Screener, Tofler and Zauba, two business information websites. The data is displayed on a user-friendly interface built with Streamlit. 

---

## Installation Guide

1. **Install Python**: Ensure Python 3.7 or higher is installed on your machine.

2. **Install Required Libraries**:
   - Open a terminal or command prompt.
   - Install the necessary libraries by running:
     ```
     pip install selenium streamlit pandas webdriver-manager
     ```

3. **Download ChromeDriver**:
   - Download the correct version of ChromeDriver from the [ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads).
   - Make sure it matches your installed Chrome version.
   - Place the `chromedriver` executable in a known location or add it to your system path.

4. **Set Up Project Files**:
   - Clone the repository or download the project files and place `zauba.py`, `tofler.py`, `screener.py` and `WebScrapingProject.py` in the same directory.

---

## Using the Application

1. **Launch the Application**:
   - In the terminal, navigate to the project directory.
   - Start the application by entering:
     ```
     streamlit run WebScrapingProject.py
     ```
   - Open the provided URL in a web browser (usually `http://localhost:8501`).

2. **Select Data Source**:
   - From the dropdown menu, choose either "Screener","Tofler","Zauba" as the data source.

3. **Start Data Scraping**:
   - Click the "Fetch Data" button to start scraping.
   - The application will automatically scrape data from the selected website and display it in a table.

4. **View and Analyze Data**:
   - Use the interactive table to sort, filter, and examine the data.

---

## Troubleshooting

- **ChromeDriver Issues**: Ensure that ChromeDriver is compatible with your installed Chrome version.
- **Scraping Errors**: Website structure changes can disrupt scraping. Contact support if errors occur.
- **CAPTCHA**: Some websites may display CAPTCHA challenges, which require manual input.
