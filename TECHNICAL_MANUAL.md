# Technical Manual

## Project Overview

This project is a web-based data extraction and display tool built with **Streamlit** and **Selenium**. It scrapes data from two business information websites, Tofler, Screener and Zauba, and displays the retrieved information on a Streamlit interface.

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
