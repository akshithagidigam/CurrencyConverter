# Currency Converter - Real-Time API Project

##  Project Overview

This is a simple **command-line Currency Converter** built using Python.  
It takes an amount, source currency, and target currency as input and converts the amount using real-time exchange rates from the **ExchangeRate API**.

---

##  Features

- Convert any amount from one currency to another
- Uses **real-time data** via API
- Error handling for invalid currency codes or network issues
- Easy-to-use command-line interface

---

##  Technologies Used

- **Python 3**
- **requests** library
- **ExchangeRate-API** (https://www.exchangerate-api.com/)

---

##  How It Works

1. The user is prompted to enter:
   - Amount to convert
   - Source currency code (like `USD`)
   - Target currency code (like `INR`)
2. The program sends a request to the ExchangeRate API.
3. It fetches the latest exchange rates for the given base currency.
4. It calculates and displays the converted amount along with the exchange rate.

---

## Code Example

```python
import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/{from_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            rate = data['conversion_rates'].get(to_currency.upper())
            if rate is not None:
                converted_amount = round(amount * rate, 2)
                print(f"\n{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}")
            else:
                print("Invalid target currency.")
        else:
            print("API error:", data.get('error-type', 'Unknown error'))

    except Exception as e:
        print("An error occurred:", e)

def main():
    print("Currency Converter CLI Tool")
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("From currency (e.g., USD): ").strip()
        to_currency = input("To currency (e.g., INR): ").strip()
        
        convert_currency(amount, from_currency, to_currency)
    except ValueError:
        print("Please enter a valid numeric amount.")

if __name__ == "__main__":
    main()
```

---

## How to Run & Sample Output

1. Clone the repository or download the `.py` file.
2. Make sure you have Python installed.
3. Install the `requests` module if not already installed:

   ```bash
   pip install requests
Run the script using:
python your_script_name.py
---
## Sample Output

Currency Converter CLI Tool
Enter the amount: 100
From currency (e.g., USD): USD
To currency (e.g., INR): INR

100.0 USD = 8330.0 INR

