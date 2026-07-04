import numpy as np
print("-=-  Simple Statics Calculator  -=-")
try:
    num = int(input("Enter How many number you Want to generate: "))
except ValueError:
    print("Enter Correct integer number!!")
else:
    arr = np.random.randint(10,100,num)
    print("Generated Array: \n",arr)
    print("Mean: ",np.mean(arr))
    print("Median: ",np.median(arr))
    print("Standerd Deviation: ",np.std(arr))
    print("Minimum: ",arr.min())
    print("Maximum: ",arr.max())
    flag = False
    for i in range(int(np.sqrt(num)),1,-1):
        if num % i == 0:
            rows = i
            columns = num // i
            flag = True
            arr2 = np.reshape(arr,(rows,columns))
            print(arr2)
            break
    if flag == True:
        print("Reshaped into 2D array: ")
    else:
        print("Unable to reshape into 2D matrix !!")
    
    print("Row-wise sum: ",np.sum(arr2,axis = 1))
