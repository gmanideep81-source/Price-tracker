# 🛒 E-Commerce Product Price Tracker

A Python-based web scraping project that automatically tracks the price of an e-commerce product, stores its price history, generates a price graph, and sends an email notification when the price decreases.

## 🚀 Features

* 🔍 Scrapes product prices using Selenium
* ⏳ Uses explicit waits to load the price element
* 💾 Stores daily price data in a CSV file
* 📊 Generates a price history graph using Matplotlib
* 📉 Compares the current price with the previous price
* 📧 Sends an email notification when the price decreases
* 🔐 Uses `.env` to keep email credentials separate from source code
* ⚙️ Runs automatically using GitHub Actions
* 🔄 Automatically commits updated price history back to the repository

## 🛠️ Technologies Used

* **Python**
* **Selenium** – Web scraping
* **Pandas** – CSV and data handling
* **Matplotlib** – Price history visualization
* **python-dotenv** – Environment variable management
* **SMTP** – Email notifications
* **Git & GitHub** – Version control
* **GitHub Actions** – Automation

## 📁 Project Structure

```text
Price-tracker/
│
├── scraper.py
├── output.csv
├── price_history.png
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
└── .github/
    └── workflows/
        └── price_tracker.yml
```

## ⚙️ How It Works

The project follows this workflow:

```text
E-Commerce Product
        ↓
     Selenium
        ↓
   Get Current Price
        ↓
 Read Previous Price
        ↓
 Compare Prices
        ↓
 Price Decreased?
     ↙       ↘
   YES        NO
    ↓          ↓
Send Email   Continue
    ↓
Save Price to CSV
        ↓
Generate Price Graph
        ↓
GitHub Actions
        ↓
Commit Updated Files
```

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/gmanideep81-source/Price-tracker/
cd Price-tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file

Create a file named `.env` in the project directory:

```text
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
```

> ⚠️ Never upload your `.env` file or email password to GitHub.

### 4. Run the scraper

```bash
python scraper.py
```

The scraper will:

1. Open the product page.
2. Extract the current price.
3. Read the previous price from `output.csv`.
4. Compare the prices.
5. Send an email if the price decreased.
6. Save the new price to `output.csv`.
7. Generate `price_history.png`.

## 📊 Price History

The project stores the price history in:

```text
output.csv
```

Example:

```text
date,price
2026-09-05,134999
2026-09-06,132999
2026-09-07,129999
```

The project also generates a visual price history:

```text
price_history.png
```

## 🤖 GitHub Actions Automation

The project uses **GitHub Actions** to automatically run the scraper every day.

The workflow is configured to run at:

```text
10:00 AM IST
```

It can also be triggered manually using the **Run workflow** button in GitHub Actions.

### Automated Process

```text
GitHub Actions
      ↓
Checkout Repository
      ↓
Setup Python
      ↓
Setup Chrome
      ↓
Install Dependencies
      ↓
Run scraper.py
      ↓
Update output.csv
      ↓
Update price_history.png
      ↓
Commit Changes
      ↓
Push Changes to GitHub
```

This allows the price history to persist between automated runs.

## 🔐 GitHub Secrets

Email credentials are stored securely using GitHub Secrets.

The following secrets are required:

```text
EMAIL
PASSWORD
```

They are accessed in GitHub Actions through environment variables instead of storing credentials directly in the source code.

## 📧 Price Drop Notification

When the current price is lower than the previous recorded price, the application sends an email notification.

Example:

```text
Hurry up!!

The price is changed from ₹134999 to ₹129999.
```

## 📦 Requirements

The required Python packages are listed in `requirements.txt`:

```text
selenium
pandas
matplotlib
python-dotenv
```



## 👨‍💻 Author

**GRV MANIDEEP**

Computer Science Engineering Student
