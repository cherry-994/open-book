import pandas as pd 
import numpy as np

# 生成模拟数据
data = pd.DataFrame()

data["age"] = np.random.randint(18, 65, 100)

# 随机生成100个18-65之间的年龄数据

data['gender'] = np.random.choice(['male','female'], 100)  
# 随机生成100条性别数据

data['income'] = np.random.normal(50000, 15000, 100)
# 生成正态分布的收入数据

data.to_csv("data.csv", index=False) 
# 数据保存到CSV文件

# 处理数据
import pandas as pd 

data = pd.read_csv("data.csv")  # 读取生成的数据

print(data.head()) # 打印前5行数据

data = data[data["age"] > 18] # 过滤年龄小于0的行

print(data["income"].mean()) # 打印平均收入
