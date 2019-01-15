#Reverse a String – Enter a string and the program will reverse it and print it out.

print("Please enter something...anything\n")
toBeReversed = input()

toBeReversed = str(toBeReversed)
Reversed = toBeReversed[-1:-(len(toBeReversed) + 1):-1]
print(Reversed)
