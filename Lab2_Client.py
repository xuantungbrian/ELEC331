from socket import *
from datetime import datetime
from timeit import default_timer as timer
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(10):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message = 'Ping ' + str(i+1) + ' ' + str(current_time)
    clientSocket.settimeout(1)
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    start = timer()
    try:
        response, serverAddress = clientSocket.recvfrom(2048)
        print(response.decode()) 
    except timeout:
        print('Request timed out')
        continue
    end = timer()   
    print('RTT: ',end-start)
    
        
clientSocket.close()


