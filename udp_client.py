import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INETm socket.SOCK_DGRAM)

# send some data
client.sendto("AAABBBCCC",(target_host,target_port))

# received some data
data, addr = client.recvfrom(4096)

print data