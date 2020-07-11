import json
from difflib import get_close_matches

cont=json.load(open("data.json"))
#print(cont)

def translate(w):
    #If word is there in cont, give output
        #Ask for intended word by asking yes or no and return defination
    if w in cont:
        return cont[w]
    elif len(get_close_matches(w,cont.keys(),cutoff=0.8))>0:
        yn=input("Did you mean {} instead? Enter Y for yes and N for no :  ".format(get_close_matches(w,cont,cutoff=0.8)[0])).lower()
        if yn=="y":
                 return cont[get_close_matches(w,cont,cutoff=0.8)[0]]
        elif yn=="n":
                 return "We didnt get your word.Double check it."
    else:
        return "No such word"

while True:
    word=input("Enter the word: ").lower()
    a=translate(word)

    if type(a)==list:
        for item in a:
            print("*" + item)

    else:
        print(a)        
    
