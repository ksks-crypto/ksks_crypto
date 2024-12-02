global word 
word = "wowowowoww"

def __len__(word):
    global length
    length = int(len(word))

__len__(word)

for i in range(length):
    if (i % 2 > 0):
        print(word[i] + f" {i}")
