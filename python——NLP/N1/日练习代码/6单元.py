text = "必须有录屏，无录屏者一律0分处理，必须是完整的考试录屏(只有单独录效果录屏按0分处理)，录屏过程中不允许有暂停行为，若是发现，按考试作弊处理，桌面必须有自己的学院、班级、姓名"
# 使用jieba分词
import jieba
from collections import Counter   

seg_list = jieba.cut(text)
print(seg_list)

#生成器对象，一次性的，循环遍历完成以后，生成器对象就空了，里面没有任何东西，内存被释放
# # 统计词频
word_count = Counter(seg_list)
print(word_count)

seg_list = jieba.lcut(text)
print(seg_list)


# 使用HanLP分词
from pyhanlp import HanLP
seg_list_hanlp = HanLP.segment(text)
print(seg_list_hanlp)
seg_list_hanlp = [term.word for term in seg_list_hanlp]
print(seg_list_hanlp)
# 统计词频
word_count_hanlp = Counter(seg_list_hanlp)
print(word_count_hanlp)


#深拷贝 浅拷贝
