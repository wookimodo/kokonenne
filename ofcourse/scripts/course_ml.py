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

# 전체 강의 데이터 불러오기
f = open(f'json/allcourse.json', encoding='UTF-8')
data = json.loads(f.read())  

# 데이터 불러오
df = pd.read_json(f"json/allcourse.json")
df = df.transpose().reset_index().rename(columns={'index':'title'})
df = df.drop(['headline','url','image','level'],axis=1)
df = df.rename(columns={'rating':'score'})
df = df[['title','teacher','stacks','student','reviewCnt','score']]

# 리뷰 수 전처리 
df['reviewCnt'] = [str(i).replace(',','') for i in df['reviewCnt']]

# 정보없음, 무료, 수강생없음 등은 0으로 처리, 평점은 null값으로 대체
df['student'] = [0 if i=='None' else i for i in df['student']]
df['reviewCnt'] = [0 if i=='None' else i for i in df['reviewCnt']]
df['score'] = [None if i=='None' else i for i in df['score']]


# 타입변환
df = df.astype({'student':'float','reviewCnt':'float','score':'float'})

# 구름사이트 감정분석 데이터
f = open(f'json/goorm_sentiment.json', encoding='UTF-8')
goorm = json.loads(f.read())  

# 데이터프레임으로 변환
review_data = []
for title in goorm:
  for review in goorm[title]:
    review_data.append([title,review[0],review[1],review[2]])
df_goorm = pd.DataFrame(review_data,columns=['title','review','sentiment','score'])

# 인프런 사이트 감정분석 데이터
f = open(f'json/inflearn_sentiment.json', encoding='UTF-8')
inflearn = json.loads(f.read())  

# 데이터프레임으로 변환
review_data = []
for title in inflearn:
  for review in inflearn[title]:
    review_data.append([title,review[0],review[1],review[2]])
df_inflearn = pd.DataFrame(review_data,columns=['title','review','sentiment','score'])

# 감정분석 데이터 합치기
df_sentiment = pd.concat([df_goorm,df_inflearn],axis=0)

# 인강별로 긍정,부정 비율 구해서 피쳐 추가
agg_dict = {
  'score' : [
        ("positive_ratio", lambda x : (x>0.98).mean()),
        ("negative_ratio", lambda x : (x<-0.85).mean()),
    ]
}

tmp = df_sentiment.groupby('title').agg(agg_dict)
tmp.columns = tmp.columns.droplevel()
tmp = tmp.reset_index()

# 전체 강의 데이터프레임에 merge
df = df.merge(tmp,how="left",on = "title") 

# stack 없는 행 삭제
idx = df.loc[df['stacks']==""].index
df = df.drop(idx)

# 대분류 추출
cat1 = []
for i in df['stacks']:
  cat1.append(i[0])
df['cat1'] = cat1
# 컬럼 순서 재정의
df = df[['title','teacher','cat1','student','reviewCnt','score','positive_ratio','negative_ratio']]


# 대분류별로 평균을 구해서 컬럼 추가
agg_dict = {
        'reviewCnt' : [
        ("avg_reviewCnt", 'mean'),
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

# student 결측치는 0으로 채움
df["student"] = df["student"].fillna(0)
df["avg_student"] = df["avg_student"].fillna(0)

# 리뷰가 없는 데이터는 평균으로 채움
df["positive_ratio"] = df["positive_ratio"].fillna(df["positive_ratio"].mean())
df["negative_ratio"] = df["negative_ratio"].fillna(df["negative_ratio"].mean())

# 강의시간, 수강생수, 리뷰수, 평점이 각 카테고리의 평균와 얼마나 차이나는지
df['diffstudent'] = [x-y for x,y in zip(df['student'],df['avg_student'])]
df['diffreviewCnt'] = [x-y for x,y in zip(df['reviewCnt'],df['avg_reviewCnt'])]
df['diffscore'] = [x-y for x,y in zip(df['score'],df['avg_score'])]

# 랭킹계산에 필요한 컬럼만 추출
df_ranking = df.iloc[:,5:]

# 민맥스스케일링
scaler = MinMaxScaler()
df_ranking = scaler.fit_transform(df_ranking)

df_ranking = pd.DataFrame(df_ranking)
df_ranking.columns = df.iloc[:,5:].columns

# 랭킹df에 title, teacher, cat1추가
df_ranking[['title','teacher']] = df[['title','teacher']]
df_ranking['cat1'] = df['cat1']
df = df_ranking[['title','teacher','cat1','diffstudent','diffreviewCnt','diffscore','positive_ratio','negative_ratio']]

# finalscore 계산
df['finalscore'] = [a+b+c+d-e for a,b,c,d,e in zip(df.loc[:,'diffstudent'],df.loc[:,'diffreviewCnt'],df.loc[:,'diffscore'],df.loc[:,'positive_ratio'],df.loc[:,'negative_ratio'])]
df['rank'] = df['finalscore'].rank(ascending=False)

# 기술 스택별로 랭킹반환하는 함수
def run():
  result = df.sort_values('finalscore',ascending=False)
  for title,rank in zip(result['title'],result['rank']):
    for i in data:
      if i == title:
        data[i]['rank'] = rank
  toJson(data,'allcourse')
  print(data)
  return result[['title','rank']]

