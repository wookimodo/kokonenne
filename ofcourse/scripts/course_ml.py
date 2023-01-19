import random
import pandas as pd
import numpy as np
import json
from sklearn.preprocessing import MinMaxScaler
from course.models import Course


# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

# 제이슨 파일 열기
f = open(f'json/inflearn.json', encoding='UTF-8')
data = json.loads(f.read())  

# 데이터 불러오기
df = pd.read_json(f"json/inflearn.json")
df = df.transpose().reset_index().rename(columns={'index':'title'})
df = df.drop(['headline','url','image','level'],axis=1)

# 강의 수 컬럼 추가
df['courseCnt'] = [i.lstrip('총').split('개')[0] for i in df['courseTime']]

# 강의 시간 전처리

df['courseTime'] = [i.split('개')[1].rstrip('의수업') for i in df['courseTime']]
df['courseTime'] = [i.replace('시간','.').replace('분','') for i in df['courseTime']]

# 강의 가격 전처리
df['price'] = [i.replace(',','') if i != None else i for i in df['price']]

# 정보없음, 무료, 수강생없음 등은 0으로 처리, 평점은 null값으로 대체
df['student'] = [0 if i==None else i for i in df['student']]
df['recommend'] = [0 if i==None else i for i in df['recommend']]
df['reviewCnt'] = [0 if i==None else i for i in df['reviewCnt']]
df['score'] = [None if i=='' else i for i in df['score']]
df['price'] = [0 if i == None else i for i in df['price']]
df['courseTime'] = [0 if i.isdigit()==False else i for i in df['courseTime']]

# 타입변환
df = df.astype({'courseTime':'float','student':'int','recommend':'int','reviewCnt':'int','price':'int','score':'float','courseCnt':'int'})

# 강의당 시간 컬럼 추가
df['pertime'] = [x/y for x,y in zip(df['courseTime'],df['courseCnt'])]

# stack 없는 행 삭제
idx = df.loc[df['stacks']==""].index
df = df.drop(idx)

# 대분류 추출
cat1 = []
for i in df['stacks']:
  cat1.append(i[0])
df['cat1'] = cat1
# 컬럼 순서 재정의
df = df[['title','teacher','cat1','courseTime','student','recommend','reviewCnt','score','courseCnt','pertime']]

# 대분류별로 평균을 구해서 컬럼 추가
agg_dict = {
    'pertime' : [
        ("avg_pertime", 'mean'),
    ],
        'reviewCnt' : [
        ("avg_reviewCnt", 'mean'),
    ],
          'courseTime' : [
        ("avg_courseTime", 'mean'),
    ],
          'recommend' : [
        ("avg_recommend", 'mean'),
    ],
          'score' : [
        ("avg_score", 'mean'),
    ],
          'student' : [
        ("avg_student", 'mean'),
    ],

}

tmp = df.groupby('cat1').agg(agg_dict)
tmp.columns = tmp.columns.droplevel()
tmp = tmp.reset_index()

# df에 merge
df = df.merge(tmp,how="left",on = "cat1") 

# 평점에 대한 결측치는 평균으로 채움
df["score"] = df["score"].fillna(df["score"].mean())
df["avg_score"] = df["avg_score"].fillna(df["avg_score"].mean())

# 강의시간, 수강생수, 추천수, 리뷰수, 평점이 각 카테고리의 평균와 얼마나 차이나는지
df['diffstudent'] = [x-y for x,y in zip(df['student'],df['avg_student'])]
df['diffrecommend'] = [x-y for x,y in zip(df['recommend'],df['avg_recommend'])]
df['diffreviewCnt'] = [x-y for x,y in zip(df['reviewCnt'],df['avg_reviewCnt'])]
df['diffscore'] = [x-y for x,y in zip(df['score'],df['avg_score'])]

# 랭킹계산에 필요한 컬럼만 추출
df_ranking = df.iloc[:,4:]
# 민맥스스케일링
scaler = MinMaxScaler()
df_ranking = scaler.fit_transform(df_ranking)

df_ranking = pd.DataFrame(df_ranking)
df_ranking.columns = df.iloc[:,4:].columns

# 랭킹df에 title, teacher, cat1추가
df_ranking[['title','teacher']] = df[['title','teacher']]
df_ranking['cat1'] = df['cat1']
df = df_ranking[['title','teacher','cat1','diffstudent','diffrecommend','diffreviewCnt','diffscore']]

# finalscore 계산
df['finalscore'] = [a+b+c+d for a,b,c,d in zip(df.loc[:,'diffstudent'],df.loc[:,'diffrecommend'],df.loc[:,'diffreviewCnt'],df.loc[:,'diffscore'])]
df['rank'] = df['finalscore'].rank(ascending=False)

# 기술 스택별로 랭킹반환하는 함수
def run():
  result = df.sort_values('finalscore',ascending=False)
  for title,rank in zip(result['title'],result['rank']):
    for i in data:
      if i == title:
        data[i]['rank'] = rank
  toJson(data,'modify')
  print(data)
  return result[['title','rank']]


# 스택별로 랭킹보여주기
# def stackrank(stack):
#   result = df.loc[df['cat1'].str.contains(stack)].sort_values('finalscore',ascending=False)
#   return result[['title','teacher']]

# print(stackrank('Java'))
