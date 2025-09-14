# def sale_data():
#     import pandas as pd
#     import matplotlib
#     matplotlib.use('Agg')  # 使用非交互式后端（解决 tostring_rgb 错误）
#     import matplotlib.pyplot as plt
#     # 模拟销售数据（日期和销售额）
#     data = {'date': pd.date_range(start='2025-08-01', periods=30, freq='D'),
#             'sales': [120, 135, 128, 150, 145, 160, 158, 170, 165, 180,
#                       175, 190, 185, 200, 210, 205, 220, 215, 230, 240,
#                       235, 250, 245, 260, 255, 270, 265, 280, 290, 285]}
#     df = pd.DataFrame(data)
#     df.set_index('date', inplace=True)
#     # 计算7日移动平均
#     df['7d_MA'] = df['sales'].rolling(window=7).mean()
#     # 可视化结果
#     plt.figure(figsize=(12, 6))
#     plt.rcParams['font.sans-serif'] = ['SimHei']  # 或 'Microsoft YaHei'
#     plt.rcParams['axes.unicode_minus'] = False
#     plt.plot(df['sales'], label='实际销售额', marker='o')
#     plt.plot(df['7d_MA'], label='7日移动平均', color='red', linewidth=2)
#     plt.title('销售数据趋势分析')
#     plt.xlabel('日期')
#     plt.ylabel('销售额')
#     plt.legend()
#     plt.grid(True)
#     # 保存到文件
#     plt.savefig('2025-08-01_sale_output.png')
#
#
# # def machelearning():
# #     global data, y, model, predict
# #     from flask import Flask, request, jsonify
# #     import joblib
# #     from sklearn.datasets import fetch_california_housing
# #     # 训练模型（实际项目中需先完成训练）
# #     data = fetch_california_housing()
# #     X, y = data.data, data.target
# #     model = RandomForestRegressor().fit(X, y)
# #     joblib.dump(model, 'house_price_model.pkl')
# #     # 部署API
# #     app = Flask(__name__)
# #     model = joblib.load('house_price_model.pkl')
# #
# #     @app.route('/predict', methods=['POST'])
# #     def predict():
# #         data = request.json['features']
# #         prediction = model.predict([data])
# #         return jsonify({'price': round(prediction[0], 2)})
# #
# #     if __name__ == '__main__':
# #         app.run(host='0.0.0.0', port=5000)
# #
# #
# # machelearning()
#
# # views.py
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.response import Response
#
#
# class OptimizedBlogView(APIView):
#     pagination_class = PageNumberPagination
#     page_size = 20  # 每页20条数据
#
#     @cache_page(60 * 5)  # 缓存5分钟
#     def get(self, request):
#         # 优化查询：一次性获取关联的作者信息
#         blogs = Blog.objects.prefetch_related('author').all()
#
#         # 分页处理
#         paginator = self.pagination_class()
#         page = paginator.paginate_queryset(blogs, request)
#
#         # 序列化数据
#         serializer = BlogSerializer(page, many=True)
#         return paginator.get_paginated_response(serializer.data)
#
#     # 在urls.py中添加路由
#
#
# path('optimized-blogs/', OptimizedBlogView.as_view())
#
# # if __name__ == '__main__':
#     # 1.数据分析：Pandas时间序列预测
# #     sale_data()
