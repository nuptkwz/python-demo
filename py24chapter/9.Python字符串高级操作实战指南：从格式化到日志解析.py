def f_string():
    name = "Alice"
    age = 25
    # 变量嵌入与运算
    print(f"{name}今年{age}岁，明年{age + 1}岁")  # Alice今年25岁，明年26岁
    print(f"名字长度：{len(name)}")  # 名字长度：5


def f_string_format_num():
    # 数字格式化（千分位、小数位、百分比）
    price = 1234567.8912
    print(f"总价：{price:,.2f}元")  # 总价：1,234,567.89元
    print(f"占比：{0.257:.2%}")  # 占比：25.70%

    # 文本对齐与填充
    text = "Python"
    print(f"|{text:_^15}|")  # |_____Python_____|


def f_equal():
    # 输出变量名及值
    x = 100
    print(f"{x=}")  # x=100


def format_match():
    import re

    text = "2023-08-15 Error: Disk full"

    # match：从起始位置匹配
    print(re.match(r"\d{4}-\d{2}-\d{2}", text))  # 匹配成功（返回Match对象）
    print(re.match(r"Error", text))  # 匹配失败（返回None）

    # search：扫描整个字符串
    print(re.search(r"Error", text))  # 匹配成功


def match_log():
    import re
    log = "2025-07-27 14:30 [WARN] Connection timeout"
    pattern = r"(?P<date>\d{4}-\d{2}-\d{2}) \d{2}:\d{2} \[(?P<level>\w+)\] (?P<msg>.+)"
    match = re.search(pattern, log)
    if match:
        print(f"日期：{match.group('date')}, 级别：{match.group('level')}, 信息：{match.group('msg')}")
        # 输出：日期：2025-07-27, 级别：WARN, 信息：Connection timeout

def en_code():
    # 编码与解码
    text = "你好，世界"
    utf8_bytes = text.encode("utf-8")  # b'\xe4\xbd\xa0\xe5\xa5\xbd...'
    gbk_bytes = text.encode("gbk")  # b'\xc4\xe3\xba\xc3...'

    # 错误处理（忽略无法解码的字符）
    try:
        decoded = gbk_bytes.decode("gbk", errors="ignore")  # 避免崩溃
        print(f"gbk_bytes.decode:{decoded}")
    except UnicodeDecodeError:
        print("解码失败！建议统一编码")

def write_read_log():
    # 读写文件时显式指定编码
    with open("log.txt", "w", encoding="utf-8") as f:  # 统一使用UTF-8
        f.write("日志内容...")

    with open("log.txt", "r", encoding="utf-8") as f:
        content = f.read()  # 无乱码风险
        print(content)

if __name__ == '__main__':
    import re
    from collections import defaultdict
    def log_parser(file_path):
        pattern = (
            r"(?P<date>\d{4}-\d{2}-\d{2}) "
            r"(?P<time>\d{2}:\d{2}) "
            r"\[(?P<level>\w+)\] "
            r"(?P<message>.+)"
        )
        stats = defaultdict(int)

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                match = re.match(pattern, line)
                if match:
                    level = match.group("level")
                    stats[level] += 1
                    # 生成格式化报告（f-string对齐）
                    print(
                        f"{match.group('date'):<10} "
                        f"{match.group('time'):<6} "
                        f"[{level}] "
                        f"{match.group('message')}"
                    )
                else:
                    print(f"无法解析: {line}")  # 记录无效行

        # 输出统计报告
        print("\n===== 日志统计 =====")
        for level, count in stats.items():
            print(f"{level}级别日志: {count}条")

    # 测试
    log_parser("system.log")
