# Name: Sam Miller
# CS 361 assignment 8
# citation: modified the Hello World tutorial from https://zguide.zeromq.org/docs/chapter1/

import zmq

context = zmq.Context()
#  Socket to talk to server
print("\n\n\nConnecting to deck microservice...\n")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for deck in range(2):
    card_list = []
    send_message = "new deck"
    print(f"1. \'{send_message}\' requested...")
    socket.send_string(send_message)
    #  Get the reply.
    message = socket.recv()
    message = message.decode()
    print(f"Received reply: \'{message}\'")
    card_list.append(message)

    for i in range(2, 55):
        send_message = "new card"
        print(f"" + str(i) + f". \'{send_message}\' requested...")
        socket.send_string(send_message)
        #  Get the reply.
        message = socket.recv()
        message = message.decode()
        print(f"Received reply: \'{message}\'")
        if message != 'empty deck!':
            card_list.append(message)

    card_list.sort()
    print("\nList of cards: ")
    for i in range(0, len(card_list), 4):
        print((card_list[i:i+4]))
    print("Length of card list: " + str(len(card_list)) + "\n\n")