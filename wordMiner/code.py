def hash_generator(word): # generates hash code
    hash = 0
    x = 0
    
    for i in word:
        hash += ord(i) * (x+1)
        x+=1
    
    hash %= 20000    
    
    return hash
    
def is_valid(word): # checks if word is valid
    if len(word) <= 3 or len(word) > 7:
        return False
        
    return True
    
hashTable = [[0 for y in range(20000)] for x in range(20)]

wordCount = 0

file = open("dictionary.txt", "r")

for word in file: # loops through each word
    if is_valid(word) == True:
        row = hash_generator(word) # cuts repetition
        
        for y in range(10):
            if hashTable[y][row] == word: # if it is the word
                break
            if hashTable[y][row] == 0:
                hashTable[y][row] = word
                wordCount += 1
                break
            
print(wordCount)
            
            
for i in range(10):
    print(hashTable[i][1136])

'''
for y in range(20000):
    for x in range(10):
        
        print(hashTable[x][y], " ", end="")
        
    print()
'''