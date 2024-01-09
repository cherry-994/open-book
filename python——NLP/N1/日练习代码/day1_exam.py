# (1)矩阵创建
import tensorflow as tf
# ①创建一个维度为3*3的全1矩阵
a1 = tf.ones(shape=[3, 3])
print(a1)
# ②使用range，创建一个1-9的1阶张量
a2 = tf.range(start=1, limit=10)
print(a2)
# ③打印上题的维度
print(a2.shape)
# ④将上题维度修改为3,1,3
a3 = tf.reshape(a2, shape=[3, 1, 3])
print(a3)
# ⑤使用函数，去除维度中函数1的维度
a4 = tf.squeeze(a3)
print(a4)
# (2)切片及其他
# ①使用1-9的向量，使用切片，打印3,4,5,6
b1 = tf.range(1, 10)[2: 6]
# ②打印上题向量的均值
b2 = tf.reduce_mean(b1)
print(b2)
# ③创见一个2行2列的标准正态分布矩阵
b3 = tf.random.normal(shape=[2, 2])
print(b3)
# ④创建一个2行2列的全0矩阵
b4 = tf.zeros(shape=[2, 2])
print(b4)
# ⑤将3,4问的结果拼接成一个4行2列的结果
a5 = tf.concat([b3, b4], axis=0)
print(a5)
