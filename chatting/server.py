import socket
from rsa import *
from client import *
import os

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 2000  # initiate port no above 1024
    while True:
        server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
        server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))

        # generate server's keys
        server_key = gen_public_private_key()
        print("\t----check server's key again: -----\n")
        print("\tpublic key: " + str(server_key[0]))
        print("\tprivate key: " + str(server_key[1]))
        private_key = server_key[1]

        # send server's public key to client
        data = str(server_key[0])
        conn.send(data.encode())

        # get client's public key
        data = conn.recv(1024).decode('utf-8')
        print("client's key received: ", data)

        # format to get client's public key
        client_public_key = data

        print(type(data))
        res = format_key(client_public_key)

        n = int(res[0])
        e = int(res[1])
        client_public_key = n, e

        print(client_public_key)
        print(type(client_public_key))
        os.system('cls')
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode('utf-8')
            # data = eval(data)
            print(type(data))
            print("\t==>Raw data receive from client: ", data)

            tmp = data.split(",")
            # print(tmp)
            # print(type(tmp))
            # print(len(tmp))
            del tmp[-1]

            for i in range(0, len(tmp)):
                tmp[i] = int(tmp[i])

            # print(tmp)
            # print(type(tmp))
            # print(len(tmp))

            if not data:
                # if data is not received break
                break


            print("Client's msg: " + str(data))

            ####################   DECRYPTTTT client's MESSAGEEEEEE ################
            test_res = decrypt(tmp, private_key)

            print("\t==>decrypted client's message: ", test_res)


            data = input("--> Server's msg:  " )
            ####################   ENCRYPTTTT server's MESSAGEEEEEE ################
            encrypted_msg = encrypt(data, client_public_key)
            data = encrypted_msg
            print("encrypt msg: ", data)

            print("Message's length: ", len(data))
            tmp = ""
            for i in range(0, len(data)):
                tmp = tmp + str(data[i]) + ","
                i = i + 1

            data = tmp

            conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection
        print("\n\nTrying to connect another client.......")


if __name__ == '__main__':
    server_program()
