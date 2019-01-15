#Count Words in a String – Counts the number of individual words in a
#string. For added complexity read these strings in from a text file
#and generate a summary.

import operator

filename="words.txt"  # assigns the text file to a variable


#define dictionary to hold unique words and their count

word_list = {}

#goes through the text file line by line, spliting it into single words on a list
#then in the list it goes through each entry and looks at the word_list dictionary
#if it exsits in the dictionary, it adds 1 to the count if not it adds it to the dictionary
   
with open(filename, "r", encoding="utf8") as f:
    for line in f:
        words = line.split()
        for word in words:
            if word in word_list:
                word_list[word] += 1
            else:
                word_list[word] = 1
        
        
#if a whole summary is desired of the text file, uncomment the following line

#print(word_list)

#new dict is the placeholder for the top 5 items of the dictionary above
#then it prints this new_dict or summary of the top 5 used words
new_dict = dict(sorted(word_list.items(), key= operator.itemgetter(1), reverse=True)[:5])

print(new_dict)
        #if word is in dictionary then word's value is +1
        #if not add to the end of the dictionary with a value of 1

        
