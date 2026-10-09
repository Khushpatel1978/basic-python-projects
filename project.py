# w>g
# g>s
# s>w
l = ["water", "gun", "snake"] 
a = int(input("enter your option: ")) 
if a<3: print("your option is: ", l[a])
else:
    print("INVALID CHOISE")
    quit()

import random

b = ["water", "gun", "snake"] 

choices = random.choice(b) 
print(f"computer chosen option: {choices}") 

if(l[a]==choices):
    print("draw")

elif(l[a]=="water" and choices=="gun"): 
    print("won") 
elif(l[a]=="gun" and choices=="snake"): 
    print("won") 
elif(l[a]=="snake" and choices=="water"): 
    print("won")
else: 
    print("lose")
