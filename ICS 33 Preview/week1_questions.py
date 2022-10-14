'''
Created on 2020-7-26

@author: panru
'''
# 
# def count(a: int, l: list):
#     count = 0
#     for i in l:
#         if i == a:
#             count += 1
#     return count
# 
# def indexes(a: int, l: list):
#     l2 = []
#     for i in range(len(l)):
#         if l[i] == a:
#             l2.append(i)
#     return l2
# 
# print(count(5, [5,3,4,5,1,2,5]))     
# print(indexes(5, [5,3,4,5,1,2,5]))

# first version of 1.7
def call(func: str, value):
    callable = {'double': 2, 'triple': 3, 'quadruple': 4, 'times10': 10}
    return eval(str(callable[func]) + '*' + str(value))
print(call('times10',5))

# second version of 1.7 without eval()
def call2(func: str, value):
    callable = {'double': (lambda x: 2*x), 'triple': (lambda x: 3*x), 'quadruple': (lambda x: 4*x), 'times10': (lambda x: 10*x)}
    return callable[func](value)

print(call2('double',5))

# 8 with closure

def between(a, b):
    def func_determinant(x):
        return a<= x <= b
    return func_determinant

college_age = between(18,22)
print(college_age(100))


print("-"*20, '8b')
# 8b 
def running_average2():
    sum = [0]
    count = [0]
    def include_it(x):
        sum[0] += x
        count[0] += 1
        return sum[0]/count[0]
    return include_it
a = running_average2()
print(a(1))
print(a(2))
print(a(4))

print('-'*20, '9')
# 9
# simpler one


        