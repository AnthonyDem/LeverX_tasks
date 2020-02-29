from threading import Thread, Lock
import concurrent.futures


class Thread:
    def __init__(self):
        self.a = 0
        self.lock = Lock()

    def function(self, arg):
        for _ in range(arg):
            with self.lock:
                self.a += 1

    def main(self):
        concurrency = 5
        with concurrent.futures.ThreadPoolExecutor(concurrency) as executor:
            for i in range(5):
                executor.submit(self.function, 1000000, ).result()

        print("----------------------", self.a)  # ???


thread = Thread()
thread.main()
