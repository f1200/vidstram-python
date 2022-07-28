from vidstream import StreamingServer
import threading
BaronServ=StreamingServer('192.168.0.105',7777)
T=threading.Thread(target=BaronServ.start_server)
T.start()
while input("enter  :") != 'stop':
    continue
else:
    BaronServ.stop_server()