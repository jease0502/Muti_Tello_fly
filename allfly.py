import socket
import threading
import time
import sys

host = ''
port = 9000
locaddr = (host,port)

# Tello的IP和接口
tello_address1 = ('192.168.0.122', 8889)
tello_address2 = ('192.168.0.121', 8889)
tello_address3 = ('192.168.0.165', 8889)
tello_address4 = ('192.168.0.148', 8889)

# 创建一个接收用户指令的UDP连接
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(locaddr)

# 定义send命令，发送send里面的指令给Telo无人机
def send(message, delay,tello):
  try:
    sock.sendto(message.encode(), tello)
    print("Sending message: " + message)
  except Exception as e:
    print("Error sending: " + str(e))
  time.sleep(delay)
# 定义receive命令，循环接收来自Tello的信息
def receive():
  while True:
    try:
      response, ip_address = sock.recvfrom(128)
      print("Received message: " + response.decode(encoding='utf-8'))
    except Exception as e:
      sock.close()
      print("Error receiving: " + str(e))
      break
      
# 开始一个监听线程，利用receive命令持续监控无人机发回的信号
receiveThread = threading.Thread(target=receive)
receiveThread.daemon = True
receiveThread.start()

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        try:
            message = input(">> ")
            if(message != "exit"):
                # 发送命令
                send(message, 0.5, tello_address1)
                send(message, 0.5, tello_address2)
                send(message, 0.5, tello_address3)
                send(message, 0.5, tello_address4)
            else:
                break
        except KeyboardInterrupt:
            print("Interrupt received, stopping...")
            break

# send("command", 3,tello_address1)
# send("takeoff", 5,tello_address1)
# send("land", 1,tello_address1)

# time.sleep(5)
# Print message
print("飛行完成")
sock.close()