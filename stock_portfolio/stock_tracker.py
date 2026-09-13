stock_price={
    "APL":180,
    "TSLA":220,
    "GOOGLE":451,
    "AMAZON":123,
    "MSFT":143
    
}
# stock_name=input("enter a stock name: ").upper()
# quantity=int(input("enter a quantity: "))

# price=stock_price[stock_name]
# investement=price*quantity

total_investement=0

portfolio = []

while True:
    stock_name=input("enter the stock name (or 'done' to finish):").upper()
    if stock_name=="DONE":
        break

    if stock_name not in stock_price:
        print("\nstock is not available")
        continue
    try:
        quantity=int(input("enter the quantity: "))

        if quantity <=0:
            print("quantity must be greater than zero")
            continue

    except ValueError as e:
        print("please enter a valid number")

        continue

    price=stock_price[stock_name]
    investement=price*quantity
    total_investement+=investement

    portfolio.append((stock_name,quantity,price,investement))

    print("\nstock: ", stock_name)
    print("price_per_share: ", price)
    print("quantity: ",quantity)
    print("total_investement: ", investement)

print("\n total_investement: ", total_investement)

save=input("do you want to save the portfolioo: ").lower()
if save=="yes":
    with open("portfolio.txt","w") as file:
        file.write("stock portfolio\n")
        file.write("----------------\n")

        for stock, quantity,price,investement in portfolio:
            file.write(f"{stock}- quantity: {quantity} - price {price} - investement: {investement}\n")

        file.write(f"\ntotal investsment : {total_investement}\n")

    print("portfolio saved successfully!")

print("thank you for approaching our stock_tracker portfollio.........")