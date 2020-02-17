from threading import Thread, Lock


a = 0


def function(arg):
    global a
    lock = Lock()
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()


def main():
    for _ in range(5):
        thread = Thread(target=function, args=(1000000,))
        thread.start()
        thread.join()

    print("----------------------", a)  # ???


main()
