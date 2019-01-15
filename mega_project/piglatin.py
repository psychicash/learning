#pig latin: take a word move the first letter to the end and add an ay
#it works but not proud of this lol

print("enter a word please")
pigglet = input().split(" ")
print(pigglet)


for i in range(len(pigglet)):
    word = pigglet[i]
    grownpig = []
    for i in range(1, len(word)):
        grownpig.append(word[i])
    grownpig.append("-")
    grownpig.append(word[0])
    grownpig.append("ay")
    grownpig = "".join(grownpig)
    print(grownpig)
    
