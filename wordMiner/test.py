file = open("dictionary.txt", "r")

def is_valid(word): # checks if word is valid
    if len(word) <= 3 or len(word) > 7:
        return False
    
        
    return True

for word in file: # loops through each word
    if is_valid(word) == True:
        print(word)
        
