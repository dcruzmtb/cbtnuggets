

#for x in range(0,10):
#    print("Value of x:",x)
#    answer = input("Press y then enter to end.")
#    if answer == "y":
#        break

x = 10
y = 15

while x < y:
    print("Value of x is:",x)
    answer = input("Press y to continue this loop.")

    if answer == "y":
        #Do some code in the future
        pass
    x += 1
else:
    print("The whole loop ran.")

print("This is the end of my code.")

