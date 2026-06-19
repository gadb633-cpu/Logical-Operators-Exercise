# Part 1
# 1
is_online = True 
has_access = False
print(is_online and has_access)
# 2
print(is_online or has_access)
# 3
status = False
print(not(status))
#4
age = 20
has_id = True
print(age>18 and has_id)
# 5
level = 3
print(1<level and 5>level)
# 6
a = 0
b = "hello"
c = ""
print(bool(a))
print(bool(b))
print(bool(c))
# 7
x = None
y = 42
print(x or y)
# Value 42 returned because None is nothing.
# 8
username = ""
default = "guest"
final_username = username or default
print(final_username)
# 9
print(True and False or True)
print((True and False) or True)
# 10
score = 75
print(score>60 and score<100)

