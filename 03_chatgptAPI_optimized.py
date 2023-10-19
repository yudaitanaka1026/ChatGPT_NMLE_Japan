#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tanakayudai

Solve the translated questions of the NMLE in Japan by ChatGPT API with the optimized prompts.

"OPENAI_API_KEY", "CSV_FILE_NAME", "QUESTION_FOLDER_PATH", "RESULT_FOLDER_PATH" and "PROMPT_CSV_FILE_PATH" should be set according to your environment following the comments below.

- `OPENAI_API_KEY`: Your OpenAI API key
- `CSV_FILE_NAME`: Name of your question CSV file
- `QUESTION_FOLDER_PATH`: Path to your question CSV file's folder
- `RESULT_FOLDER_PATH`: Path to save the result
- `PROMPT_CSV_FILE_PATH`: Path to the CSV file containing optimized prompts
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "OPENAI_API_KEY"

# Load the tuned prompts
df_p = pd.read_csv("PROMPT_CSV_FILE_PATH", header=0, index_col=0)
df_p.head()

tra = [df_p.iloc[0, 0], df_p.iloc[1, 0], df_p.iloc[0, 0], df_p.iloc[0, 0], df_p.iloc[1, 0], df_p.iloc[1, 0]]
ex = [df_p.iloc[0, 1], df_p.iloc[1, 1], df_p.iloc[0, 1], df_p.iloc[0, 1], df_p.iloc[1, 1], df_p.iloc[1, 1]]

# Translation the original Japanese sentences into plain English and answer the translated questions
# For non-comprehension questions
def modified_ask(name, translation, exam):
  df = pd.read_csv("QUESTION_FOLDER_NAME" + name + ".csv", header=0, index_col=0)
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
             "content": translation
             },
             {
                 "role": "user",
              "content": str(df.iloc[i, 4])+str(df.iloc[i, 5])
              }],
              temperature=0
              )
    df.iloc[i, 8] = english["choices"][0]["message"]["content"]
    
    res = []
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": exam
             },
             {
                 "role": "user",
              "content": df.iloc[i, 8]
              }],
              temperature=0
              )
    df.iloc[i, 9] = res["choices"][0]["message"]["content"]

  df.to_csv("RESULT_FOLDER_NAME" + name + '.csv')

qtype = ['必修一般', '必修臨床', '一般総論', '一般各論', '臨床総論', '臨床各論']]
for i in range(-1, len(qtype)):
  modified_ask(qtype[i], tra[i], ex[i])

# For comprehension questions
df = pd.read_csv("QUESTION_FOLDER_PATH" + "CSV_FILE_NAME" + ".csv", header=0, index_col=0)
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
           "content": df_p.iloc[2, 0]
           },
           {
               "role": "user",
            "content": "Q1:"+df.iloc[i*2, 4]+df.iloc[i*2, 5]+"Q2:"+df.iloc[i*2+1, 4]+df.iloc[i*2+1, 5]
            }],
            temperature=0
            )
  df.iloc[i*2, 8] = english["choices"][0]["message"]["content"]
  
  res = []
  res = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {"role": "system",
           "content": df_p.iloc[2, 1]
           },
           {
               "role": "user",
            "content": df.iloc[i*2, 8]
            }],
            temperature=0
            )
  df.iloc[i*2, 9] = res["choices"][0]["message"]["content"]
  
df.to_csv("RESULT_FOLDER_PATH" + "CSV_FILE_NAME" + ".csv")
