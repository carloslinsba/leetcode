from isomophirc_205 import Solution

class iso_TestCase:
    test = {
        "egg,add" : True,
        "foo,bar" :  False,
        "paper, title" : True,
        "badc, baba" : False,

    }

t = iso_TestCase()
for entry in t.test:
    parameter = entry.split(",")
    if Solution().isIsomorphic(parameter[0].strip(), parameter[1].strip()) == t.test.get(entry):
        print("Success", entry)
    else:
        print("Failed", entry)



