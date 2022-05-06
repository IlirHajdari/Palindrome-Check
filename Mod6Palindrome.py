def is_palindrome(word):
#logic to check if input is palindrome
    if len(word) < 1:
        return True
    else:
        if word[0].lower() == word[-1].lower():
            return is_palindrome(word[1:-1])
        else:
            return False
        
#user input
user_input = str(input("Check if entry is a palindrome: "))
if(is_palindrome(user_input) == True):
    print("The entry is a palindrome!")
else:
    print("The entry is not a palindrome! Please try again.")