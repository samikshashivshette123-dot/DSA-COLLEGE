n = int(input("\nhow many no. of Emplyees in company ?"))
array = []
i=0
for i in range(n):
     item = float(input("\n Enter  Salary of Employee"))
     array.append(item)
print("You have entered following Salary\n",array)
def SelectionSort(arr,n):      
    for i in range(n):
        Min = i
        for j in range(i+1,n):
            if(arr[j]<arr[Min]):
                Min = j
        temp=arr[i]
        arr[i]=arr[Min]
        arr[Min]=temp        
    print("\n The sorted Salary are using Selection Sort:-",arr)
SelectionSort(array,n)
def BubbleSort(arr,n):
        for i in range(len(arr)-1):
            for j in range(len(arr)-1):
                if(arr[j] > arr[j+1]):
                    temp = arr[j]
                    arr[j] = arr[j+1]
                    arr[j+1] = temp
        print("\n The sorted Salary using Bubble Sort:-",arr)
        arr.reverse()
        print("\n Top five Salaryof Employee :", arr[:5])
BubbleSort(array,n)