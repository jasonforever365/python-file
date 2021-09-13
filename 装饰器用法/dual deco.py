def wrapper1(func1):
    print('set func1')		# 在wrapper1装饰函数时输出
    def improved_func1():
        print('call func1')	# 在wrapper1装饰过的函数被调用时输出
        func1()
    return improved_func1

def wrapper2(func2):
    print('set func2')  	# 在wrapper2装饰函数时被输出
    def improved_func2():
        print('call func2')	# 在wrapper2装饰过的函数被调用时输出
        func2()
    return improved_func2

@wrapper1
@wrapper2
def original_func():
    pass

if __name__ == '__main__':
    #程序运行的顺序：original_func = wrapper1(wrapper2(original_func))
    original_func()
    print('-----')
    original_func()
