def check (prices, tip = 10):
    sum_ = sum(prices)
    total = sum_ * (100 - tip) / 100
    return total

print(check([100, 300, 500]))
print(check([100, 300, 500], 0))
print(check([100, 300, 500], 20))