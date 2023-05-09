# Name: Sam Miller
# CS 361 assignment 8
# citation: modified the Hello World tutorial from https://zguide.zeromq.org/docs/chapter1/

import json
import requests
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    message = socket.recv()
    message = message.decode()
    print(f"Received request: \'{message}\'")

    # if the client is requesting a new deck, initiate a new deck
    if message == "new deck":
        deck = requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
        deck_text = json.loads(deck.text)
        deck_id = deck_text['deck_id']

    # shuffle the cards and check the remaining amount
    shuffle = requests.get("https://deckofcardsapi.com/api/deck/" + deck_id + "/shuffle/?remaining=true")
    shuffle_text = json.loads(shuffle.text)
    remaining = shuffle_text['remaining']
    print("Remaining cards: " + str(remaining))

    # microservice calls the api to draw a card only if cards are remaining in the deck
    if remaining > 0:
        card = requests.get("https://deckofcardsapi.com/api/deck/" + deck_id + "/draw/?count=1")
        card_text = json.loads(card.text)
        card_code = card_text['cards'][0]['code']
    else:
        card_code = "empty deck!"

    #  Send reply to client
    print(f"Sending Response: \'{card_code}\'")
    socket.send_string(card_code)
