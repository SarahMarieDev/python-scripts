import socket

# Start a socket object using IPv4 properties and TCP protocol
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind to our local computer on IP 0.0.0.0, port 1337
sock.bind(("0.0.0.0", 1337))
# Start listening with a backlog size of 10
sock.listen(10)