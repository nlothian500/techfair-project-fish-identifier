score = 0

x = input("what is your favourite food?")
if x == "chicken":
    print("correct")
    score+=1
else:
    print("incorrect")

p = int(input("what is 2+2?"))
if p == 4:
    print("correct")
    score+=1
else:
    print("incorrect")

j = input("what is the name of the capital of jamaica called?")
if j == "kingston":
    print("correct")
    score+=1
else:
    print("incorrect")
print(str(score)+"/3")

