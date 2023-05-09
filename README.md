# Deck of Cards API Microservice 

# requesting data from the microservice:
<p>To request data from the microservice a string is passed. It is currently configured to accept either 'new card' or 'new deck'. If it receives the message 'new deck' a new deck is created and then a card is drawn. With 'new card' it is assumed that a deck has already been created, and instead a card is drawn. The API will select a card at random and return that card code to the user (for example '2H' would be the 2 of hearts). If there are no remaining cards in the deck, a custom message 'empty deck!' is sent back to the client in lieu of a card code. </p>
<p> The application uses ZMQ to send and receive data. 

