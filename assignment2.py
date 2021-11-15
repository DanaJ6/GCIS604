import csv
import array as Array


with open('assignment2_file.csv','r') as csvotg:
    con=csv.reader(csvotg)
    con_list=[]
    for x in con:
        con_list.append(x)
    tuple_new_data=[]
    for x in con_list[1]:
        if x!="":
            tuple_new_data.append(int(x))
        else:
            pass
    arraynewdata=list(map(int,con_list[0]))
    tuplenewdata=list(map(int,tuple_new_data))
    array1=Array.array('i',arraynewdata)
    tuple1=tuple(tuplenewdata)
    list1=con_list[4]
    set1=set(con_list[5])
    dict1=dict(zip(con_list[6],con_list[5]))
 
an_array = Array.array('i', [5, 20, 30, 34, 45, 67, 78, 90, 97])

print(array1,'\n',tuple1,'\n',list1,'\n',set1,'\n',dict1)

with open('assignment2_file.txt','w') as file1:
    data=str(dict1)+'\n'+str(list1)+'\n'+str(tuple1)+'\n'+str(array1)
    file1.write(data)

print("\n")


con=[]

with open('assignment2_file.txt','r') as file2:
    for line in file2:
        con.append(line.rstrip())
for x in con:
    print(x)

print("\n")

if 'Fujairah' in list1 and 'brown' in set1 and 'Data Science' in dict1:
    print("Yes, Found them!!\n 'Fujairah' in list1,\n 'brown' in set1 and \n 'Data Science' in dict1")
else:
    print("None")

print("\n")

#insertion sort
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

'''merge sorting using the function's for tuple1'''

def merge_sort(array):
    if len(array)<=1:
        return array
    midpoint=len(array)//2
    left,right=merge_sort(array[:midpoint]),merge_sort(array[midpoint:])
    return merge(left,right)
def merge(left,right):
    result=[]
    left_pointer=right_pointer=0
    while left_pointer< len(left) and right_pointer<len(right):
        if left[left_pointer]<right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer +=1
        else:
            result.append(right[right_pointer])
            right_pointer+=1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result

ltuple1=list(tuple1)
resultuple1=merge_sort(ltuple1)
tuple1=tuple(resultuple1)


def quick_sort(sequence):
    length = len(sequence)
    if length < 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item >pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

quick_sort(list1)


'''Quick sorting for set1'''

quick_sort(set1)

'''sorting by value done for dict1'''

ndict1={}
for x in sorted(dict1):
    temp=dict1[x]
    ndict1[x]=temp
dict1=ndict1


with open('assignment2_file.txt','w') as file3:
    data=str(array1)+'\n'+str(tuple1)+'\n'+str(list1)+'\n'+str(set1)+'\n'+str(dict1)
    file3.write(data)


con=[]
with open('assignment2_file.txt','r') as file4:
    for line in file4:
        con.append(line.rstrip())


for x in con:
    print(x)

print("\n")

with open('assignment2_file2.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    for x in con:
        temp=[]
        temp.append(x)
        writer.writerow(temp)
