import time

def count_time_wrapper(func):
    def improved_func(*args,**kwargs):    #接收函数参数
        "统计函数的运行时间"
        start_time = time.time()
        ret = func(*args,**kwargs)        #传入参数并记录返回值
        end_time = time.time()
        print("it takes {} s to find all the soultion".format(end_time-start_time))
        return ret                        #返回未增强函数的返回值
    return improved_func

def count_odds(lim=100):
    "输出0-100之间的所有奇数，并统计函数执行的时间"
    cnt = 0
    for i in range(lim):
        if i % 2 == 1:
            #print(i)
            cnt += 1
    return cnt

if __name__ == "__main__":
    #装饰器等价于在第一次调用函数时执行以下语句
    #装饰前
    print(count_odds(lim=1000))
    #装饰后
    count_odds = count_time_wrapper(count_odds)
    print(count_odds(lim=1000))