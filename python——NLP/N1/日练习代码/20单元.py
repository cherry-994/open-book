import numpy as np
import faiss

# 加载数据 # 加载名为  第三题.csv 的CSV文件，使用逗号分隔，生成浮点数数组
data = np.loadtxt(r'C:\Users\jiayu\Desktop\日考\实训基础N1-算法进阶1-20单元\数据.csv', delimiter=',')

# 创建一个查询向量
query_vector = [0.457812,0.920403,0.879069,0.252616,0.348009,0.182589,0.901796,0.706528,0.726658,0.900088,0.779164,0.599155,0.291125,0.151395,0.335175,0.657552]

#暴力检索，正排索引
# 初始化 Faiss 索引h
index = faiss.IndexFlatL2(16) #

# 添加数据到 Faiss 索引
index.add(data)

# 在 Faiss 索引中查找最近的 k 个邻居
k = 2
D, I = index.search(np.array([query_vector]), k)

# 打印查询结果
print(I)