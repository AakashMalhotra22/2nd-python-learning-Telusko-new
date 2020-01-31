'''
When you divide a big task into multiple process, and again into small parts, these small parts are called threads.

'''

'''
Examples: You are playing a car race game, then there are many things happening at the same time such as you are driving a car,
your opponents are also there, then other changes also there.
These small small parts are called threads.
#so if you are using octa core cpu, all of the four cores are used and reduce the work load.

That's the use of thread.

You can check the thread in your computer in task manager.
More softwares you run at a time, more thread you will get.

'''

# When you run a code, the code is run by a thread that is the "main thread".

#If you want to execute two codes, you can execute them in by two different threads.
# so there will be three threads
# main thread
# first thread
# second thread

from threading import* # it is required to import threading
from time import * # It is required to use sleep

class hello(Thread):
    def run(self):
      for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):

      for i in range(5):
              print("hi")
              sleep(1)


t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()# This ensures that unless the t1 is completed executed, print("bye") will not excecute.
t2. join() # This ensues that unless the t2 is completed, print("bye") will not execute

print("bye")