def total_price(price1 :float , price2 : float ) -> str:
    return f"Total Price {price1 + price2}"


sum = total_price(10,20.22)
sum = total_price('10','20.22')
print(sum)