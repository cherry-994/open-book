

from sklearn.feature_extraction.text import CountVectorizer

# # 读取数据


texts = ["dog cat fish","dog cat cat","fish bird", 'bird'] 

# 实例化BOW词袋子模型（3分）
vectorizer = CountVectorizer()

# 训练词袋子模型（3分）
#toarray()转化为numpy类型
a = vectorizer.fit_transform (texts).toarray()  

print(a)
# 输出查看词袋字典（3分）
print("Vocabulary:", vectorizer.vocabulary_)

# # 输出第0个列表元素中索引为3的元素的词频（3分）

print(a[0][3])
# 查看每个词在所有文档中的词频（3分）
print(a.sum(axis=0))