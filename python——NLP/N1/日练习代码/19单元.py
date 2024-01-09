#第二道
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

X = ["i love you", "he loves me", "she likes baseball", "i hate you", "sorry for that", "this is awful"]
labels = [1, 1, 1, 0, 0, 0]

test_text = 'sorry hate you'

# Tokenize the sentences
tokens = [sentence.split() for sentence in X]

# Build vocabulary
vocabulary = set()
for sentence_tokens in tokens:
    vocabulary.update(sentence_tokens)

# Create word-to-id and id-to-word mappings
word2id = {word: idx for idx, word in enumerate(vocabulary)}
id2word = {idx: word for word, idx in enumerate(vocabulary)}

print("id_word:", id2word)
print("word_id:", word2id)


#构建输入数据
input_sequences = []
target_sequences = []
for sentence in X:
    words = sentence.split()
    input_sequence = [word2id[i] for i in words]  
    input_sequences.append(input_sequence)
print(input_sequences)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 定义超参数
embedding_dim = 16
hidden_size = 128
output_size = 1  # 二分类输出为1
vocab_size = len(word2id)

# 定义模型
class TextRNN_Attention(nn.Module):
    def __init__(self):
        super(TextRNN_Attention, self).__init__()
        self.embeddings = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        x = self.embeddings(x)
        out, (h, c) = self.lstm(x)
        out = torch.sum(out, 1)
        out = self.fc(out)
        out = torch.sigmoid(out)
        return out


x_train = torch.LongTensor(input_sequences).to(device)
y_train = torch.FloatTensor(labels).unsqueeze(1).to(device)
print(y_train)


simple_net = TextRNN_Attention().to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(simple_net.parameters(), lr=0.01)


for i in range(1000):
    optimizer.zero_grad()
    preds = simple_net(x_train)
    loss = criterion(preds, y_train)
    if i % 100 == 0:
        print(f'{i} loss train: {loss.item()}')
    loss.backward()
    optimizer.step()
