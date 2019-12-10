import random, socket, sys, threading

with open ('numbers.txt') as ifile:lines = ifile.readlines()
a = []
b = []
for i in range(3):a.append(int(lines[i]))
for i in range(3,6):b.append(int(lines[i]))
n = int(lines[6])

def Client(conn, address):
	try:
		print "Incoming connection from client..."
		data = conn.recv(10)
		t = random.choice('01')
		conn.sendall(t)
		z = conn.recv(8)
		z = int(z)
		print 'y =',data[0:-1]
		print 'z =',str(z)
		if int(t) == 0:
			if ((z**2) % n) == int(data[0:-1]):conn.sendall(('Welcome Name-'+data[-1]))
			else:conn.sendall('Access denied')
		elif int(t) == 1:
			if ((z**2) % n) == ((b[int(data[-1])-1] * int(data[0:-1])) % n):conn.sendall('Welcome Name-' + data[-1])
			else:conn.sendall('Access denied!')
	finally:conn.close()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 15061)
print "Server running..."
soc.bind(address)
soc.listen(1)
connList = []
try:
	while 1:
		print "Waiting for connection..."
		conn, address = soc.accept()
		thread = threading.Thread(target = Client, args = (conn, address))
		if (len(connList)==3):
			connList[0].join()
			connList.pop(0)
		connList.append(thread)
		connList[-1].start()
except(KeyboardInterrupt):print '\nConnection Closed...'
