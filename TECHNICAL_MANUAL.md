# Technical Manual

## Project Overview

This project is a web-based data extraction and display tool built with **Streamlit** and **Selenium**. It scrapes data from three business information websites, Tofler, Screener and Zauba, and displays the retrieved information on a Streamlit interface.

---

## System Requirements

- **Python**: Version 3.7 or higher.
- **Chrome Browser**: Latest version for Selenium compatibility.
- **ChromeDriver**: Matching version to Chrome.

---

## Architecture

1. **Streamlit Front-End**:
   - `WebScrapingProject.py` runs the Streamlit application, creating a user-friendly interface to select the data source and initiate scraping.

2. **Selenium-Based Scraping Modules**:
   -  **`tofler.py`**, **`screener.py`** and **`zauba.py`** contain functions for scraping business data from Zauba and Tofler, respectively.
   - Each module opens the target website, retrieves the required elements using XPath/CSS selectors, and stores the data in a structured format (list or pandas DataFrame).

3. **Data Display**:
   - Data retrieved by `tofler.py`,`screener.py` and `zauba.py` is presented in a Streamlit table, enabling sorting and basic data analysis.

---

## Code Details

### `tofler.py`,`screener.py` and `zauba.py`

- **Functions**:
  - Each file defines a main scraping function that opens the respective website, locates elements, extracts data, and stores it in a DataFrame.
- **Libraries Used**:
  - `selenium` for browser automation.
  - `pandas` for data structuring.
- **Error Handling**:
  - Custom error handling for network or structural changes in the target website is included.

### `WebScrapingProject.py`

- **Streamlit Setup**:
  - Sets up UI components like dropdowns and buttons.
  - Imports data retrieval functions from `tofler.py`,`screener.py` and `zauba.py`.
- **Functions**:
  - The script includes functions to handle UI events, such as data source selection and data display.
- **Data Table Display**:
  - Streamlit’s `dataframe` component displays data in a table, with options for sorting and filtering.

---
## Database:

1. **Tool Used: `Duckdb`**
DuckDB is an in-process **SQL OLAP** database for high-performance analytics directly on local files. Its lightweight architecture makes it ideal for real-time data processing and analytics without needing a server. It supports efficient columnar storage, which accelerates query execution on large datasets. With built-in support for **Parquet** and **CSV**, DuckDB seamlessly integrates with data science workflows, especially in Python and R environments. It offers ACID compliance for reliable transactions, and its SQL-based interface allows for easy adoption by users familiar with SQL databases. DuckDB’s low resource footprint makes it perfect for embedded analytics and local data exploration.

2. **Usage in our project**
   To address the challenges of slow data scraping and unreliable results due to dynamic websites, we implemented a solution that caches data locally to reduce user wait times. For efficient storage, we chose DuckDB, a high-performance database optimized for analytical workloads.
   
Each scraping session in the repository's **Backend** folder automatically creates a unique folder using the `os` library for each company. This folder contains the scraped data in several formats: **overview.txt**, **source_data.txt**, and **<company_name>.duckdb**. The `.duckdb` file stores all dataframes fetched from the website, making it easy to query and retrieve specific data quickly.

With DuckDB’s speed, retrieving data from these folders is fast, significantly enhancing the user experience. The Python script 
**fetchTofler.py** handles the retrieval process from these company folders. The entire process, from folder creation to data updates, is automated. Each fetch refreshes the data with the latest information, ensuring users have the most accurate results. Additionally, a
fetchlist file logs each new company added, keeping track of all records efficiently.

This approach minimizes user wait times, providing quick, reliable access to data and ensuring users get timely and accurate results.

--- 

## Maintenance and Updates

1. **ChromeDriver Compatibility**:
   - Update `chromedriver` whenever the Chrome browser updates.
   - Check compatibility if scraping errors occur.

2. **Website Structure**:
   - Monitor Tofler, Screener and Zauba for structure updates; adjust selectors as needed.
   - Review the website's HTML structure and modify the selectors if scraping functions encounter errors.

3. **Feature Expansion**:
   - Add functionality to scrape multiple pages.
   - Implement caching to avoid redundant data fetching.

---

## Error Handling and Debugging

- **Network Errors**: Check internet connectivity and site accessibility.
- **Element Not Found**: Ensure selectors are up-to-date with site structure.
- **CAPTCHA**: Websites with CAPTCHA may require manual intervention or CAPTCHA-solving services.

---

## Security and Legal Considerations

- **Data Use**: Ensure compliance with the terms of service of Tofler, Screener and Zauba.
- **Ethics**: Use appropriate timing delays to avoid being blocked or flagged by websites.
