# input string
# read backwords

while True:
    user_input = input("please enter a word: ")
    def palindrome(user_input):
        user_input = user_input.lower()
        user_input = user_input.replace(" ","")
        if user_input == user_input[::-1]:
            return "this word is a palindrome"
        else:
            return "this is not a palindrome"

    print(palindrome(user_input))