from multiprocessing import Process
import time

def func1():
    while True:
        print('Holaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        time.sleep(10)

def func2():
    while True:
        print('Adios')
        time.sleep(5)

def main():
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    main()