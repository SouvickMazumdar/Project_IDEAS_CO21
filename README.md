# Project_IDEAS_CO21
# Web Scraping and Data Display Application

This project is a web-based application built using **Streamlit** and **Selenium**. It enables users to scrape and display business data from [Tofler](https://www.tofler.in/) and [Zauba](https://www.zaubacorp.com/) on an interactive web interface. The application leverages **Selenium** to automate data extraction from these websites and displays the results on a **Streamlit** dashboard.

---

## Features

- **Automated Data Scraping**: Extracts data from Tofler and Zauba automatically using Selenium-based scripts.
- **Interactive Web Interface**: Users can interact with the web application to view or refresh data from each website.
- **Data Display**: Extracted data is displayed in a tabular format for easy viewing and analysis.
- **Error Handling and Logging**: Logs scraping errors and other issues to ensure smooth performance.

## Project Structure

The project contains three main Python files, each serving a specific purpose:

- **`zauba.py`**: Handles data scraping from Zauba using Selenium. The script extracts relevant business information, formats it, and saves it in a structured format.
- **`tofler.py`**: Similar to `zauba.py`, this file handles scraping data from Tofler. The data fields and structure may vary based on the website layout.
- **`WebScrapingProject.py`**: The main Streamlit application file that serves as the front-end interface. It imports data from `zauba.py` and `tofler.py` and presents it in a web-based dashboard.

---

## Prerequisites

### Software Requirements

- **Python**: Version 3.7 or higher
- **Google Chrome**: Latest version for compatibility with Selenium
- **ChromeDriver**: Ensure that the version of ChromeDriver matches your installed version of Chrome.

### Library Requirements

Install the necessary Python libraries using the following commands:

```bash
pip install selenium
pip install streamlit
pip install pandas
```