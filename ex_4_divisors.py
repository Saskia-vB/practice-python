num = int(input("please enter a number :"))

def divisors(num):
    div_list = []
    for i in range(1,num):
        if num % i == 0:
            div_list.append(i)
    return div_list

# print(divisors(num))

