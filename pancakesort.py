from random import randrange

#Make a function to flip the passed array between the start and stop indices [inclusive]
#Actually a useful function outside this exercise. 
def flip(a, start, stop):
	b = a[start:stop+1];
	b = b[::-1];
	b = a[0:start]+b+a[stop+1:len(a)];
	return b;

#Perform the pancake sort! Can only sort by flipping from one part of the stack to the a side over. 
#The idea is to move the minimum element to the last element of the array and then effectively make the array 1 element smaller. 
#Keep performing the algorithm until there is 1 element left and the array should be sorted
#Not optimized. Requires >O(n^2) time. But was quick to write. You know what they say about premature optimization  :)

def pancakeSort(arr):
	for i in range(len(arr)):
		min = arr[0]; minindex = 0; 
		for j in range(len(arr)):
			if( (j<=len(arr)-1-i) and (arr[j] < min)):
				min = arr[j];
				minindex = j;
		arr = flip(arr,0,minindex);
		arr = flip(arr,0,len(arr)-i-1);
	arr = arr[::-1];
	return arr;
	

#Test out the pancake sort on a 10 element array 
b = [];
for i in range(10):
	b.append(randrange(100));

print b;
print pancakeSort(b);
#It works.
