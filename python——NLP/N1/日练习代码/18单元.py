# from elasticsearch import Elasticsearch
# import json
# from elasticsearch.helpers import bulk

# es = Elasticsearch(hosts=['http://localhost:9200'])
# index_name = 'pneumonia5'
# actions = []

# with open(r'C:\Users\jiayu\Desktop\月考\07-08-2-00001\第三题数据.json', 'r', encoding='utf-8') as file:
#     for line in file:
#         actions.append({'_index': index_name, '_source': json.loads(line)})
    
#     # 在循环外执行批量操作
#     bulk(es, actions, index=index_name)

# # 执行搜索操作
# keyword = "流行性感冒怎么治疗"
# response = es.search(index=index_name, q=keyword)

# # 打印搜索结果
# print(response)