import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))

print ('conectado!!\n')


nameFile = str(input('Arquivo> '))

client.send(nameFile.encode())

with open(nameFile, 'wb') as file:
    while 1:
        data = client.recv(100000)
        if not data:
            break
        file.write(data)


print(f"{nameFile} recebido")


