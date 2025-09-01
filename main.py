# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from datetime import datetime

# Function to download csv from brandstofdata.nl using selenium
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
    # Use pandas to open and read downloaded csv file. If you rerun this
    # script after a while, make sure that the previous downloaded file
    # 'mainchart.csv' is removed from your downloads beforehand.
    df_main = pd.read_csv("~/Downloads/mainChart.csv")
    df_main.rename(columns={"category": "Datum", "benzine prijs":
        "Benzineprijs"}, inplace = True)

    # Remove the first 4 characters in column 'Datum'. These represent the
    # day of the month and a space. This is irrelevant for further analysis.
    df_main["Datum"] = df_main["Datum"].str.slice(start=4)
    # Convert column 'Datum' from string to datetime
    df_main["Datum"] = pd.to_datetime(df_main.Datum)
    # Add a column with the month number
    df_main["Maand"] = df_main["Datum"].dt.month
    # Check result
    print(df_main)

    # Create a second dataframe with the average petrol price per month
    df_average = (df_main.groupby(["Maand"])["Benzineprijs"].
                  mean().
                  round(2).
                  reset_index())
    df_average["Maand"] = pd.to_datetime(df_average['Maand'],
                                                format='%m').dt.month_name(
                                                locale="nl_NL")
    # Check result
    print(df_average)

    # Create unique filenames for each times the script is run for both
    # files to prevent overwriting. Can be commented out if preferred.
    a = 0
    while os.path.exists(f"Benzineprijzen_"f"{datetime.now():%Y%m%d_%H%M}.csv"):
        a += 1

    b = 0
    while os.path.exists(f"Prijs per maand_{datetime.now():%Y%m%d_%H%M}.csv"):
        b += 1

    # Print both dataframes to csv files
    df_main.to_csv(f"Benzineprijzen_{datetime.now():%Y%m%d_%H%M}.csv",
                                                                index=False)

    df_average.to_csv(f"Prijs per maand_{datetime.now():%Y%m%d_%H%M}.csv",
                                                                index=False)

    print(f"CSVs processed and saved!")

# Initializer
# Choose whether to run both parts of the script or just one of the two
if __name__ == "__main__":
    download_csv()
    process_csv()
