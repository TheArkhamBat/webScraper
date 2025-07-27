webScraper

This repository contains a Python web scraper built using Selenium. Currently, it is configured to scrape product information (image URL, description, price, and company) from Alibaba's product search results page for "laptop" and save it to a CSV file.

Features
Scrapes product details (image, description, price, company) from Alibaba.

Outputs the scraped data into a products.csv file.

Uses Selenium for browser automation, allowing it to handle dynamic content.

Setup and Installation
To get this scraper up and running on your local machine, follow these steps:

1. Prerequisites
Before you begin, ensure you have the following installed:

Python 3.x: Download from python.org.

Git: For cloning the repository. Download from git-scm.com.

Google Chrome Browser: The scraper uses ChromeDriver to control Chrome. Ensure you have a recent version installed.

ChromeDriver: This is crucial. The version of ChromeDriver must match your Chrome browser's major version.

Check your Chrome browser version by typing chrome://version/ in the address bar. Note the major version (e.g., 138).

Download the corresponding ChromeDriver from the official Chrome for Testing availability dashboard: https://googlechromelabs.github.io/chrome-for-testing/

Find the chromedriver for your Chrome version and linux64 (or your OS).

Unzip the downloaded file.

Move the chromedriver executable to a directory in your system's PATH (e.g., /usr/local/bin/) and make it executable:

# Assuming you are in the directory where you unzipped chromedriver-linux64.zip
cd chromedriver-linux64 # Move into the extracted folder
sudo mv chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver
# You can verify with: chromedriver --version

2. Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/TheArkhamBat/webScraper.git
cd webScraper

3. Create and Activate a Virtual Environment
It's highly recommended to use a virtual environment to manage project dependencies.

# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On Linux/macOS:
source .venv/bin/activate

# On Windows (Command Prompt):
# .venv\Scripts\activate.bat

# On Windows (PowerShell):
# .venv\Scripts\Activate.ps1

You should see (.venv) at the beginning of your terminal prompt, indicating the virtual environment is active.

4. Install Dependencies
With the virtual environment activated, install the required Python packages:

pip install selenium

Note: This project currently only explicitly lists selenium as a dependency. If other libraries are added in the future, you might use pip install -r requirements.txt if such a file is provided.

Usage
Once everything is set up, you can run the scraper:

# Make sure your virtual environment is activated
python scraper.py

The script will launch a Chrome browser, navigate to the specified Alibaba search page, scrape the product data, and save it to a file named products.csv in the same directory as the script.

Deactivating the Virtual Environment
When you're finished working on the project, you can deactivate the virtual environment:

deactivate
