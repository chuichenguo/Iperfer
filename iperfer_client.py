import socket
import time
message = ""
for i in range(0, 1000):
    message = message + "0"

stop = False
input_data = input()
input_word = input_data.split()
if len(input_word) != 8:
    print("Error: missing or additional arguments")
    stop = True
elif "Iperfer -c -h" not in input_data:
    print("Error: missing or additional arguments")
    stop = True
elif "-t" not in input_data:
    print("Error: missing or additional arguments")
    stop = True
elif "-p" not in input_data:
    print("Error: missing or additional arguments")
    stop = True
elif int(input_word[5]) < 1024 or int(input_word[5]) > 65535:
    print("Error: port number must be in the range 1024 to 65535")
    stop = True


if(stop == False):
    SERVER = input_word[3]
    PORT = int(input_word[5])
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    print("This is client.")
    counter = 0
    start_time = time.time()
    timeout = time.time() + int(input_word[7])
    while True:
        if time.time() > timeout:
            end_time = time.time()
            client.sendall(bytes("bye", 'UTF-8'))
            bandwidth = (1000*8*counter) / (int(end_time-start_time)*1000*1000)
            print("sent=", counter, " KB ", "rate=", bandwidth, " Mbps")
            break

        in_data = client.recv(1024)
        print("From Server :", in_data.decode())
        client.sendall(bytes(message, 'UTF-8'))
        counter = counter + 1

    # client.close()
