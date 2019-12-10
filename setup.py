import random, libnum, os

p = 191
q = 29
n = p * q

a = []
b = []
for i in range(3):
	a.append(random.randint(2, (n-1)))
	b.append((a[i]**2) % n)

res = open('numbers.txt', 'w')
for i in range(3):res.write(str(a[i])+'\n')
for i in range(3):res.write(str(b[i])+'\n')
res.write(str(n))
res.close()

os.system('python server.py')
