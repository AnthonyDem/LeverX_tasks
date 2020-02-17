from threading import Thread, Lock
import concurrent.futures

a = 0
lock = Lock()


def function(arg):
    global a
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()


def main():
    concurrency = 5
    with concurrent.futures.ThreadPoolExecutor(concurrency) as executor:
        thread1 = executor.submit(function, 1000000)
        thread2 = executor.submit(function, 1000000)
        thread3 = executor.submit(function, 1000000)
        thread4 = executor.submit(function, 1000000)
        thread5 = executor.submit(function, 1000000)


    print("----------------------", a)  # ???


main()
