import time
from functools import wraps
def timer(func):
    @wraps(func)  # 保留原函数元信息（如__name__）
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)  # 执行原函数
        end = time.perf_counter()
        print(f"{func.__name__} 耗时: {end - start:.4f}秒")
        return result

    return wrapper


@timer
def data_processing(n):
    """模拟数据处理函数"""
    time.sleep(n)
    return "处理完成"

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 调用 {func.__name__}，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} 返回: {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

class Singleton:
    def __init__(self,cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.cls(*args, **kwargs)
            return self.instance

if __name__ == '__main__':
    # @time 语法糖
    print(data_processing(2))  # 输出执行时间 + "处理完成"
    add(1, 2)