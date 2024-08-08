# tafqeet-py
python pkg for converting numbers to arabic words 


## Ex:

```
from tafqeet import Tafqeet, Currency


def main(num, currency):
    if currency == Currency.EGP.value:
        return Tafqeet.tafqeet_EGP(num)

    return Tafqeet.tafqeet(num)


if __name__ == "__main__":
    print(main(17.54324, "EGP"))
```

```
    print(Tafqeet.tafqeet(41612)) 
    
   # واحد وأربعون ألفًا وستمائة واثنى عشر
    
    print(Tafqeet.tafqeet_EGP(956342)) 
    
    # تسعمائة وستة وخمسون ألفًا وثلاثمائة واثنان وأربعون جنيها مصريا فقط لا غير
    
    print(Tafqeet.tafqeet_EGP(17.54324)) 
    
    # سبعة عشر جنيها وخمسة آلاف وأربعمائة واثنان وثلاثون قرشا مصريا فقط لا غير
```

Inspired by 

https://github.com/ASammour/TafqeetJs/