#initial list [5,1,2,4,3]
# k=0(the first element is 5)
# m=1
# swap 5 and 1
# list after swap is[1,5,2,4,3]
# k=1(the first two element is 1,2)
# m=2
# swap 5 and 2
# list after swap is[1,2,5,4,3]
# k=2(the first three element is 1,2,3)
# m=3
# swap 5 and 3
# list after swap is[1,2,3,4,5]
# k=3(the first four element is 1,2,3,4)
# m=4
# no need to swap
# k=4(the first four element is 1,2,3,4,5)
# m=5
# no need to swap
# k=5
# so final list is [1,2,3,4,5]


#yes

# In this case, the swap does not change the list,
#and repeat the remaining steps until the sorting is complete.

#It directly modifies the input list,
#so there is no need to return a new list during the sorting process.


