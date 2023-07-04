### EVERYTHING IS OBJECT IN PYTHON
This elaborates more om how data values in Python are represented in objects such as numbers, strings and lists

#### The Requirements
- The allowed editors are emacs, vi and vim
- README.md file, at the root of the folder of the project
- files should end with a new line
- No shebang in .txt files
- Only one line in .txt answer files

#### The Tasks
- What function would you use to get the type of an object?
- How do you get the variable identifier (which is the memory address in the CPython implementation)?
- In the following code, do a and b point to the same object? Answer with Yes or No.
- In the following code, do a and b point to the same object? Answer with Yes or No.
- In the following code, do a and b point to the same object? Answer with Yes or No
- In the following code, do a and b point to the same object? Answer with Yes or No.
- What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = s1
>>> print(s1 == s2)
- What do these 3 lines print?
>>> s1 = "Best"
>>> s2 = s1
>>> print(s1 is s2)
- What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 == s2)
- What do these 3 lines print?
>>> s1 = "Best School"
>>> s2 = "Best School"
>>> print(s1 is s2)
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 == l2)
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3] 
>>> print(l1 is l2)
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 == l2)
- What do these 3 lines print?
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> print(l1 is l2)
- What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1.append(4)
print(l2)
- What does this script print?
l1 = [1, 2, 3]
l2 = l1
l1 = l1 + [4]
print(l2)
- What does this script print?
def increment(n):
    n += 1

a = 1
increment(a)
print(a)
- What does this script print?
def increment(n):
    n.append(4)

l = [1, 2, 3]
increment(l)
print(l)
- What does this script print?

def assign_value(n, v):
    n = v

l1 = [1, 2, 3]
l2 = [4, 5, 6]
assign_value(l1, l2)
print(l1)
- Write a function def copy_list(l): that returns a copy of a list.
What does this script print?
a = (1)
b = (1)
a is b
- What does this script print?

a = (1, 2)
b = (1, 2)
a is b
- Will the last line of this script print 139926795932424? Answer with Yes or No.
>>> a
[1, 2, 3]
>>> id (a)
139926795932424
>>> a += [4]
>>> id(a)
