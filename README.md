# cs361_microservice
microservice for partners project

Communication contract:
1. How to request data from the microservice: First establish a socket connection with the microservice. Next send data to the microservice, the data is sent through the socket connection as a string encoded into bytes. The microservice will handle the data sent to it, and reply back across the socket connection with a string encoded into bytes.

2: How to recieve data from the microservice: When the microservice sends data it will be as a string encoded into bytes. The data will have to be recieved through the socket connection using the socket recv function. Once the encoded data is received it will have to be decoded.

UML diagram of recieving and requesting:


