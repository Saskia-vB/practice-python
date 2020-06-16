def div_3_5(num):
    return num % 5 == 0 and num % 3 == 0

def div_5(num):
    return num % 5 == 0

def div_3(num):
    return num % 3 == 0

def fizzbuzz(num):
    if div_3_5(num):
        print("fizzbuzz")
    elif div_5(num):
        print("fizz")
    elif div_3(num):
        print('buzz')
    else:
        print(num)

while True:
    num = input('please enter number: ')
    if "exit" in num:
        print("bye for now")
        break
    if num.isnumeric():
        num =int(num)
    for number in range(1, num+1):
        fizzbuzz(number)
