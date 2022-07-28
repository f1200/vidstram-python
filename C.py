from vidstream import ScreenShareClient
import threading
BaronServ=ScreenShareClient('192.168.0.105',7777)
T=threading.Thread(target=BaronServ.start_stream)
T.start()
while input("enter  :") != 'stop':
    continue
else:
    BaronServ.stop_stream()