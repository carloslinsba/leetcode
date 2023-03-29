from findDuplicate import Solution

class DuplicateFiles609_TestCase():
    test= {
        "["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]":["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"],
       [["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]] : ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"],
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