import socket
from rsa import *


def gen_public_private_key():
    bit_length = 3
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private = generate_keypair(
        p, q, 2 ** bit_length)  # 8 is the keysize (bit-length) value.
    print("Public Key: ", public)
    print("Private Key: ", private)
    return public,private

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


        key = gen_public_private_key()
        print("----check again: -----\n")
        print("\tpublic key: " + str(key[0]))

        print("\tprivate key: " + str(key[1]))
        private = key[1]

        data = str(key[0])
        conn.send(data.encode())

        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode('utf-8')
            # data = eval(data)
            print(type(data))
            print(data)

            tmp = data.split(",")
            print(tmp)
            print(type(tmp))
            print(len(tmp))
            del tmp[-1]

            for i in range (0, len(tmp)):
                tmp[i] = int(tmp[i])

            print(tmp)
            print(type(tmp))
            print(len(tmp))
            ####################   DECRYPTTTT MESSAGEEEEEE ################

            test_res = decrypt(tmp,private)
            print("decrypted message: ", test_res)



            if not data:
                # if data is not received break
                break

            # res = ''.join(format(ord(i), '08b') for i in str(data))
            # print("test format: "  + res)
            print("User's msg: " + str(data))
            data = "hi" ##input("--> Server's msg:  " )
            conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection
        print("\n\nTrying to connect another client.......")





if __name__ == '__main__':


    server_program()