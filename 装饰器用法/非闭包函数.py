import time


def count_time(func):
    "统计函数的运行时间"
    start_time = time.time()
    func()
    end_time = time.time()
    print("it takes {} s to find all the soultion".format(end_time-start_time))

def print_odds():
    "输出0-100之间的所有奇数，并统计函数执行的时间"
    for i in range(100):
        if i % 2 == 1:
            print(i)

if __name__ == "__main__":
    count_time(print_odds)
