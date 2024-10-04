
fileObject = open("output.txt", mode="w")

print("Hello Ben!", file=fileObject)

print("Hello","Ben","ThirdValue",sep = ":")

print("Hello",end="")
print("Goodbye")

print("Hello","Ben","ThirdValue",end="",sep = "-")

print("Hello","Ben","ThirdValue",sep = "-", end="xx")