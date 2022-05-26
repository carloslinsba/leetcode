from integer_to_roman import Solution

class Roman_Int_TestCase():
    test= {
        1: "I",
        3: "III",
        4: "IV",
        40: "XL",
        90: "XC",
        58: "LVIII",
        1994: "MCMXCIV"
    }

a =Roman_Int_TestCase()
for entry in a.test.keys():
    if a.test.get(entry) == Solution().intToRoman(entry):
        print("Success", entry)
    else:
        print("Failed", entry)
    



