a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



def list_overlap(a,b):
    new_list = []
    for number in a:
        if number in b:
            if new_list.count(number) < 1:
                    new_list.append(number)
    return new_list

print(list_overlap(a,b))