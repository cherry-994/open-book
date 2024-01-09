import pandas as pd
import jieba
from gensim.models import Word2Vec
import re  #正则
# #读取文件并进行简单的处理
data = pd.read_excel(r"C:\Users\jiayu\Desktop\N1日考\实训基础N1-算法进阶1-10单元\sohu_corpus_auto_corpus.xls")

data = data["review"].apply(lambda x: re.sub('[^\u4e00-\u9fa5]+', '', str(x)))    #
print(data[:5])


#构建中文词汇表
datas = []
for row in data:
    words = jieba.cut(row)
    datas.append([i for i in words])
print(datas)


# #训练模型
model = Word2Vec(datas, sg=1, min_count=1)   #100万   100万*3    3

#计算和食堂相似的前5个词
similar_words = model.wv.most_similar('食堂',topn=5)
print(similar_words)


#计算句子相似度
s1 = "堂食的卫生条件不错"
s2 = "食堂的很干净，地板很干净"

s1 = str(jieba.lcut(s1))
s2 = str(jieba.lcut(s2))

similarity = model.wv.wmdistance(s1,s2)
print("The Word Mover's Distance between s1 and s2 is:", similarity)