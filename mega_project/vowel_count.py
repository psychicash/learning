#Count Vowels – Enter a string and the program counts the number of
#vowels in the text. For added complexity have it report a sum of
#each vowel found.
#does not handle instances of y...

to_count = input("Enter a word:")
vowel_count = 0
vowels = ['a', 'e', 'i', 'o', 'u']


for i in range(len(to_count)):
    item_checked = to_count[i]
    if item_checked in vowels:
        vowel_count += 1


print("There are " + str(vowel_count) + " vowels in " + to_count + ". Have a nice day.")

