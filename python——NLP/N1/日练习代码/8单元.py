import jieba   #分词
import jieba.analyse    #关键词提取，TF-IDF

sentence='''语言模型起源于语音识别(speech recognition)，输入一段音频数据，语音识别系统通常会生成多个句子作为候选，究竟哪个句子更合理？就需要用到语言模型对候选句子进行排序。如今语言模型的应用范围早已扩展到机器翻译、信息检索、问答、文摘等众多NLP领域。
'''
#使用TF-IDF进行关键词提取
#topK 关键词的数量
#withWeight 返回带不带权重

kw=jieba.analyse.extract_tags(sentence,topK=5,allowPOS=('n','ns'), withWeight=1)
print(kw)

#textrank进行关键词提取
kw=jieba.analyse.textrank(sentence,topK=5)
print(kw)

from pyhanlp import *   #Hanlp
#输出关键词
topK = 3
keywords = HanLP.extractKeyword(sentence, topK)
print(keywords)