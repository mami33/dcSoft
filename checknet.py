import socket
import time
global err_connection


err_connection = False
def checknet():

    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect(("8.8.8.8",53))
        return True
    except socket.error as ex:
        print(ex)
        return False

i = 0
while not checknet():

    time.sleep(1)
    i += 1
    if i == 5:
        err_connection = True
        break


