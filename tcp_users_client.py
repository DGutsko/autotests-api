import socket

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = "Привет, сервер!"
    client_socket.send(message.encode())

    response = client_socket.recv(1024).decode()
    print("Ответ от сервера:")
    print(response)

    client_socket.close()

if __name__ == '__main__':
    client()