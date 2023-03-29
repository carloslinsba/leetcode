from int_to_english import Solution

class Int_English_TestCase():
    test= {
        0: "Zero",
        1: "One",
        23: "Twenty Three",
        123: "One Hundred Twenty Three",
        2345: "Two Thousand Three Hundred Forty Five",
        12345: "Twelve Thousand Three Hundred Forty Five",
        412345: "Four Hundred Twelve Thousand Three Hundred Forty Five",
        1234567: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
        2147483647: "Two Billion One Hundred Fourty Seven Million Four Hundred Eighty Three Thousand Six Hundred Fourty Seven"
    }

a =Int_English_TestCase()
for entry in a.test.keys():
    if a.test.get(entry) == Solution().numberToWords(entry):
        print("Success", entry)
    else:
        print("Failed", entry)

#  get pattern -> hundreds, then make a string slicing and add the correct wording when needed