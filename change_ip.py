import threading
import socket
import time

host = ''
port = 9000

locaddr = (host,port)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_addr = ('192.168.10.1',8889)

sock.bind(locaddr)
msg = 'command'.encode('utf-8')
sent = sock.sendto(msg,tello_addr)
time.sleep(2)

msg = "ap AIC_2.4 aiclub0000".encode('utf-8')
sent = sock.sendto(msg,tello_addr)
time.sleep(2)	
