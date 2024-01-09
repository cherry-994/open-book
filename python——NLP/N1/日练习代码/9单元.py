import jieba
from gensim.models import Word2Vec
import pandas as pd

# 2. 完成数据的加载
data = pd.read_csv('数据.csv')['content']

print(data)
#读取停用词
stopwords = []
with open('stopWord.txt', 'r', encoding='utf-8') as f:
    for line in f:
        stopwords.append(line.strip())

#去停用词并使用jieba进行分词
data_after_cut = []
for i in data:
    cut_sen = [j for j in jieba.cut(i) if j not in stopwords]
    data_after_cut.append(cut_sen)


# 训练模型
model = Word2Vec(data_after_cut, min_count=1, sg=1)

# 保存模型
model.save('word2vec.model')

# 加载模型并计算与“一阳生”最相似的5个词，排序并打印
model = Word2Vec.load('word2vec.model')

