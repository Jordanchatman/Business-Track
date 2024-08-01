import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))

# Receive the first message from the server
message = client.recv(1024).decode()
# Send a response to the server
client.send(input(message).encode())

# Receive the second message from the server
message = client.recv(1024).decode()
# Send another response to the server
client.send(input(message).encode())

# Print the final message from the server
print(client.recv(1024).decode())
