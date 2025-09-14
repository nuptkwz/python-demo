import utils.calculator as calc  # 别名避免冲突

# 电商折扣计算器（综合参数类型）
def apply_discount(price: float, discount=0.1, *tax_rates, **coupons):
    """
    :param price: 基础价格（位置参数）
    :param discount: 默认折扣（默认参数）
    :param tax_rates: 可变税率（元组）
    :param coupons: 优惠券字典（键值对）
    """
    final_price = price * (1 - discount)
    for tax in tax_rates:  # 累加税率
        final_price *= (1 + tax)
    for coupon_name, value in coupons.items():  # 应用优惠券
        final_price -= value
    return max(final_price, 0)  # 防止负价格


if __name__ == '__main__':
    # 1.调用示例
    # print(apply_discount(100, 0.2, 0.05, 0.03, VIP=10, NEWUSER=5))
    # 2.
    # ✅ 安全导入（推荐）

    result = calc.add(3, 5)

    # ⚠️ 风险导入（污染命名空间）

    # 🔄 动态导入（插件系统）
    module_name = "utils.logger"
    log_module = __import__(module_name)
    log_module.log_error("System error!")