data = "learning python and python learning python is fun have fun with python learning python and"
word_count = dict()
for word in data.split(" "):
    word_count[word] = word_count[word]+1 if word_count.get(word) else 1

for word,count in word_count.items():
    print(f"{word}  = {count}") 
