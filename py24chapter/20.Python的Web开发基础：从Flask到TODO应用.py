from flask import Flask, jsonify, render_template, request

# app = Flask(__name__)


# 路由定义
# @app.route('/user/<username>')
# def show_user(username):
#     # 传入变量到模板
#     return render_template('profile.html',
#                            name=username,
#                            skills=['Python', 'Java', 'AI'])


app = Flask(__name__)
books = [
    {"id": 1, "title": "Python基础教程"}
]


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)  # 自动转为JSON格式


@app.route('/books', methods=['POST'])
def add_book():
    new_book = {"id": len(books) + 1, "title": request.json['title']}
    books.append(new_book)
    return jsonify(new_book), 201  # 201表示创建成功


if __name__ == '__main__':
    app.run(debug=True)
