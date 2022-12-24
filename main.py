import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(3)
print("Working...")
client_socket, address = server.accept() 
data = client_socket.recv(2048).decode('utf-8')
print(data)
# hdrs = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
content = 'Good work'.encode('utf-8')
client_socket.send(content)
print('The end')