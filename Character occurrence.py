string = input("please enter youre own word : ")
char = input("please enter youre own character : ")
i = 0
count = 0
while(i < len(string)): #string operaton

    if(string[i] == char): #conditon 1
        count = count + 1
    i = i + 1
print("the total number of times",char,"has occured=", count)