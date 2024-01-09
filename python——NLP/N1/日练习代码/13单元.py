from sklearn.feature_extraction.text import TfidfVectorizer

# 示例文档集合
documents = [
    "This is a sample document.",
    "TF-IDF is used in information retrieval.",
    "Information retrieval is the process of obtaining information from a large repository of data.",
    "TF-IDF stands for Term Frequency-Inverse Document Frequency."
]

# 创建一个TfidfVectorizer对象
tfidf_vectorizer = TfidfVectorizer()

# 训练并转换文档集合
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# 查询词
query_term = "TF-IDF"

# 获取查询词的索引
query_term_index = tfidf_vectorizer.vocabulary_.get(query_term)

# 7.将文档转化为numpy数组并获取TF-IDF值
tfidf_values = tfidf_matrix.toarray()[:, query_term_index]

# 打印TF-IDF值
for i, value in enumerate(tfidf_values):
    print(f"TF-IDF for '{query_term}' in Document {i + 1}: {value}")
