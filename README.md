# Iperfer
Excuting like Iperf.

## Open two powershell
1. server

Iperfer -s -p <listen port>

Iperfer -s -p 8080

2. client

Iperfer -c -h <server hostname> -p <server port> -t <time> 

Iperfer -c -h 127.0.0.1 -p 8080 -t 2
