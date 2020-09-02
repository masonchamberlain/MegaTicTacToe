import time, socket, sys
import files.board

print('Client Server...')
time.sleep(1)

# Get the hostname, IP Address from socket and set Port
soc = socket.socket()
shost = socket.gethostname()
ip = socket.gethostbyname(shost)

# get information to connect with the server
print(shost, '({})'.format(ip))
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
port = 1234

print('Trying to connect to the server: {}, ({})'.format(server_host, port))
time.sleep(1)
soc.connect((server_host, port))
print("Connected...\n")

soc.send(name.encode())
server_name = soc.recv(1024)
server_name = server_name.decode()
print('{} has joined...'.format(server_name))
print('Enter [bye] to exit.')

game = files.board
game.setPlayerTwo(name)
game.setPlayerOne(server_name)
message = soc.recv(1024)
message = message.decode()
size = int(message)
print(message)
print(size)
game.size = size
game.setBoard(size)
game.currentPlayer = 2
print(game.instructions())
print("Please wait for host to begin..")

while True:
    message = soc.recv(1024)
    message = message.decode()
    game.updateBoard(message)
    soc.send(game.boardToString().encode())