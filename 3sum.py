

def test(list_data):
    l = len(list_data)
    if l < 3:
        return []
    list_data.sort()
    res = []
    for data in range(l-2):
        if list_data[data] > 0:
            break
        if data > 0 and list_data[data] == list_data[data - 1]:
            continue
        target = 0 - list_data[data]
        i = data + 1
        j = l - 1
        while i < j:
            s = list_data[i] + list_data[j] + list_data[data] 
            if  s == 0:
                res.append([list_data[data], list_data[i], list_data[j]])
                while i < j and list_data[i] == list_data[i + 1]:
                    i += 1
                while i < j and list_data[j] == list_data[j - 1]:
                    j -= 1
                i += 1
                j -= 1
            elif s < 0:
                i += 1
            else:
                j -= 1
    return res

nums = [-1, 0, 1, 2, -1, -4]
print(test(nums))
