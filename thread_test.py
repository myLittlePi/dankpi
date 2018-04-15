import requests
import threading
import time


def lol():
    time.sleep(5)
    print 123

t = threading.Thread(target=lol)
t.start()
print "looool"
print t.is_alive()
t.join()

print "xd"


