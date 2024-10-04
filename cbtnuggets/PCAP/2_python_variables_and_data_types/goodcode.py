#Our starting Values
term1 = 0
term2 = 1
count = 0
totalterms = 10

#Loop until we hit our total
while count < totalterms:
    print(term1)

    #Update the value with each cycle
    nextterm = term1 + term2
    term1 = term2
    term2 = nextterm
    count = count + 1

#################################
    n1,n2,c = 0,1,0
    while c<10:
        print(n1);n=n1+n2
        n1=n2;n2=n;c+=1
