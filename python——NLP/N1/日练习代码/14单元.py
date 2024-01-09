import numpy as np

# 定义隐藏状态和观察状态
hidden_states = ['开心', '不开心']
observation_states = ['消费', '不消费']

# 初始状态概率
initial_prob = np.array([0.6, 0.4])

# 转移概率矩阵
transition_prob = np.array([[0.7, 0.3],
                            [0.4, 0.6]])

# 发射概率矩阵
emission_prob = np.array([[0.4, 0.6],
                          [0.7, 0.3]])

# 生成观察序列的函数
def generate_observation_sequence(num_steps):
    observation_sequence = []
    hidden_state = np.random.choice(hidden_states, p=initial_prob)  #按隐藏状态概率随机选择一个隐藏状态

    for _ in range(num_steps):
        observation = np.random.choice(observation_states, p=emission_prob[hidden_states.index(hidden_state)])  #根据隐藏状态来随机选择一个观测状态
        observation_sequence.append(observation)  #将观测状态加入到空列表中
        hidden_state = np.random.choice(hidden_states, p=transition_prob[hidden_states.index(hidden_state)]) #根据转移矩阵来选择初始状态
    
    return observation_sequence

# 生成一个观察序列
num_steps = 10
observation_sequence = generate_observation_sequence(num_steps)
print(observation_sequence)
