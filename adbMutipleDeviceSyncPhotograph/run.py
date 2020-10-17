from ppadb.client import Client as AdbClient
from threading import Thread, Event
import time

# 拍照延时
TIME_INTERVAL = 2


# Default is "127.0.0.1" and 5037
client = AdbClient(host="127.0.0.1", port=5037)

class Phone(Thread):
    def __init__(self, device):
        super().__init__()
        self.device = device
        self.event = Event()
        self.event.clear()
    
    def run(self):
        self.device.shell('am start -a android.media.action.STILL_IMAGE_CAMERA')
        print('Device %s: open camera' % (self.device.serial))
        while True:
            self.event.wait()
            self.device.shell('input keyevent 27')
            self.event.clear()
            print('Device %s: take a photo' % (self.device.serial))

    def action(self):
        self.event.set()


if __name__=='__main__':
    T=[]
    for device in client.devices():
        t = Phone(device)
        t.start()
        T.append(t)
    
    i=0
    while True:
        i+=1
        for t in T:
            t.action()
        print('第 %s 次拍照'%(i))
        time.sleep(TIME_INTERVAL)
    
    for t in T:
        t.join()