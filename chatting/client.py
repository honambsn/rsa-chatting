import socket
from rsa import *
def format_key(x):
    raw = x.replace("(" , "")
    raw = raw.replace(")","")
    raw= raw.split(",")

    print("raw: ",raw)
    # print(raw[0])
    # print(raw[1])
    return raw

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 2000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    data = client_socket.recv(1024).decode()
    print("Server's public key: " + data)  # show in terminal

    public_key = data


    print(type(data))
    res = format_key(public_key)

    n = int(res[0])
    e = int(res[1])
    public_key = n,e

    print(public_key)
    print(type(public_key))



    message = input("-->User's msg: ") # input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode() # receive response

        print("Server's msg: " + data)  # show in terminal

        message = input("-->User's msg: ")  # again take input

        ####################   ENCRYPTTTT MESSAGEEEEEE ################
        encrypted_msg = encrypt(message, public_key)
        message = encrypted_msg
        # #message = ''.join(map(lambda x: str(x), encrypted_msg))
        print("encrypt msg: ", message)
        #message = ''.join(map(lambda x: str(x), encrypted_msg))
        print(len(message))
        tmp = ""
        for i in range (0, len(message)):
            tmp = tmp + str(message[i]) + ","
            i = i+1

        message = tmp

        # message = tmp
    client_socket.close()  # close the connection



if __name__ == '__main__':
    client_program()