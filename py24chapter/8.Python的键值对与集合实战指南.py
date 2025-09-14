


def fun_1():
    # 创建字典的三种方式
    user = {'name': 'Alice', 'age': 30, 'city': 'Paris'}  # 直接创建
    user = dict(name='Bob', age=25)  # dict构造函数
    user = dict([('name', 'Charlie'), ('age', 28)])  # 键值对元组

    # 键的唯一性验证
    data = {1: 'one', '1': 'ONE', 1.0: 'ONE'}  # 输出 {1: 'ONE'} - 整数1和浮点数1.0被视为相同键



if __name__ == '__main__':
    import json

    # 字典转JSON
    profile = {
        "user_id": 153,
        "preferences": {"theme": "dark", "language": "zh_CN"},
        "tags": ["python", "backend"]
    }
    json_data = json.dumps(profile, indent=2)
    print("Serialized JSON:\n", json_data)

    # JSON转字典
    loaded_data = json.loads(json_data)
    print("\nDeserialized dictionary:")
    print(f"User ID: {loaded_data['user_id']}, Theme: {loaded_data['preferences']['theme']}")