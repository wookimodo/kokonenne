import bcrypt
import json

# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

# json 불러오기
with open('inflearn test 240개.json', 'r', encoding='utf-8') as file:
    temp_dict = json.load(file)


salt = bcrypt.gensalt()
for i in temp_dict:
    url = temp_dict[i]['url']
    pwdurl = url.encode('utf-8')
    a = bcrypt.hashpw(pwdurl, salt)
    j = a.decode('utf-8')
    print(j)
    temp_dict[i]['pwdurl'] = j
    
# 제이슨 파일로 저장
toJson(temp_dict,"inflearn test")
print("json 저장 완료")
