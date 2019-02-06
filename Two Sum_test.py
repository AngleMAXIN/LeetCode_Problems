

def two_sum(number_list, targer):
    if len(number_list) == 0:
        return []
    d = dict()

    for i in range(len(number_list)):
        if targer - number_list[i] in d:
            return [d[targer - number_list[i]], i]
        d[number_list[i]] = i
    return []

if __name__ == '__main__':
    numbers = [2, 5, 8, 4,6]
    target = 10
    result = two_sum(numbers, target)
    print(result)
