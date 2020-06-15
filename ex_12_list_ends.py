a = [5, 10, 15, 20, 25]

# def list_ends(a):
#     new_list = []
#     new_list.append(a[0])
#     new_list.append(a[-1])
#     return new_list
#
# print(list_ends(a))

def list_ends(a):
    return [a[0], a[-1]]

print(list_ends(a))