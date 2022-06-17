import threading

def link():
    for x in range(10):
        print("hello")
def link2():
    for x in range(10):        
        print("salom")

t1 = threading.Thread(target=link)
t2 = threading.Thread(target=link2)

t1.start()
t2.start()
