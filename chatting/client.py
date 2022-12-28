import socket
from rsa import *
import os

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

    server_public_key = data


    print(type(data))
    res = format_key(server_public_key)

    n = int(res[0])
    e = int(res[1])
    server_public_key = n,e

    print(server_public_key)
    print(type(server_public_key))



    # gen client's key
    client_key = gen_public_private_key()
    print("\t----check server's key again: -----\n")
    print("\tpublic key: " + str(client_key[0]))
    print("\tprivate key: " + str(client_key[1]))
    private_key = client_key[1]


    message = str(client_key[0]) # input
    client_socket.send(message.encode())
    print("client's key sent")

    message = ("START!!!")

    os.system('cls')

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode() # receive response

        print("Raw data receive from server: " + data)  # show in terminal

        tmp = data.split(",")
        del tmp[-1]
        for i in range(0, len(tmp)):
            tmp[i] = int(tmp[i])

        test_res = decrypt(tmp, private_key)

        print("\t==>decrypted server's message: ", test_res)
        message = input("-->User's msg: ")  # again take input

        ####################   ENCRYPTTTT client's MESSAGEEEEEE ################
        encrypted_msg = encrypt(message, server_public_key)
        message = encrypted_msg
        print("encrypt msg: ", message)

        print("Message's length: ", len(message))
        tmp = ""
        for i in range (0, len(message)):
            tmp = tmp + str(message[i]) + ","
            i = i+1

        message = tmp

        # message = tmp
    client_socket.close()  # close the connection



if __name__ == '__main__':
    client_program()