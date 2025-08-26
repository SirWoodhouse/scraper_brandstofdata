# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from datetime import datetime

# Function to download csv
def download_csv():
    # Selecting browser. Firefox works better than Safari
    browser_driver = webdriver.Firefox()
    # Navigate to website
    browser_driver.get("https://brandstofdata.nl/brandstof/benzine")
    # Find and click menu
    open_menu = browser_driver.find_element(By.CSS_SELECTOR,
                                            ".apexcharts-menu-icon")
    open_menu.click()
    # Download .csv file
    download_csv_file = browser_driver.find_element(By.CSS_SELECTOR,
                                                        ".exportCSV")
    download_csv_file.click()

# Function to process csv
def process_csv():
    # Use pandas to open and read downloaded csv file
    df_main = pd.read_csv("~/Downloads/mainChart.csv")
    df_main.rename(columns={"category": "Datum", "benzine prijs":
        "Gem. benzineprijs"}, inplace = True)
    # Replace the '.' with ',' in column 'Datum' to make further processing
    # easier.
    df_main["Gem. benzineprijs"] = (df_main["Gem. benzineprijs"].astype(
        str).str.replace
                                                    (".",",",regex=False))
    # Remove the first 4 characters in column 'Datum'. These represent the
    # day of the month and a space. This is irrelevant for further analysis.
    df_main["Datum"] = df_main["Datum"].str.slice(start=4)
    # Convert column 'Datum' from string to datetime
    df_main['Datum'] = pd.to_datetime(df_main.Datum)
    # Add a column with the month number
    df_main['Maand'] = df_main['Datum'].dt.month

    # Create unique filename
    i = 0
    while os.path.exists(f'benzineprijzen_{datetime.now():%Y%m%d_%H%M}.csv'):
        i += 1

    # print df to new csv file
    df_main.to_csv(f'benzineprijzen_{datetime.now():%Y%m%d_%H%M}.csv',
                                                                index=False)
    print(f"CSV processed and saved as benzineprijzen_{datetime.now()
                                                        :%Y%m%d_%H%M}.csv")

# Initializer
if __name__ == "__main__":
    # download_csv()
    process_csv()
