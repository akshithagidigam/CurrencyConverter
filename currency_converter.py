import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://v6.exchangerate-api.com/v6/APIKEY/latest/{from_currency.upper()}"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data['result'] == 'success':
            rate = data['conversion_rates'].get(to_currency.upper())

            if rate is not None:
                converted_amount = round(amount * rate, 2)
                print(f"\n{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}")
                print(f"(Exchange rate: 1 {from_currency.upper()} = {rate} {to_currency.upper()})")
            else:
                print(f"Error: '{to_currency.upper()}' is not a valid target currency.")
        else:
            print(f"API Error: {data.get('error-type', 'Unknown error')}")
    except Exception as e:
        print("Exception occurred:", e)

def main():
    print("Currency Converter CLI Tool")
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("From currency (e.g., USD): ").strip()
        to_currency = input("To currency (e.g., INR): ").strip()
        
        convert_currency(amount, from_currency, to_currency)
    except ValueError:
        print("Invalid input. Please enter a numeric amount.")

if __name__ == "__main__":
    main()
