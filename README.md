# cs361_microservice
microservice for partners project

Communication contract:
1. How to request data from the microservice: First establish a socket connection with the microservice. The connection is a Localhost connection on port 1237. Next send data to the microservice, the data is sent through the socket connection as a string encoded into bytes. The microservice will handle the data sent to it, and reply back across the socket connection with a string encoded into bytes.

2: How to recieve data from the microservice: When the microservice sends data it will be as a string encoded into bytes. The data will have to be recieved through the socket connection using the socket recv function. Once the encoded data is received it will have to be decoded  from bytes.

UML diagram of recieving and requesting:
![image](https://user-images.githubusercontent.com/97048406/198756415-b81f220e-c523-46e4-8bcf-ec335a6d5e74.png)


