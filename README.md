# Deck of Cards API Microservice 

## requesting data from the microservice:
<p>To request data from the microservice a string is passed. It is currently configured to accept either 'new card' or 'new deck'. If it receives the message 'new deck' a new deck is created and then a card is drawn. With 'new card' it is assumed that a deck has already been created, and instead a card is drawn. The API will select a card at random and return that card code to the user (for example '2H' would be the 2 of hearts). If there are no remaining cards in the deck, a custom message 'empty deck!' is sent back to the client in lieu of a card code. </p>
<p> The application uses ZMQ to send and receive data. In order to request data a socket needs to be instantiated and a port connection needs to be made. A basic request syntactically appears as so:</p>
      <p>import zmq</p>
      <p>context = zmq.Context()</p>
      <p>socket = context.socket(zmq.REQ)</p>
      <p>socket.connect("tcp://localhost:5555")</p>
      <p>socket.send_string('new deck')</p>
      
## receiving data from the microservice:
<p>To receive data you first need to have made a request through a connected socket. Once that request has been made, the card code data can be received like so:</p>
      <p>message = socket.recv()</p>
<p>Where message is a variable holding the byte type data. Since byte type data is a bit clunky, it is recommended to use .decode() on byte type data variables to be more useful in a Python context:</p>
      <p>message = message.decode()</p>

