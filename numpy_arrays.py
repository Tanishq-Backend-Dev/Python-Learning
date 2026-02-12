from numpy import *

# 1st way of creating an array

#val = array([1,2,3,4,5])
#print(val) -> [1 2 3 4 5]

# 2nd way of creating an array

#val = linspace(0,15,20)
#print(val) ->  [0.          0.78947368  1.57894737  2.36842105  3.15789474  3.94736842
#  4.73684211  5.52631579  6.31578947  7.10526316  7.89473684  8.68421053
#  9.47368421 10.26315789 11.05263158 11.84210526 12.63157895 13.42105263
# 14.21052632 15.        ]

# 3rd way of creating an array

# val = arange(1,15,2)
# print(val) -> [ 1  3  5  7  9 11 13]

# 4th way of creating an array

# vals = logspace(1,40,5)
# print(vals) -> [1.00000000e+01 5.62341325e+10 3.16227766e+20 1.77827941e+30
#  1.00000000e+40]

# 5th way of creating an array

# vals = zeros(5)
# print(vals) -> [0. 0. 0. 0. 0.]

# 6th way of creating an array

# vals = ones(5)
# print(vals)

#----------------------------------------------------------------------------------------#

# arr = array([1,2,3,4,5])
# arr = arr + 5
# print(arr) --> [ 6  7  8  9 10]

# arr1 = array([1,2,3,4,5])
# arr2 = array([6,7,8,9,10])
# arr3 = arr1 + arr2
# print(arr3) --> [ 7  9 11 13 15]

# arr = array([1,2,3,4,4,5])
# print(sum(arr))

#----------------------------------------------------------------------------------------#
# Copying an array

# arr1 = array([1,2,3,4,5])
# arr2 = arr1

# print(arr1)
# print(arr2)

#----------------------------------------------------------------------------------------#

# Create a multi-dimensional array

arr1 = array([
    [1,2,3],
    [4,5,6]
])
print(arr1)

m = matrix(arr1)
print(m)
