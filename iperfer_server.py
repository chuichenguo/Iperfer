import socket
import threading
import time


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.clientsocket = clientsocket
        print("New connection added: ", clientAddress)

    def run(self):
        print("Connection from : ", clientAddress)
        self.clientsocket.send(bytes("Hi, This is from Server.", 'utf-8'))
        counter = 0
        start_time = time.time()
        while True:
            msg = ""
            data = self.clientsocket.recv(1000)
            msg = data.decode()
            if msg == "bye":
                end_time = time.time()
                bandwidth = (1000*8*counter) / \
                    (int(end_time-start_time)*1000*1000)
                print("sent=", counter, " KB ", "rate=", bandwidth, " Mbps")
                break
            else:
                print("From Client : ", msg)
                self.clientsocket.send(bytes(msg, 'UTF-8'))
                counter = counter + 1
        print("Client at ", clientAddress, " disconnected...")


stop = False
input_data = input()
input_word = input_data.split()
if len(input_word) != 4:
    print("Error: missing or additional arguments")
    stop = True
elif "Iperfer -s -p" not in input_data:
    print("Error: missing or additional arguments")
    stop = True
elif int(input_word[3]) < 1024 or int(input_word[3]) > 65535:
    print("Error: port number must be in the range 1024 to 65535")
    stop = True

if stop == False:
    LOCALHOST = "127.0.0.1"
    PORT = int(input_word[3])
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((LOCALHOST, PORT))
    print("Server started")
    print("Waiting for client request.")
    # while True:
    # The Iperfer server s hould shut down after it handles one connection from a client.
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
