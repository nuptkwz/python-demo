

def type_converter(value, target_type):
    def safe_convert_to_int(v):
        """处理科学计数法、浮点字符串等复杂情况"""
        try:
            # 先尝试直接转换整数字符串或整数
            return int(v)
        except (ValueError, TypeError):
            try:
                # 处理浮点字符串或科学计数法（如"1e3"）
                return int(float(v))
            except (ValueError, TypeError):
                raise  # 抛出异常给外层捕获

    converters = {
        "int": safe_convert_to_int,
        "float": float,
        "str": str,
        "bool": lambda v: v.lower() in ("true", "1", "yes", "on")
                          if isinstance(v, str)
                          else bool(v) and v not in (0, False)
    }

    if target_type not in converters:
        return f"转换失败: 不支持的目标类型{target_type}"

    try:
        return converters[target_type](value)
    except (ValueError, TypeError):
        return f"转换失败: {value}→{target_type}"


def convert_nested(data, target_type):
    if isinstance(data, (list, tuple)):
        return [convert_nested(item, target_type) for item in data]
    return type_converter(data, target_type)



if __name__ == '__main__':
    print(convert_nested(["1", "2.5", True], "float"))
    # 输出 [1.0, 2.5, 1.0]
    # # 测试用例
    # # 测试用例
    # print(type_converter("3.14", "int"))  # 3
    # print(type_converter("1e3", "int"))  # 1000（修复科学计数法问题）
    # print(type_converter(0, "bool"))  # False
    # print(type_converter("True", "bool"))  # True
    # print(type_converter("yes", "bool"))  # True（新增支持值）}"

    # s = "Python"
    # print(id(s))  # 地址1
    # s += "3.8"  # 新建字符串
    # print(id(s))  # 新地址

    # print(bool(""))  # True（非空字符串均为真）
    #
    # print(int(2.999))  # 输出2（非四舍五入）
    #
    # print(10 + 3.14)  # int→float，输出13.14
    # if "non-empty":  # str→bool，自动转为True
    #     print("执行")
