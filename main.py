from tafqeet import Tafqeet, Currency


def main(num, currency):
    if currency == Currency.EGP.value:
        return Tafqeet.tafqeet_EGP(num)

    return Tafqeet.tafqeet(num)


if __name__ == "__main__":
    print(main(17.54324, "EGP"))