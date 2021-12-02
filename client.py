from socket import create_connection
from ssl import SSLContext, PROTOCOL_TLS_CLIENT


hostname='example.org'
ip = '192.168.1.10'
port = 3000
context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')

with create_connection((ip, port)) as client:
    with context.wrap_socket(client, server_hostname=hostname) as tls:
        print(f'Using {tls.version()}\n')
        while True:
            m = input('Client: ')
            tls.sendall(bytes(m,"utf8"))
            if m == "quit":
                break
            data = tls.recv(1024)
            if (data.decode("utf8"))=="quit":
                break
            print('Server: ',data.decode("utf8"))
