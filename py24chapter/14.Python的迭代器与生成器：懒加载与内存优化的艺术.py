
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

def count_down_test():
    for num in Countdown(5):
        print(num)  # 输出：5, 4, 3, 2, 1

def chat_bot():
    response = "Hello!"
    while True:
        msg = yield response  # 接收外部传入的值
        response = f"Received: {msg}"

if __name__ == '__main__':
    # 生成1千万数据的平方（内存仅128B）
    # squares_gen = (x ** 2 for x in range(10_000_000))
    # print(next(squares_gen))  # 0
    #
    # # 对比：列表推导占用约900MB内存
    # squares_list = [x ** 2 for x in range(10_000_000)]

    bot = chat_bot()
    next(bot)  # 初始化生成器
    print(bot.send("Hi"))  # 输出：Received: Hi