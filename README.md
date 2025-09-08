# Scraper for brandstofdata.nl

This project was created to avoid having to manually download and parse data 
from the website brandstofdata.nl.

Note that this script is written on and tested for macOS. You might need to 
adapt the code when trying to run it on a Windows- or Linux-machine. The language used for the output files is Dutch.

## Why scrape this website?

My mother-in-law watches the kids every week and has 
to travel by car for approximately 150km. My girlfriend and I wanted to 
compensate her for the petrol cost. To do this fair and square for everyone 
I figured we needed the average cost of petrol each month. Brandstofdata.nl 
collects the average petrol price across the Netherlands and returns an 
average value.

### Easy/easier parsing

Instead of manually downloading the csv file every couple of months or so, I 
wanted to automate this and make life a bit easier. And of course, as a beginner 
programmer, this is a nice little project to get better at Python. The 
script makes use of Selenium for the scraping part.

## How to run the script

Easy! Make sure you have Firefox installed and edit the download folder 
(currently: "~/Downloads/mainChart.csv") if necessary. Run the script via your 
preferred IDE or through the terminal.

### Output

When run the script outputs two csv files which can be used. One file is 
just a copy of the data on brandstofdata.nl, the other shows the average 
petrol price per month.

## License

This project is licensed under the GNU General Public License. See the 
LICENSE.txt file for more information.

## Want to contribute?

Please feel free to fork the project. I like to learn so it 
would be much appreciated if you share your edits on this project.