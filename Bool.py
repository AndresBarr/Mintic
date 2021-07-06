"""a=True
print (type(a)) #Class Bool
b=False
c=True

print(not(a)) #false
print(not(b)) #True
print(a and b) #False
print(a and c) #True
print(a or b) #True
print(a or c) #True
print (b or b) #True"""

p = 10
q = 3
r = 5

if (p > 2) and (q < 3):
    print('entra al if 1')
if (r == 5) and ((q == 3) or (r > 1)):
    print('entra al if 2')
if not(p<10):
    print('entra al if 3')
if not (q==2):
    print('entra al if 4')

