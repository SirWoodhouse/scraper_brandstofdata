# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import os
from datetime import datetime

# Function to download csv from brandstofdata.nl using Selenium
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
    df_average["Maand"] = pd.to_datetime(df_average["Maand"],
                                                format='%m').dt.month_name(
                                                locale="nl_NL")
    # Check result
    print(df_average)

    # Return the dataframes for use in a second function
    return df_main, df_average

# Function to save the returned values in the function above to a csv file.
# The function is written in such a way that the files get a unique name
# # each time the function is called.
def save_to_csv(df, prefix="output"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{prefix}_{timestamp}.csv"
    df.to_csv(filename, index=False)

# Initializer
# Choose whether to run all the functions in this script parts by
# commenting out the functions you don't need.
if __name__ == "__main__":
    download_csv()
    df_main, df_average = process_csv()
    save_to_csv(df_main, "Benzineprijzen")
    save_to_csv(df_average, "Prijs per maand")
