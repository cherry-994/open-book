def clean_sales_data(sales_data):
    cleaned_data = []
    for record in sales_data:
        # 1. 删除销售数量小于1的记录
        if record['quantity'] >= 1:
            # 2. 删除销售金额小于0的记录
            if record['amount'] >= 0:

                # 4. 转换产品名称为大写
                record['product_name'] = record['product_name'].upper()
                # 5. 四舍五入销售金额到两位小数
                record['amount'] = round(record['amount'], 2)
                # 6. 将销售数量转换为整数
                record['quantity'] = int(record['quantity'])
                # 10. 将销售记录添加到清洗后的数据列表
                cleaned_data.append(record)
    return cleaned_data

# 创建销售数据
sales_data = [
    {'product_name': 'Product A', 'quantity': 5, 'amount': 100.00},
    {'product_name': 'Product B', 'quantity': 2, 'amount': -50.00},
    {'product_name': 'Product C$', 'quantity': 1, 'amount': 25.0},
    {'product_name': 'Product D', 'quantity': 0, 'amount': 10.0},
    {'product_name': 'Product E', 'quantity': 3, 'amount': 75.0},
    {'product_name': 'Product F', 'quantity': 4, 'amount': 80.0},
    {'product_name': 'Product G', 'quantity': 6, 'amount': 150.0},
]

# 调用清洗函数
cleaned_data = clean_sales_data(sales_data)
print(cleaned_data)