#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tanakayudai

Solve the original Japanese text questions of the NMLE in Japan by ChatGPT API
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "*****"

# Answer the Original Japanese questions
# For non-comprehension questions
def japanese_ask(name):
  df = pd.read_csv('*****' +name+ '.csv', header=0, index_col=0)
  df['output'] = ''
  df['check'] = ''
  df['error'] = ''
  for i in range(len(df)):
    res = []
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
             "content": "次の質問に理由を添えて答えよ"
             },
             {"role": "user",str(df.iloc[i, *])
             }],
              temperature=0
              )
    df.iloc[i, *] = res["choices"][0]["message"]["content"]
  
  df.to_csv('*****' +name+'.csv')

# For comprehension questions 
df = pd.read_csv('*****.csv', header=0, index_col=0)
df['output'] = ''
df['check'] = ''
df['error'] = ''
for i in range(len(df)//2):
  res = []
  res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
                "role": "system",
             "content": "次の質問に理由を添えて答えよ"
             },
             {"role": "user",
            "content": "Q1:"+df.iloc[i*2, *]+"Q2:"+df.iloc[i*2+1, *]
            }],
            temperature=0
            )
  df.iloc[i*2, *] = res["choices"][0]["message"]["content"]
  
df.to_csv('*****.csv')