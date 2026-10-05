text = "python is easy and python is powerful and python is fun"

words=text.split()

kawsar={}
most_word=""
count_highest=0

for word in words:
    if word in kawsar:
        kawsar[word]+=1
    else:
        kawsar[word]=1

for word,count in kawsar.items():
    print(word,":",count)
    if count>count_highest:
        count_highest=count
        most_word=word
print("Most repeted word:",most_word)
print("Count:",count_highest)




