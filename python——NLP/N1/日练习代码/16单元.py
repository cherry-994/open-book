from hmmlearn import hmm
import numpy as np

# 定义HMM模型
model = hmm.MultinomialHMM(n_components=2)

# 初始化HMM模型的参数
model.startprob_ = np.array([0.6, 0.4])  # 初始状态概率
model.transmat_ = np.array([[0.7, 0.3],  # 状态转移概率矩阵
                            [0.4, 0.6]])
model.emissionprob_ = np.array([[0.1, 0.4, 0.5],  # 发射概率矩阵
                               [0.6, 0.3, 0.1]])

# 生成观测序列
obs = np.array([[0, 2, 1, 1, 2, 0]]).T

# 使用前向算法计算观测序列的概率
log_prob = model.score(obs)

print("观测序列的对数概率:", log_prob)
