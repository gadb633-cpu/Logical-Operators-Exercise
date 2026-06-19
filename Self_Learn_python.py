# Part 3
# 1
# short circuit evaluation is :When you run a test on two things, for example, if they are equal, Python checks the first side to see if it is true or false, and then the second side is not interesting, it doesn't check it at all, and then even if there is an error on the other side, it won't show it.
# 2 
# operator precedence is : Operator precedence: Python will first resolve certain operators and then resolve other operators.
# and bifor or
# 3 
#  == This compares whether the content on both sides is equal and does not contradict each other and is It checks whether it is exactly the same variable not only if the content does not contradic
# 4
# Because the None command is stored in the computer's memory in one cell and not each time, the way to compare it is to check whether it is the same address of a location in memory or not, and therefore is is better.
# Practice
# 1
a = 12
b = 10
print(bin(a))
print(bin(b))
print(a ^ b)
# 2
a = 12
b = 10
print(a & b , a | b)
print(bin(a & b))
print(bin(a | b))
# 3 
x = True
y = False
print(x and y)
print(x or y)
print(not(x))
print(not(y))
# 4
num = 8
print(num << 1)
print(num >> 1)
print(bin(num << 1))
print(bin(num >> 1))








