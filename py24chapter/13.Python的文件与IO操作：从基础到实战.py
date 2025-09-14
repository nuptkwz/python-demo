
def write_pic():
    # 文本文件读写（自动处理编码）
    with open('demo.txt', 'w', encoding='utf-8') as f:  # 写模式
        f.write("Hello,世界\n第二行内容")

    with open('demo.txt', 'r') as f:  # 读模式
        print(f.read())  # 输出整个文件内容

    # 二进制文件读写（图片/音视频）
    with open('image.jpg', 'rb') as f:  # 二进制读
        data = f.read()

    with open('copy.jpg', 'wb') as f:  # 二进制写
        f.write(data)  # 复制图片文件

def read_csv_data():
    import csv
    # 写入CSV
    with open('data.csv', 'w', newline='') as f:  # newline=''防空行
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Name', 'Age', 'City'])
        writer.writerow(['Alice', 25, 'New York'])
        writer.writerows([  # 批量写入多行
            ['Bob', 30, 'Los Angeles'],
            ['Charlie', 35, 'Chicago']
        ])

    # 读取CSV（字典形式）
    with open('data.csv', 'r') as f:
        reader = csv.DictReader(f)  # 自动解析表头
        for row in reader:
            print(f"{row['Name']} lives in {row['City']}")


if __name__ == '__main__':
    import openpyxl  # 需安装：pip install openpyxl
    import json


    def excel_to_json(excel_path, json_path):
        wb = openpyxl.load_workbook(excel_path)
        sheet = wb.active
        # 获取标题行
        headers = [cell.value for cell in sheet[1]]
        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):  # 跳过标题行
            row_data = {}
            for idx, value in enumerate(row):
                key = headers[idx]
                # 处理JSON格式的字符串（如Skills列）
                if isinstance(value, str) and value.startswith('['):
                    try:
                        value = json.loads(value.replace("'", '"'))  # 单引号转双引号
                    except json.JSONDecodeError:
                        pass  # 保持原始字符串
                row_data[key] = value
            data.append(row_data)

        with open(json_path, 'w') as f:
            json.dump(data, f, indent=2)

    excel_to_json('input.xlsx', 'output.json')