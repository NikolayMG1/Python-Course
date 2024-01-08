from threading import Thread
from time import sleep

def delayed_hi():
    sleep(1)
    print("I'm a thread")

t1 = Thread(target=delayed_hi)
t1.start()

print("The thread has started")
print("I want to wait for it to end")
# t1.join()  # Comment this, to see the change
print("The thread has finished")