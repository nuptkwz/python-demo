import math
import matplotlib.pyplot as plt
import time


def prime_sieve(limit):
    """埃拉托色尼筛法生成素数"""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    primes = []

    for num in range(2, int(math.sqrt(limit)) + 1):
        if sieve[num]:
            primes.append(num)
            sieve[num * num:: num] = [False] * len(sieve[num * num:: num])

    return primes + [i for i in range(int(math.sqrt(limit)) + 1, limit + 1) if sieve[i]]


def is_prime_optimized(n):
    """优化版素数检测"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # 只检查奇数因子
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


# 性能对比测试
def performance_test():
    """不同算法的性能比较"""
    sizes = [10, 100, 1000, 10000, 50000]
    sieve_times = []
    optimized_times = []

    for size in sizes:
        # 筛法测试
        start = time.time()
        primes_sieve = prime_sieve(size)
        sieve_times.append(time.time() - start)

        # 单个检测测试
        start = time.time()
        primes_opt = [i for i in range(2, size + 1) if is_prime_optimized(i)]
        optimized_times.append(time.time() - start)

        # 验证结果一致
        assert primes_sieve == primes_opt, f"算法不一致 @ size={size}"

    return sizes, sieve_times, optimized_times


# 可视化性能对比
def plot_performance(sizes, times1, times2):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times1, 'o-', label='筛法生成素数')
    plt.plot(sizes, times2, 's-', label='单个优化检测')
    plt.xlabel('计算范围')
    plt.ylabel('耗时(秒)')
    plt.title('素数计算算法性能对比')
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(True)
    plt.legend()
    plt.savefig('prime_performance.png')
    plt.show()


# 查找范围内的孪生素数
def find_twin_primes(limit):
    """查找孪生素数对(如(3,5), (11,13))"""
    primes = prime_sieve(limit)
    twins = []
    for i in range(1, len(primes)):
        if primes[i] - primes[i - 1] == 2:
            twins.append((primes[i - 1], primes[i]))
    return twins
def discount_sys():
    # 用户折扣系统
    age = int(input("请输入年龄: "))
    is_member = input("是否是会员(y/n): ").lower() == 'y'

    if age <= 12:
        discount = 0.5  # 儿童半价
    elif age >= 65:
        discount = 0.7  # 老人7折
    elif is_member:
        discount = 0.8  # 会员8折
    else:
        discount = 1.0  # 无折扣

    print(f"您的最终折扣为: {discount * 10}折")

    # 单行条件表达式(三元运算符)
    result = "特价商品" if discount < 1.0 else "全价商品"

def seat_type():
    # 航班座位分配系统 - 避免多层嵌套
    seat_type = input("座位类型(头等舱/商务舱/经济舱): ")
    has_child = input("是否有随行儿童(y/n): ") == 'y'
    is_vip = input("是否是VIP客户(y/n): ") == 'y'

    # 使用组合条件代替嵌套
    if seat_type == "头等舱" or is_vip:
        service = "专属贵宾室"
    elif seat_type == "商务舱" and has_child:
        service = "儿童娱乐包"
    else:
        service = "标准服务"

    print(f"您享受的服务: {service}")


if __name__ == '__main__':
    # 筛选1000以内的素数
    primes_1000 = prime_sieve(1000)
    print(f"1000以内的素数有 {len(primes_1000)} 个")
    print(f"前10个素数: {primes_1000[:10]}")

    # 找孪生素数
    twins = find_twin_primes(1000)
    print(f"\n1000内找到 {len(twins)} 对孪生素数")
    print(f"前5对: {twins[:5]}")

    # 性能测试与可视化
    sizes, sieve_times, optimized_times = performance_test()
    plot_performance(sizes, sieve_times, optimized_times)