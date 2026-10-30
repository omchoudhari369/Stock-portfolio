# STOCK PORTFOLIO TRACKER

# Sample stock prices (NOT live market prices)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 420
}

# Dictionary to store user's portfolio
portfolio = {}

print("================================")
print("     STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for ticker, price in stock_prices.items():
    print(f"{ticker}: ${price} per share")

# Take stock details from the user
while True:
    ticker = input("\nEnter stock ticker (or 'done' to finish): ").upper().strip()

    if ticker == "DONE":
        break

    if ticker not in stock_prices:
        print("Invalid ticker! Please choose an available stock.")
        continue

    try:
        quantity = int(input("Enter number of shares: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Invalid quantity! Please enter a whole number.")
        continue

    # Add shares to the portfolio
    if ticker in portfolio:
        portfolio[ticker] += quantity
    else:
        portfolio[ticker] = quantity

    print(f"Added {quantity} shares of {ticker}!")

# Calculate portfolio value
total_value = 0

print("\n========== YOUR PORTFOLIO ==========")
print(f"{'Ticker':<10}{'Shares':<10}{'Price':<12}{'Value':<12}")
print("-" * 44)

for ticker, quantity in portfolio.items():
    price = stock_prices[ticker]
    value = quantity * price
    total_value += value

    print(f"{ticker:<10}{quantity:<10}${price:<11.2f}${value:<11.2f}")

print("-" * 44)
print(f"TOTAL PORTFOLIO VALUE: ${total_value:.2f}")

# Optional: Save portfolio to a text file
if portfolio:
    save = input("\nSave portfolio to a text file? (yes/no): ").lower().strip()

    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("STOCK PORTFOLIO REPORT\n")
            file.write("======================\n\n")

            for ticker, quantity in portfolio.items():
                price = stock_prices[ticker]
                value = quantity * price

                file.write(
                    f"{ticker}: {quantity} shares x "
                    f"${price:.2f} = ${value:.2f}\n"
                )

            file.write(f"\nTotal Portfolio Value: ${total_value:.2f}")

        print("Portfolio saved successfully to portfolio.txt!")

print("\nThank you for using Stock Portfolio Tracker!")