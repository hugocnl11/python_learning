#logical operators (and, or) = used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("The temperature is good today!")
    print("Go outside!")
elif temp <0 or temp > 30:
    print("The temperature is bad, take care!")

#this is the same code but with the negative sentences using "if not" or "elif not"
#if not temp >= 0 and temp <= 30:
#    print("The temperature is bad, take care!")
#elif not temp <0 or temp > 30:
#    print("The temperature is good today!")
#    print("Go outside!")
