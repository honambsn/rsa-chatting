# import PySimpleGUI as sg
# import json
#
# # Define the window's contents
# data = "Nam"
# data2 = ["werkhjwe;kjrhek hasdfhq wo;er;wejsj werkhjwe;kjrhek hasdfhq wo;er;wejsj werkhjwe;kjrhek hasdfhq wo;er;wejsj werkhjwe;kjrhek hasdfhq wo;er;wejsj ",
# 		 "432343244444444444444444444444444444444444444444444444444444444444444444448-908240293-48120-39481230480-23842983@!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!."
# 		 "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"]
# def show(data2):
# 	layout = [[sg.Text("What's your name?")],
# 			  [sg.Input(key='-INPUT-')],
# 			  [sg.Text(size=(40,1), key='-OUTPUT-')],
# 			  [sg.Button('Ok'), sg.Button('Quit'), sg.Button('Clear')]]
#
# 	# Create the window
# 	window = sg.Window('Chatting',  layout,size=(640,480))
#
# 	# Display and interact with the Window using an Event Loop
#
# 	while True:
# 		event, values = window.read()
# 		# See if user wants to quit or window was closed
# 		if event == sg.WINDOW_CLOSED or event == 'Quit':
# 			break
# 		if event == 'Clear':
#
# 			print()
# 		# Output a message to the window
# 		#window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI" + data2)
# 		window['-OUTPUT-'].update(data2)
# 	# Finish up by removing from the screen
# 	window.close()
# show(data2[1])



################################################################################################
# from tkinter import *
# class MyWindow():
#     def __init__(self, win, data):
#
#         self.lbl1=Label(win, text='First number')
#         self.lbl2=Label(win, text='Second number')
#         self.lbl3=Label(win, text='Result')
#         self.t1=Entry(bd=3)
#         self.t2=Entry()
#         self.t3= Entry()
#         self.btn1 = Button(win, text='Add')
#         self.lbl1.place(x=100, y=50)
#         self.t1.place(x=200, y=50)
#         self.lbl2.place(x=100, y=100)
#         self.t2.place(x=200, y=100)
#         self.b1=Button(win, text='Add', command=self.add(data))
#         self.b1.place(x=100, y=150)
#         self.lbl3.place(x=100, y=200)
#         self.t3.place(x=200, y=200)
#
#     def add(self, data):
#         self.t3.delete(0, 'end')
#         num1=int(self.t1.get())
#         print(num1)
#
#         num2=int(self.data)
#
#         print(num2)
#         result=num1+num2
#         self.t3.insert(END, str(result))
# window=Tk()
#
# mywin=MyWindow(window,2)
#
# window.title('Hello Python')
# window.geometry("400x300+10+10")
# window.mainloop()

################################################################################################

# # Import the required library
# from tkinter import *
# from tkinter import ttk
#
# # Create an instance of tkinter frame
# win=Tk()
# win.title('Chatting')
#
# # Set the geometry
# win.geometry("700x350")
#
# def get_input():
#    label.config(text=""+text.get(1.0, "end-1c"))
# #
# def get_output():
#    label.config(text="hiiiii")
#
# # Add a text widget
# text=Text(win, width=80, height=15)
# text.insert(END, "")
# text.pack()
#
# # Create a button to get the text input
# b=ttk.Button(win, text="Print", command=get_input)
# b.pack()
#
#
# # Create a Label widget
# label=Label(win, text="", font=('Calibri 15'))
# label.pack()
#
#
# win.mainloop()


################################################################################################
#
# from tkinter import *
#
# # GUI
# root = Tk()
# root.title("Chatting")
#
# BG_GRAY = "#ABB2B9"
# BG_COLOR = "#17202A"
# TEXT_COLOR = "#EAECEE"
#
# FONT = "Helvetica 14"
# FONT_BOLD = "Helvetica 13 bold"
# test_str = "hi"
# # Send function
# def send():
# 	send = "You -> " + e.get()
#
# 	txt.insert(END, "\n" + send)
#
#
# 	user = e.get().lower()
#
#
# 	if (user == "2"):
# 		txt.insert(END, "\n"  +test_str)
#
# 	else:
# 		txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
#
# 	e.delete(0, END)
#
#
# lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
# 	row=0)
#
# txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
# txt.grid(row=1, column=0, columnspan=2)
#
# scrollbar = Scrollbar(txt)
# scrollbar.place(relheight=1, relx=0.974)
#
# e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
# e.grid(row=2, column=0)
#
# send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
# 			command=send).grid(row=2, column=1)
# #
# # root.mainloop()
# from rsa import *
#
# p = rand(1, 1000)
# q = rand(1, 1000)
#
#
#
#
# def generate_keypair_2(p, q, keysize):
#     # keysize is the bit length of n so it must be in range(nMin,nMax+1).
#     # << is bitwise operator
#     # x << y is same as multiplying x by 2**y
#     # p and q values have similar bit-length.
#     # this will generate an n value that's hard to factorize into p and q.
#
#     nMin = 1 << (keysize - 1)
#     nMax = (1 << keysize) - 1
#     primes = [2]
#
#     # we choose two prime numbers in range(start, stop) so that the difference of bit lengths is at most 2.
#     start = 1 << (keysize // 2 - 1)
#     stop = 1 << (keysize // 2 + 1)
#
#     if start >= stop:
#         return []
#     # get prime nums
#     for i in range(3, stop + 1, 2):
#         for p in primes:
#             if i % p == 0:
#                 break
#         else:
#             primes.append(i)
#
#     while (primes and primes[0] < start):
#         del primes[0]
#
#     #choosing p and q from the generated prime numbers.
#     while primes:
#         p = random.choice(primes)
#         primes.remove(p)
#         q_values = [q for q in primes if nMin <= p * q <= nMax]
#         if q_values:
#             q = random.choice(q_values)
#             break
#
#     #get p,q
#     print("print p,q:  " , p, q)
#
#
#     n = p * q
#
#     # get phi(n).Euler function
#     phi = (p - 1) * (q - 1)
#
#     #generate public key 1<e<phi(n)
#     e = random.randrange(1, phi)
#     g = gcd(e, phi)
#
#     while True:
#         #as long as gcd(1,phi(n)) is not 1, keep generating e
#         e = random.randrange(1, phi)
#         g = gcd(e, phi)
#         #generate private key
#         d = mod_inverse(e, phi)
#         if g == 1 and e != d:
#             break
# generate_keypair_2(p,q,2)
# msg = "xin chao"
# print([ord(c) for c in msg])
#
# test_msg = [(ord(c) for c in msg)]
#
# print("test_msg: " , str(test_msg) , type(test_msg))
# print(ord('a'))
# print(chr(97))
#
#
# msg_ciphertext = [pow(ord(c), 3, 2) for c in msg]
# print(type(msg_ciphertext))

from mpmath import *
import decimal

from math import sqrt
#required for the sqrt() function, if you want to avoid doing **0.5
import random
import gmpy2
#required for randrange
from random import randint as rand

#just to use the well known keyword rand() from C++

nMin = 6703903964971298549787012499102923063739682910296196688861780721860882015036773488400937149083451713845015929093243025426876941405973284973216824503042048
nMax = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084095

start = 57896044618658097711785492504343953926634992332820282019728792003956564819968
stop = 231584178474632390847141970017375815706539969331281128078915168015826259279872

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

p = rand(1, 1000)
q = rand(1, 1000)

def min_max(keysize):
    # nMin = decimal.Decimal(1 << (keysize - 1))
    # nMax = decimal.Decimal((1 << keysize) - 1)
    nMin = 1 << (keysize - 1)

    nMax = (1 << keysize) - 1
    return  nMin,nMax


def generate_keypair(p, q, keysize):

    primes = [2]
    # start = 1 << (keysize // 2 - 1)
    # stop = 1 << (keysize // 2 + 1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    while (primes and primes[0] < start):
        del primes[0]

    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break
    print(p, q)
    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randrange(1, phi)
    g = gcd(e, phi)

    while True:
        e = random.randrange(1, phi)
        g = gcd(e, phi)
        #generate private key
        d = mod_inverse(e, phi)
        if g == 1 and e != d:
            break


    return ((e, n), (d, n))


def encrypt(msg_plaintext, package):
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext


def decrypt(msg_ciphertext, package):
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))



def gen_public_private_key():
    bit_length = 512
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private = generate_keypair(
        p, q, 2 ** bit_length)  # 8 is the keysize (bit-length) value.
    print("Public Key: ", public)
    print("Private Key: ", private)
    return public,private



#-------------------------------------------------------------
#driver program
if __name__ == "__main__":
    bit_length = 512
    print("Running RSA...")
    print("Generating public/private keypair...")
    public, private = generate_keypair(
        p, q, 2**bit_length)  # 8 is the keysize (bit-length) value.
    print("Public Key: ", public)
    print("Private Key: ", private)
    msg = input("Write msg: ")
    print([ord(c) for c in msg])
    encrypted_msg = encrypt(msg, public)
    print(encrypted_msg)
    print(type(encrypted_msg))
    print("type of encrypted msg: " , type(encrypted_msg))

    print("Encrypted msg: ")
    print(''.join(map(lambda x: str(x), encrypted_msg))) # print as string
    print(type(public))
    print("Decrypted msg: ")
    print(decrypt(encrypted_msg, private))


    #print(min_max(512))




    # gen_public_private_key()
    #
    # # print("\n")
    # # print(public, private)
    # # mp.dps = 1000
    # keysize = 512
    #
    # #
    # nMin = 1 << (keysize - 1)
    # print(nMin)
    # nMax = (1 << keysize) - 1
    #
    # print(nMax)
    # print("####################################")
    # start = 1 << (keysize // 2 - 1)
    # print(start)
    # stop = 1 << (keysize // 2 + 1)
    # print(stop)

    # precision = 1000
    # decimal.getcontext().prec = precision
    # value = decimal.Decimal((1 << keysize) - 1)
    # print(value)


