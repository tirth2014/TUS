prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3}

stocks = {
    "banana": 10,
    "apple": 8,
    "orange": 0,
    "pear": 5
}

# for i in prices.keys():
#     print(i)
#     print("price: {} ".format(prices.get(i)))
#     print("stock: {}".format(stocks.get(i)))


total = 0

for i in prices.keys():
    x = prices.get(i)*stocks.get(i)
    print(x)
    total += x

print("total money we would make is: ", total)