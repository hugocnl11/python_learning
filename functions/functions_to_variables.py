def hello():
    print("Hello")

#print(hello) #it prints the memory adress when the function is located in memory
hi = hello
print(hi) #have the same memory adress

hi() # will make the same like hello() with a diferent name


say = print

say("WOW! i cant belive this works")