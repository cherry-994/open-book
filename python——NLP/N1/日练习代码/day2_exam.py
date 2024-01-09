# 1.对以下数据进行多变量线性回归处理（每小题10分）
# (1)数据处理

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, losses, optimizers

# ①读取data-01-test-score.csv数据
data = np.loadtxt('data-01-test-score.csv', delimiter=',')
# ②将最后一列作为y标签，其他数据作为x
x = data[:, :-1]
y = data[:, -1]
# ③将数据进行洗牌处理
# ④将数据按照7:3比例切分为训练集和测试集
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(x, y, shuffle=True)
# (2)模型操作
# ①创建模型
model = models.Sequential()
# ②设置网络，输入3个特征，输出一个数据值
model.add(layers.Dense(input_dim=3, units=1, activation='relu'))
model.add(layers.Dense(units=1, activation='linear'))
# ③使用rmsprop进行梯度下降，损失函数设置为均方误差
model.compile(optimizer=optimizers.RMSprop, loss='mse', metrics='mse')
# ④训练数据2000次
model.fit(train_x, train_y, epochs=2000)
# ⑤使用测试集数据，打印测试结果
predict = model.predict(test_x)
print(predict)
# ⑥可视化：将测试集的真实值和预测值变化绘图进行对比
plt.plot(test_y)
plt.plot(predict)
plt.show()
