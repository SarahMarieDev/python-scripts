import socket

# # TCP Sockets

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(("0.0.0.0", 1337))

# print('Connected!')

# while True:
#     message = input("[SEND]: ")
#     sock.send(str.encode(message))
#     received = sock.recv(1024)
#     print(received.decode("utf-8"))

# socket.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Ready!')

while True:
    message = input("[SEND]: ")
    sock.sendto(str.encode(message), ("0.0.0.0", 1337))
    received = sock.recvfrom(1024)
    print(received[0].decode("utf-8"))
    print(received)

socket.close()


