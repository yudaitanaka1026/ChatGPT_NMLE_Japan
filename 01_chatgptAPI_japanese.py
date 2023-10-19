#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tanakayudai

Solve the original Japanese text questions of the NMLE in Japan by ChatGPT API

"OPENAI_API_KEY", "CSV_FILE_NAME", "QUESTION_FOLDER_PATH" and "RESULT_FOLDER_PATH" should be set according to your environment following the comments below.

OPENAI_API_KEY: Please enter your openai api key.
CSV_FILE_NAME: Please enter your question csv file name.
QUESTION_FOLDER_PATH: Please enter the path of question csv file on your environment.
RESULT_FOLDER_PATH: Please enter the path on your environment which you want to output result.
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "OPENAI_API_KEY"

# Answer the Original Japanese questions
# For non-comprehension questions
def japanese_ask(name):
  df = pd.read_csv("QUESTION_FOLDER_PATH" + name + ".csv", header=0, index_col=0)
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
             {"role": "user",
             "content": str(df.iloc[i, 7])+str(df.iloc[i, 8])
             }],
              temperature=0
              )
    df.iloc[i, 11] = res["choices"][0]["message"]["content"]
  
  df.to_csv("RESULT_FOLDER_PATH" + name +".csv")

japanese_ask("CSV_FILE_NAME")

# For comprehension questions 
df = pd.read_csv("QUESTION_FOLDER_PATH" + "CSV_FILE_NAME" + ".csv", header=0, index_col=0)
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
            "content": "Q1:"+df.iloc[i*2, 7]+df.iloc[i*2, 8]+"Q2:"+df.iloc[i*2+1, 7]+df.iloc[i*2+1, 8]
            }],
            temperature=0
            )
  df.iloc[i*2, 11] = res["choices"][0]["message"]["content"]
  
df.to_csv("RESULT_FOLDER_PATH" + "CSV_FILE_NAME" + ".csv")
