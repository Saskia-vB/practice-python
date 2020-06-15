a = [1,1,2,3]

def rem_dup(a):
    new_list = []
    for item in a:
        if new_list.count(item) < 1:
            new_list.append(item)
    return new_list

print(rem_dup(a))