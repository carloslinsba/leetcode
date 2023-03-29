from longest14 import Solution

class Longest_14_TestCase():
    test= {
        'fl': ["flower","flow","flight"],
        '': ["dog","racecar","car"],
        'a': ["aa", "ab"],

    }

a =Longest_14_TestCase()
for entry in a.test.keys():
    print (Solution().longestCommonPrefix(a.test.get(entry)))
    print (entry)
    print (a.test.get(entry))
    if entry == Solution().longestCommonPrefix(a.test.get(entry)):
        print("Success", entry)
    else:
        print("Failed", entry)
    



