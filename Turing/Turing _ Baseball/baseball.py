
def is_float(entry):
    try: 
        float(entry)
        return True
    except:
        return False


def calPoints(ops) -> int:
    list =[]
    for entry in ops:
        if is_float(entry):
            list.append(float(entry))
        else:
            if entry.strip() == 'C':
                list.pop()
            else:
                if entry.strip()=='D':
                    list.append(2*float(list[len(list)-1]))
                else:
                    if entry.strip()=='+':
                        list.append( list[len(list)-1] + list[len(list)-2] )

    result = 0
    for entry in list:
        result+= entry
    return result

if __name__ =='main':
    line = input()
    ops = line.strip().split()

    print (calPoints(ops))