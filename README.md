# E-Commerce Product Scraper

This project is a beginner-friendly web scraping script built with Python.
It extracts product information from an online store and exports the data into an Excel file.

The goal of this project is to demonstrate how web scraping can be used to collect structured data for business or research purposes.

## Features

* Scrapes product names
* Extracts product prices
* Collects product ratings
* Extracts product links
* Exports the data into an Excel file

## Technologies Used

* Python
* Requests
* BeautifulSoup
* Pandas
* OpenPyXL

## Installation

Clone the repository:

```
git clone https://github.com/ExcelsKennedy2/Ecommerce-Product-Scraper.git
```

Navigate to the project folder:

```
cd ecommerce-product-scraper
```

Install dependencies:

```
pip install -r requirements.txt
```

## Usage

Run the scraper:

```
python scraper.py
```

The script will scrape product data and generate:

```
products.xlsx
```

## Example Output

| Product      | Price  | Rating | Link         |
| ------------ | ------ | ------ | ------------ |
| Example Book | £51.77 | Three  | product link |

## Learning Goals

This project demonstrates:

* Sending HTTP requests
* Parsing HTML pages
* Extracting structured data
* Exporting data to Excel

## Disclaimer

This scraper is intended for educational purposes. Always respect website terms of service when scraping data.
