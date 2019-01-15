#Check if Palindrome – Checks if the string entered by the user is a
#palindrome. That is that it reads the same forwards as backwards like
#“racecar”

def reverse(word):
    word = str(word)
    reversed_word = word[-1:-(len(word) + 1):-1]
    return reversed_word


to_be_checked = input("Please enter a word you'd like to check?")

if (to_be_checked == reverse(to_be_checked)):
    print("The word " + str(to_be_checked) + " is a palindrome.")
else:
    print("The word " + str(to_be_checked) + " is not a palindrome. Sorry!")
    
