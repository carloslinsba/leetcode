from baseball import calPoints

class Baseball_Test_Case():
    test= {
        30: ["5", "2","C","D", "+"],
        27: ["5", "-2","4","C", "D","9","+", "+"],
        1: ["1"],
        
    }

a =Baseball_Test_Case()
for entry in a.test.keys():
    if entry == calPoints(a.test.get(entry)):
        print("Success", entry)
    else:
        print("Failed", entry)