from socket import socket, AF_INET, SOCK_STREAM
from ssl import SSLContext, PROTOCOL_TLS_SERVER


ip = '192.168.1.10'
port = 3000
context = SSLContext(PROTOCOL_TLS_SERVER)
context.load_cert_chain('cert.pem', 'key.pem')

with socket(AF_INET, SOCK_STREAM) as server:
    server.bind((ip, port))
    server.listen(1)
    with context.wrap_socket(server, server_side=True) as tls:
        connection, address = tls.accept()
        print(f'Connected by {address}\n')
        
        while True:
            data = connection.recv(1024)
            str_d = data.decode("utf8")
            if str_d =="quit":
                break
            print("Client: "+str_d)
            m = input("Servre: ")
            connection.sendall(bytes(m,"utf8"))
            if m == "quit":
                break
       
