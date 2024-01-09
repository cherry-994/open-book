# 定义词汇表
vocab = ["I", "love", "coding", "in", "Python"]

# 要编码的句子
sentence = "I love coding in Python"

# 创建一个字典来映射词汇表中的单词到它们的索引
word_to_index = {word: index for index, word in enumerate(vocab)}

# 初始化一个全零的向量，长度为词汇表的大小
one_hot_vector = [0] * len(vocab)

# 对句子进行one-hot编码
for word in sentence.split():
    if word in word_to_index:
        one_hot_vector[word_to_index[word]] = 1

print(one_hot_vector)
