import json
# 제이슨 파일로 저장

def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

f = open(f'스택별.json', encoding='UTF-8')
data = json.loads(f.read())

tem_dict={}

for i in data:
    tem_dict[i] = []

toJson(tem_dict,'aaa')