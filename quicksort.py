import random

#Pick a pivot
#put all the elements less than the pivot in a list
#---------------------greater than ----------------
#sort both sublists:
#answer is quicksort(less) + pivot + quicksort(greater)

#we can choose any pivot
#but ideally it should be close to the median value
#we can use the leftmost/rightmost or random element
#it will take O(n logn) time for an average unsorted list

#Quicksort will take O(n**2) when the list is already or almost sorted!

#############################
#an implementation with the first element as the pivot
def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        
        print("less: ", less)
        print("greater: ", greater)
        print('-----------------')

        return quicksort(less) + [pivot] + quicksort(greater)

#print(quicksort([10, 5, 2, 9, 17, 7, 3, 6, 4, 12, 13, 8, 19, 11]))
#############################

#an implementation with a random element as the pivot
def quicksort2(list):
    if len(list) < 2:
        return(list)
    else:
        index = random.randrange(len(list))
        pivot = list[index]
        print(pivot)
        list.remove(pivot)
        
        less = [i for i in list if i <= pivot]
        greater = [i for i in list if i > pivot]

        print("less: ", less)
        print("greater: ", greater)
        print('-----------------')

        return quicksort2(less) + [pivot] + quicksort2(greater)

print(quicksort2([10, 5, 2, 9, 17, 7, 3, 6, 4, 12, 13, 8, 19, 11]))