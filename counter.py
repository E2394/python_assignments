sentence = input("Gimme a sentence..>")
a =dict()
m = 0

for i in sentence:
    if i not in a.keys():
        counter=sentence.count(i)
        a.update({sentence[m]:counter})
        m+=1
    else:
        m+=1

print(a) 
