#convert one dimensional list to an array using the array() NumPy function
from numpy import array
data_one = [11,22,33,44,55]
data_one = array(data_one)
print(data_one)
print(type(data_one))

#Two dimension data 
data = [[11,22],[33,44],[55,66]]
data = array(data)
print(data)
print(type(data))

#Array indexing 
#print the last two values in a data set 1 dimension array
print(data_one[-1])
print(data_one[4]) 
print()

#2d indexing of data
print(data[0,1])
#print first row
print (data[0,])
print()


#Array Slicing
#Access all data in ana array
print('Print all elements in the array',data_one[:])
print()
print('Print all elements in a 2D array',data[:])
#slice data from index 0 to 1 
print('Slice data from Index 0 to 1', data_one[0:1])
#slice data from the end of the dimension
print('Slice data with negative index', data_one[-2:])
 #Slice a 2d array
data_three = array([[11,22,33], [44,55,66],[77,88,99]])
X, y = data_three[:, :-1], data_three[:, -1]
print(X)
print(y)

#Split tarin and Test Trains
#split a loaded data dataset and separate train and test sets
#Split some rows in which some rows are used for trainig and the remainder for testing
data_three = array([[11,22,33], [44,55,66],[77,88,99]])
split = 2
train, test = data_three[:split,:],data_three[split:,:]
print('Train data set', train)
print('Test data set', test) 


# shape
data = array(data_one)
print(data_one.shape)
print(data_three.shape)


