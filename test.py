'''
Created on Oct 20, 2017

@author: U0117078
'''
x = 10
if(x < 0):
    x = 0
    print("Negative Number")
elif x == 0:
    print("Zero")
elif x == 1:
    print("one")
else:
    print("More")
    
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
print(words)

for i in range(10):
    print(i)
for i in range(5,10):
    print(i)
for i in range(5,25,3):
    print(i)

print(list(range(5)))

def fibonacci(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
         print(a, end=' ')
         a, b = b, a+b
         print()
    fibonacci(10)