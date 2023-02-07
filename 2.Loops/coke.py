valid = [25, 10, 5]
price = 50

price_a = 50

coin_total = 0

print("Amount Due: 50")
while True:
    coin_inserted = int(input("Insert coin: "))

    if coin_inserted in valid:
        coin_total += coin_inserted
        price_a -= coin_inserted

    if coin_total >= price:
        print(f"Change Owned {coin_total - price}")
        break

    else:
        print(f"Amount Due: {price_a}")


