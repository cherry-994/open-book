
from sklearn_crfsuite import CRF


# 新的训练数据
X_train_new = [
    [{'word': '她', 'pos': 'pronoun'}, {'word': '是', 'pos': 'verb'}, {'word': '医生', 'pos': 'noun'}],
    [{'word': '他', 'pos': 'pronoun'}, {'word': '是', 'pos': 'verb'}, {'word': '工程师', 'pos': 'noun'}]
]
y_train_new = [['B-per', 'O', 'B-job'], ['B-per', 'O', 'B-job']]

# 定义CRF模型
crf = CRF(
    c1=0.1,
    c2=0.1,
    max_iterations=100,
    all_possible_transitions=True
)

# 训练新的CRF模型
crf.fit(X_train_new, y_train_new)

# 预测新的数据
X_train_new = [
    [{'word': '她', 'pos': 'pronoun'}, {'word': '是', 'pos': 'verb'}, {'word': '医生', 'pos': 'noun'}],
    [{'word': '他', 'pos': 'pronoun'}, {'word': '是', 'pos': 'verb'}, {'word': '工程师', 'pos': 'noun'}]
]
y_pred = crf.predict(X_train_new)
print("预测结果:", y_pred)
