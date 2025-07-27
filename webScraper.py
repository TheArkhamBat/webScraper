from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv

# initialize a Chrome web driver instance
driver = webdriver.Chrome(service=Service())

# the URL of the target page
url = "https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.home_new_user_first_screen_fy23_pc_search_bar.keydown__Enter&tab=all&SearchText=laptop"

# connect to the target page
driver.get(url)

# where to store the scraped data
products = []

# select all product elements on the page
product_elements = driver.find_elements(By.CSS_SELECTOR, ".m-gallery-product-item-v2")

# iterate over the product nodes and scrape data from them
for product_element in product_elements:
    # extract the product details
    img_element = product_element.find_element(By.CSS_SELECTOR,".search-card-e-slider__img")
    img = img_element.get_attribute("src")

    description_element = product_element.find_element(By.CSS_SELECTOR,".search-card-e-title")
    description = description_element.text.strip()

    price_element = product_element.find_element(By.CSS_SELECTOR,".search-card-e-price-main")
    price = price_element.text.strip()

    company_element = product_element.find_element(By.CSS_SELECTOR,".search-card-e-company")
    company = company_element.text.strip()

    # create a product dictionary with the
    # scraped data
    product = {
        "img": img,
        "description": description,
        "price": price,
        "company": company
    }

    # add the product data to the array
    products.append(product)

# define the output CSV file name
csv_file_name = "products.csv"

# open the file in write mode and create a CSV writer
with open(csv_file_name, mode="w", newline="", encoding="utf-8") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=["img", "description", "price", "company"])

    # write the header row
    writer.writeheader()

    # write product data rows
    for product in products:
        writer.writerow(product)

# close the browser
driver.quit()