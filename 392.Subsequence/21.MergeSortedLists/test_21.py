from merge21 import Solution

class TestCase():
    test= {
        ["aaaaaa,bbaaaa"]: False,
        "a,b":  False,
        "abc,ahbgdc":  True,
        "axc,ahbgdc":  False,
        
    }

t = SubsequenceTestCase()
for entry in t.test:
    parameter = entry.split(",")
    if Solution().isSubsequence(parameter[0].strip(), parameter[1].strip()) == t.test.get(entry):
        print("Success", entry)
    else:
        print("Failed", entry)