#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tanakayudai

Solve the translated questions of the NMLE in Japan by ChatGPT API.
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "*****"

# Translation the original Japanese sentences into English ones and answer the translated questions
# For non-comprehension questions
def english_ask(name):
  df = pd.read_csv('*****' +name+ '.csv', header=0, index_col=0)
  df['english'] = ''
  df['output'] = ''
  df['check'] = ''
  df['error'] = ''
  for i in range(len(df)):
    english = []
    english = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
             "content": "Translate the following Japanese into English."
             },
             {
                 "role": "user",
              "content": str(df.iloc[i, *])+str(df.iloc[i, *])
              }],
              temperature=0
              )
    df.iloc[i, *] = english["choices"][0]["message"]["content"]
    
    res = []
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
             "content": "Answer the following questions with reasons."
             },
             {"role": "user",
             "content": df.iloc[i, *]
             }],
              temperature=0
              )
    df.iloc[i, *] = res["choices"][0]["message"]["content"]
  
  df.to_csv('*****' +name+'.csv')

# For comprehension questions 
df = pd.read_csv('*****.csv', header=0, index_col=0)
df['english'] = ''
df['output'] = ''
df['check'] = ''
df['error'] = ''
for i in range(len(df)//2):
  english = []
  english = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role": "system",
           "content": "Translate the following Japanese into English."
           },
           {
               "role": "user",
            "content": "Q1:"+df.iloc[i*2, *]+"Q2:"+df.iloc[i*2+1, *]
            }],
            temperature=0
            )
  df.iloc[i*2, *] = english["choices"][0]["message"]["content"]
    
  res = []
  res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role": "system",
           "content": "Answer the following questions with reasons."
           },
           {"role": "user",
            "content": df.iloc[i*2, *]
            }],
            temperature=0
            )
  df.iloc[i*2, *] = res["choices"][0]["message"]["content"]
  
df.to_csv('******.csv')
