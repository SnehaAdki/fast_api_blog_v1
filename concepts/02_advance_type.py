#before python 3.9 use the typing module 

from typing import List, Tuple ,Dict


price : List[int] = [12,13,14]
price_tuple: Tuple[int,int,int] = (1,2,3)
price_dict: Dict[str,int] = {
    "itm1" : 25,
    "itm2" : 29,
    "itm3" : 30,
}

print("Before python3.9")
print(price)
print(price_tuple)
print(price_dict)

print("------------")

price : list[int] = [12,13,14]
price_tuple: tuple[int,int,int] = (1,2,3)
price_dict: dict[str,int] = {
    "itm1" : 25,
    "itm2" : 29,
    "itm3" : 30,
}

print("After python3.9")
print(price)
print(price_tuple)
print(price_dict)

print("With union--------------")
price_opt1 : list[Union[int , float]] = [12,13.100,14]
# or 
price_opt2: list[int | float] = [12, 13.1, 14] # by using 3.10

print(price_opt1)
print(price_opt2)