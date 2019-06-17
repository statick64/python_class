divisorList=[]

x=int(input("Enter a number to find its divisors: "))
for i in range(1,x+1):
    while i<=x: 
        if x%i == 0:
            divisorList.append(i)
            i+=1
            print (str(x) +" has " + str(len(divisorList) )+ " divisors") 
            print (divisorList)