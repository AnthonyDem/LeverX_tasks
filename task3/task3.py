from threading import Thread, Lock
import concurrent.futures

lock = Lock()


def function(arg):
    a = 0
    for _ in range(arg):
        lock.acquire()
        a += 1
        lock.release()
    return a


def main():
    concurrency = 5
    a = 0
    with concurrent.futures.ThreadPoolExecutor(concurrency) as executor:
        for _ in range(5):
            thread = executor.submit(function, 1000000)
            a += thread.result()

    print("----------------------", a)  # ???


main()
