import socket
import sys

client_socket = socket.socket()
hostname = "192.168.100.4"
port = 12345
client_socket.connect((hostname, port))
print('\n===============Geometric Shapes Menu ===============\n')
print("1. Circle")
print ("2. Square")
print ("3. Rectangle")
print ("4. Triangle")
print ("5. Rhombus")
print ("6. Quit") 
print('===================================================== \n')

while True:
    shape_num = input('Please, Select The Option: ')
    print('')
    args = []
    if shape_num == '1':
       args.append(float(input('Enter The Raduis (R): ')))
       data_to_send = ','.join([shape_num] + [str(arg) for arg in args])
       client_socket.send(data_to_send.encode())
       area = client_socket.recv(1024).decode() 
       print('Area Of The Circle = ', area)
       print('')
       print("******************************************************\n")
    elif shape_num == '2':
         args.append(float(input('Enter The Length (L) / Width (W): ')))
         data_to_send = ','.join([shape_num] + [str(arg) for arg in args])
         client_socket.send(data_to_send.encode())
         area = client_socket.recv(1024).decode()
         print('Area Of The Square = ', area)
         print('')
         print("******************************************************\n")
    elif shape_num == '3':
         args.append(float(input('Enter The Length (L): ')))
         args.append(float(input('Enter The Width (W): ')))
         data_to_send = ','.join([shape_num] + [str(arg) for arg in args])
         client_socket.send(data_to_send.encode())
         area = client_socket.recv(1024).decode()
         print('Area Of The Rectangle = ', area)
         print('')
         print("******************************************************\n")
    elif (shape_num == '4'):
         args.append(float(input('Enter The Base (B): ')))
         args.append(float(input('Enter The Height (H): ')))
         data_to_send = ','.join([shape_num] + [str(arg) for arg in args])
         client_socket.send(data_to_send.encode())
         area = client_socket.recv(1024).decode()
         print('Area Of The Triangle = ', area)
         print('')
         print("******************************************************\n")
    elif (shape_num == '5'):
         args.append(float(input('Enter The Large Diameter (D): ')))
         args.append(float(input('Enter The Small Diameter (d): ')))
         data_to_send = ','.join([shape_num] + [str(arg) for arg in args])
         client_socket.send(data_to_send.encode())
         area = client_socket.recv(1024).decode()
         print('Area Of The Rhombus = ', area)  
         print('')
         print("******************************************************\n")
    elif (shape_num == '6'):
         break    
    elif (shape_num != '1', '2', '3', '4', '5', '6'):
         print('Opps!! Invalid option...Please Try Again.')
         print('')
         print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")      
    

print('Closing client connection, goodbye...')
print('')
print("******************************************************\n")
sys.exit()
 


