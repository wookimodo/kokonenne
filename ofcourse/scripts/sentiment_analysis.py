import pandas as pd
import numpy as np
import json
from transformers import pipeline

# 제이슨 파일로 저장
def toJson(res_dict,save_name):
    with open(f'{save_name}.json', 'w', encoding='utf-8') as file :
        json.dump(res_dict, file, ensure_ascii=False, indent='\t')

# 리뷰데이터 불러와서 데이터프레임으로 변환
df = pd.read_json(f"json/reviewData.json")
df = df.transpose().reset_index().rename(columns={'index':'title'})

# 감정분석 모델
classifier = pipeline(
    "sentiment-analysis", model="sangrimlee/bert-base-multilingual-cased-nsmc"
)

def run():
  # 리뷰별로 감정분석 실행
  review_list = []
  df_length = len(df)
  for i in range(df_length):
    title  = df.iloc[i]['title']
    reviews = df.iloc[i]['review']
    for review in reviews:
      # 500자로 제한해서 분석
      sentiment = classifier(review[:500])[0]
      # [리뷰, 긍/부정, 스코어]를 저장
      review_list.append([title,review[:500],sentiment['label'],sentiment['score']])
  # 분석결과를 데이터프레임으로 저장
  sentiment = pd.DataFrame(review_list,columns=['title','review','sentiment','score'])

  # 감성 분석결과를 json파일로 저장
  sentiment_dict = {}
  length = len(sentiment)

  for i in range(length):
    if sentiment.iloc[i]['title'] not in sentiment_dict.keys():
      sentiment_dict[sentiment.iloc[i]['title']] = [ [sentiment.iloc[i]['review'], sentiment.iloc[i]['sentiment'], sentiment.iloc[i]['score']] ]
    else:
      sentiment_dict[sentiment.iloc[i]['title']].append([sentiment.iloc[i]['review'],sentiment.iloc[i]['sentiment'],sentiment.iloc[i]['score']])

  toJson(sentiment_dict,"sentiment")