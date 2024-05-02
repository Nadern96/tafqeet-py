import re
from enum import Enum

class Tafqeet:
    _ONES = {
        0: "صفر",
        1: "واحد",
        2: "اثنان",
        3: "ثلاثة",
        4: "أربعة",
        5: "خمسة",
        6: "ستة",
        7: "سبعة",
        8: "ثمانية",
        9: "تسعة",
        10: "عشرة",
        11: "أحد عشر",
        12: "اثنى عشر"
    }
    _TENS = {
        1: "عشر",
        2: "عشرون",
        3: "ثلاثون",
        4: "أربعون",
        5: "خمسون",
        6: "ستون",
        7: "سبعون",
        8: "ثمانون",
        9: "تسعون"
    }
    _HUNDREDS = {
        0: "صفر",
        1: "مائة",
        2: "مئتان",
        3: "ثلاثمائة",
        4: "أربعمائة",
        5: "خمسمائة",
        6: "ستمائة",
        7: "سبعمائة",
        8: "ثمانمائة",
        9: "تسعمائة"
    }
    _THOUSANDS = {
        1: "ألف",
        2: "ألفان",
        39: "آلاف",
        1199: "ألفًا"
    }
    _MILLIONS = {
        1: "مليون",
        2: "مليونان",
        39: "ملايين",
        1199: "مليونًا"
    }
    _BILLIONS = {
        1: "مليار",
        2: "ملياران",
        39: "مليارات",
        1199: "مليارًا"
    }
    _TRILLIONS = {
        1: "تريليون",
        2: "تريليونان",
        39: "تريليونات",
        1199: "تريليونًا"
    }

    @staticmethod
    def _getNth(num, start, end):
        finalNum = ""
        for idx in range(start, end + 1):
            finalNum = finalNum + str(num)[idx]

        return finalNum

    @staticmethod
    def _getNthReverse(num, end):
        finalNum = ""

        pos = 1
        while pos != end and len(str(num)) >= pos:
            finalNum = str(num)[len(str(num)) - pos] + finalNum
            pos += 1

        return finalNum

    @staticmethod
    def _oneTen(num):
        value = "صفر"

        if int(num) in Tafqeet._ONES:
            value = Tafqeet._ONES[int(num)]
        else:
            first = int(Tafqeet._getNth(num, 0, 0))
            second = int(Tafqeet._getNth(num, 1, 1))

            if first in Tafqeet._TENS and second in Tafqeet._TENS:
                if Tafqeet._TENS[first] == "عشر":
                    value = Tafqeet._ONES[second] + " " + Tafqeet._TENS[first]
                else:
                    value = Tafqeet._ONES[second] + " و" + Tafqeet._TENS[first]
        return value

    @staticmethod
    def _hundred(num):
        value = ""

        while len(str(num)) != 3:
            num = "0" + str(num)

        first = int(Tafqeet._getNth(num, 0, 0))

        if first in Tafqeet._HUNDREDS:
            value = Tafqeet._HUNDREDS[first]

        value = value + " و" + Tafqeet._oneTen(int(Tafqeet._getNth(num, 1, 2)))
        return value

    @staticmethod
    def _thousand(num):
        value = Tafqeet._thousandsTrillions(
            Tafqeet._THOUSANDS[1],
            Tafqeet._THOUSANDS[2],
            Tafqeet._THOUSANDS[39],
            Tafqeet._THOUSANDS[1199],
            0,
            int(num),
            Tafqeet._getNthReverse(num, 4)
        )
        return value

    @staticmethod
    def _million(num):
        value = Tafqeet._thousandsTrillions(
            Tafqeet._MILLIONS[1],
            Tafqeet._MILLIONS[2],
            Tafqeet._MILLIONS[39],
            Tafqeet._MILLIONS[1199],
            3,
            int(num),
            Tafqeet._getNthReverse(num, 7)
        )
        return value

    @staticmethod
    def _billion(num):
        value = Tafqeet._thousandsTrillions(
            Tafqeet._BILLIONS[1],
            Tafqeet._BILLIONS[2],
            Tafqeet._BILLIONS[39],
            Tafqeet._BILLIONS[1199],
            6,
            int(num),
            Tafqeet._getNthReverse(num, 10)
        )
        return value

    @staticmethod
    def _trillion(num):
        value = Tafqeet._thousandsTrillions(
            Tafqeet._TRILLIONS[1],
            Tafqeet._TRILLIONS[2],
            Tafqeet._TRILLIONS[39],
            Tafqeet._TRILLIONS[1199],
            9,
            int(num),
            Tafqeet._getNthReverse(num, 13)
        )
        return value

    @staticmethod
    def _thousandsTrillions(one, two, three, eleven, diff, num, other):
        other = int(other)
        other = Tafqeet.tafqeet(other)

        if other == "":
            other = "صفر"

        value = ""
        num = int(num)
        ones = 0
        tens = 0
        hundreds = 0

        if len(str(num)) == (4 + diff):
            ones = int(Tafqeet._getNth(num, 0, 0))

            if ones == 1:
                value = one + " و" + other
            elif ones == 2:
                value = two + " و" + (other)
            else:
                value = Tafqeet._oneTen(ones) + " " + three + " و" + other

        elif len(str(num)) == (5 + diff):
            tens = int(Tafqeet._getNth(num, 0, 1))

            if tens == 10:
                value = Tafqeet._oneTen(tens) + " " + three + " و" + other
            else:
                value = Tafqeet._oneTen(tens) + " " + eleven + " و" + other

        elif len(str(num)) == (6 + diff):
            hundreds = int(Tafqeet._getNth(num, 0, 2))
            two = int(Tafqeet._getNth(num, 1, 2))
            th = ""

            if two == 0:
                th = one
            else:
                th = eleven

            if 100 <= tens <= 199:
                value = Tafqeet._hundred(hundreds) + " " + th + " و" + other
            elif 200 <= tens <= 299:
                value = Tafqeet._hundred(hundreds) + " " + th + " و" + other
            else:
                value = Tafqeet._hundred(hundreds) + " " + th + " و" + other

        return value

    @staticmethod
    def tafqeet(num):
        value = ""
        num = int(num)

        if str(num).isdigit() and len(str(num)) <= 14:

            if len(str(num)) in [1, 2]:
                value = Tafqeet._oneTen(num)

            elif len(str(num)) == 3:
                value = Tafqeet._hundred(num)

            elif len(str(num)) in [4, 5, 6]:
                value = Tafqeet._thousand(num)

            elif len(str(num)) in [7, 8, 9]:
                value = Tafqeet._million(num)

            elif len(str(num)) in [10, 11, 12]:
                value = Tafqeet._billion(num)

            elif len(str(num)) in [13, 14, 15]:
                value = Tafqeet._trillion(num)

        value = re.sub('/وصفر/g', '', value)
        value = re.sub('/ +(?= )/g', '', value)
        value = re.sub('/صفر و/g', '', value)
        value = re.sub('/مئتان أ/', "مائتا أ", value)
        value = re.sub('/مئتان م/', "مائتا م", value)

        return value

    @staticmethod
    def tafqeet_EGP(num):
        pounds_val = Tafqeet.tafqeet(int(num)) + " جنيها"

        pt_val = ""
        if num-int(num) > 0:
            ptr = int((num-int(num))*100)
            print(ptr)
            pt_val = Tafqeet.tafqeet(ptr)

        if len(pt_val) > 0:
            pt_val = " و" + pt_val + " قرشا"

        value = pounds_val + pt_val + " مصريا فقط لا غير"
        return value


class Currency(Enum):
    EGP = 'EGP'
