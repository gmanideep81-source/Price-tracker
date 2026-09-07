# E-Commerce Product Price Tracker

A Python-based web scraping project that tracks the price of an e-commerce product and stores its price history.

## Features

* Scrapes product price using Selenium
* Uses explicit waits to load the price element
* Stores daily prices in a CSV file
* Compares the current price with the previous price
* Sends an email notification when the price decreases
* Generates a price history graph using Matplotlib
* Uses `.env` to keep email credentials separate from the source code

## Technologies Used

* Python
* Selenium
* Pandas
* Matplotlib
* python-dotenv
* SMTP

## Project Structure

```text
price-tracker/
│
├── scraper.py
├── output.csv
├── price_history.png
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/gmanideep81-source/Price-tracker/
cd price-tracker
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

```text
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

### 4. Run the scraper

```bash
python scraper.py
```

The current price will be stored in `output.csv`.

If the price is lower than the previous recorded price, an email notification will be sent.

A price history graph will also be generated as:

```text
price_history.png
```

## Author

GRV MANIDEEP
