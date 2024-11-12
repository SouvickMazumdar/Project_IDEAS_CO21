# Project_IDEAS_CO21
# Web Scraping and Data Display Application

This project is a web-based application built using **Streamlit** and **Selenium**. It enables users to scrape and display business data from [Tofler](https://www.tofler.in/), [Screener](https://www.screener.in/) and [Zauba](https://www.zaubacorp.com/) on an interactive web interface. The application leverages **Selenium** to automate data extraction from these websites and displays the results on a **Streamlit** dashboard.

---

## Features

- **Automated Data Scraping**: Extracts data from Tofler, Screener and Zauba automatically using Selenium-based scripts.
- **Interactive Web Interface**: Users can interact with the web application to view or refresh data from each website.
- **Data Display**: Extracted data is displayed in a tabular format for easy viewing and analysis.
- **Error Handling and Logging**: Logs scraping errors and other issues to ensure smooth performance.

## Project Structure

The project contains three main Python files, each serving a specific purpose:

- **`screener.py`**: Handles data scraping from Screener using Selenium. The script extracts relevant business information, formats it, and saves it in a structured format.
- **`zauba.py`**: Handles data scraping from Zauba using Selenium. The script extracts relevant business information, formats it, and saves it in a structured format.
- **`tofler.py`**: Handles data scraping from Tofler using Selenium. The script extracts relevant business information, formats it, and saves it in a structured format. The data fields and structure may vary based on the website layout.
- **`WebScrapingProject.py`**: The main Streamlit application file that serves as the front-end interface. It imports data from `screener.py`, `zauba.py` and `tofler.py` and presents it in a web-based dashboard.

---

## Prerequisites

### Software Requirements

- **Python**: Version 3.7 or higher
- **Google Chrome**: Latest version for compatibility with Selenium

### Library Requirements

Install the necessary Python libraries using the following commands:

```bash
pip install -r .\requirement.txt
```
---
## Installation and Setup

1. **Clone the Repository**: Download or clone this repository to your local machine.

2. **Organize Files**:
   - Ensure that `screener.py`, `tofler.py`, `zauba.py`,  and `WebScrapingProject.py` are located in the same project directory.

3. **Install required Librares**: Go inside the cloned repo and run the below command in command prompt
```bash
pip install -r .\requirement.txt
```
---

---

## Running the Application

1. **Start Streamlit**: Run the Streamlit application from the terminal in the project directory using the command 
```bash
streamlit run WebScrapingProject.py
```

2. **Open the Application**: Once Streamlit starts, it will provide a local URL (usually `http://localhost:8501`) where the application can be accessed. Open this URL in a web browser.

3. **Select Data Source and Start Scraping**:
   - Choose between Screener, Zauba and Tofler as the data source on the main interface.
   - Click the provided button to start the scraping process. Data will be displayed in a table format once fetched.

4. **View Data**:
   - The scraped data is displayed directly in the Streamlit dashboard.
   - Use Streamlit’s built-in options to filter, sort, or export data if necessary.

---

## Code Overview

### `screener.py`, `zauba.py` and `tofler.py`

These files contain the Selenium-based scraping functions for Screener, Zauba and Tofler. Each script performs the following actions:
- **Open the Target Website**: Navigates to the specified page on Screener, Zauba or Tofler.
- **Extract Data**: Locates and extracts relevant business data using Selenium selectors.
- **Store Data**: Stores the data in a structured format (e.g., a list or pandas DataFrame) for easy access.

**Note**: Custom selectors (XPath, CSS selectors) are used to locate elements on the target websites, and minor modifications to these selectors may be required if website layouts change.

### `WebScrapingProject.py`

This file serves as the main entry point for the Streamlit application. It includes:
- **Import Statements**: Imports `screener.py`, `zauba.py` and `tofler.py` to access scraping functions.
- **Streamlit Interface**: Sets up the user interface with dropdown options for selecting the data source, buttons to initiate scraping, and a data table to display results.
- **Error Handling**: Provides basic error handling to catch issues like network errors or site structure changes.

---

## Troubleshooting

- **ChromeDriver Issues**:
  - Ensure that your ChromeDriver version matches your installed version of Chrome.
  - If the `chromedriver` executable is not in your system path, specify its location explicitly in `zauba.py` and `tofler.py`.

- **Network or Website Issues**:
  - If a website blocks the scraping requests, try adding delays between actions in the Selenium script.
  - Consider using a VPN or proxy if access is restricted, but ensure this aligns with website policies.

- **Element Selection Errors**:
  - Websites may change their structure or class names periodically. If scraping fails, inspect the site’s HTML structure and update the selectors in the scripts.

- **CAPTCHA Handling**:
  - If the target website uses CAPTCHA, manual intervention may be required. Alternatively, consider using services that assist in CAPTCHA handling if necessary.

---

## Future Enhancements

- **Data Caching**: Implement caching to reduce redundant scraping and load times.
- **Multi-Page Scraping**: Add functionality to scrape data across multiple pages for comprehensive data retrieval.
- **Data Export**: Enable data export to CSV or Excel for external analysis.

---

## License

This project is licensed under the MIT License. Please see the `LICENSE` file for more details.
