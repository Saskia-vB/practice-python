user_input = int(input("Enter a number:"))
u2 = int(input("second number to divide by: "))

if user_input % 4 == 0:
    print("is divisble by 4")
elif user_input %  2 == 0:
    print("is even")
else:
    print("is odd")

def if_div(user_input, u2):
    if user_input % u2 == 0:
        return "is divisible"
    else:
        "not divisible"

print(if_div(user_input, u2))