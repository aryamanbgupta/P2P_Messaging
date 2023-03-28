import socket

# initialize some sample client details
client_list = {'client1': ('127.0.0.1', 8888), 'client2': ('127.0.0.1', 8889)}

# create a client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to another client
target_client = 'client1' # choose the target client
target_address = client_list[target_client] # get the target client's IP address and port number
client_socket.connect(target_address)

while True:
    #get user message
    msg = input("Message: ")
    # send a message to the target client
    client_socket.send(msg.encode())

    # receive a response from the target client
    response = client_socket.recv(1024).decode()
    print(response)
    if (response=="Disconnect"):
        break
    
# close the socket
client_socket.close()
