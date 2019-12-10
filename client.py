import random, socket, sys

with open ('numbers.txt') as ifile:lines = ifile.readlines()
a = []
for i in range(3):a.append(int(lines[i]))
n = int(lines[6])
cid = '0'
while cid not in '123':cid = raw_input('\nEnter client id (1-3): ')
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 15061)
print "Connecting to server..."
soc.connect(address)
try:
	x = str(random.randint(10, 9999))
	print 'x =',x
	y = str((int(x)**2) % n)
	soc.sendall((y + cid).zfill(10))
	t = int(soc.recv(1))
	print 't =',str(t)
	if t == 0:
		soc.sendall(x.zfill(8))
	elif t == 1:
		x = str(int(x) * a[int(cid) - 1])
		soc.sendall(x.zfill(8))
	reply = soc.recv(14)
	print reply
except(KeyboardInterrupt):
	print "Closing socket..."
	soc.close()
