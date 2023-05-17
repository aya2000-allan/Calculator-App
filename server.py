import socket

server_socket = socket.socket() 
hostname = "192.168.100.4" 
port = 12345
server_socket.bind((hostname, port))
server_socket.listen(1)
print("Welcome, Server is started!!")
print("Waiting for client request..")
client_socket, address = server_socket.accept()
print('Connected to client', address)
def calc_area(shape, *args):

    if   shape == '1':
         area = 3.14 * (args[0] ** 2)
         return area
    elif shape == '2':
         area = args[0] ** 2
         return area
    elif shape == '3':
         area = args[0] * args[1]
         return area
    elif shape == '4':
         area = 0.5 * args[0] * args[1]
         return area
    elif shape == '5':
         area = args[0] * args[1]
         return area 
          
while True:  
      try:       
         data_from_client = client_socket.recv(1024).decode()
         data_from_client = data_from_client.split(',')
         shape_num = data_from_client[0] 
         args = [float(arg) for arg in data_from_client[1:]]
         area = calc_area(shape_num, *args)
         client_socket.send(str(area).encode())
      except:
          break
 
print ('Connection Closed')
client_socket.close() 
