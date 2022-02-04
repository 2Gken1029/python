#!/usr/bin/env python3
# coding: utf-8

import requests
import json
import time
from pprint import pprint

import pandas as pd

# 1. 楽天レシピのレシピカテゴリ一覧を取得する

res = requests.get('https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426?applicationId=1037522848820870734')

json_data = json.loads(res.text)
# pprint(json_data)

# mediumカテゴリの親カテゴリの辞書
parent_dict = {}

df = pd.DataFrame(columns=['category1','category2','category3','categoryId','categoryName'])

# 大カテゴリ
for category in json_data['result']['large']:
    df = df.append({'category1':category['categoryId'],'category2':"",'category3':"",'categoryId':category['categoryId'],'categoryName':category['categoryName']}, ignore_index=True)

# 中カテゴリ
for category in json_data['result']['medium']:
    df = df.append({'category1':category['parentCategoryId'],'category2':category['categoryId'],'category3':"",'categoryId':str(category['parentCategoryId'])+"-"+str(category['categoryId']),'categoryName':category['categoryName']}, ignore_index=True)
    parent_dict[str(category['categoryId'])] = category['parentCategoryId']

# 小カテゴリ
for category in json_data['result']['small']:
    df = df.append({'category1':parent_dict[category['parentCategoryId']],'category2':category['parentCategoryId'],'category3':category['categoryId'],'categoryId':parent_dict[category['parentCategoryId']]+"-"+str(category['parentCategoryId'])+"-"+str(category['categoryId']),'categoryName':category['categoryName']}, ignore_index=True)

# genre = input()
genre = "肉"

# 2. キーワードからカテゴリを抽出する
df_keyword = df.query(f'categoryName.str.contains("{genre}")', engine='python')
# pprint(df_keyword)

# 3. 人気レシピを取得する
df_recipe = pd.DataFrame(columns=['recipeId', 'recipeTitle', 'foodImageUrl', 'recipeMaterial', 'recipeCost', 'recipeIndication', 'categoryId', 'categoryName'])

for index, row in df_keyword.iterrows():
    time.sleep(3) # 連続でアクセスすると先方のサーバに負荷がかかるので少し待つのがマナー

    url = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?applicationId=1037522848820870734&categoryId='+row['categoryId']
    res = requests.get(url)

    json_data = json.loads(res.text)
    recipes = json_data['result']

    for recipe in recipes:
        df_recipe = df_recipe.append({'recipeId':recipe['recipeId'],'recipeTitle':recipe['recipeTitle'],'foodImageUrl':recipe['foodImageUrl'],'recipeMaterial':recipe['recipeMaterial'],'recipeCost':recipe['recipeCost'],'recipeIndication':recipe['recipeIndication'],'categoryId':row['categoryId'],'categoryName':row['categoryName']}, ignore_index=True)

pprint(df_recipe)

if __name__ == '__main__':
    pass