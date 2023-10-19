#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tanakayudai

Solve the original Japanese text comprehension questions of the NMLE in Japan by ChatGPT API

"OPENAI_API_KEY", "CSV_FILE_NAME", "QUESTION_FOLDER_PATH" and "RESULT_FOLDER_PATH" should be set according to your environment following the comments below.

- `OPENAI_API_KEY`: Your OpenAI API key
- `CSV_FILE_NAME`: Name of your question CSV file
- `QUESTION_FOLDER_PATH`: Path to your question CSV file's folder
- `RESULT_FOLDER_PATH`: Path to save the result
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "OPENAI_API_KEY"

# Answer the Original Japanese questions
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
            "content": "Q1:"+df.iloc[i*2, 3]+df.iloc[i*2, 4]+"Q2:"+df.iloc[i*2+1, 3]+df.iloc[i*2+1, 4]
            }],
            temperature=0
            )
  df.iloc[i*2, 8] = res["choices"][0]["message"]["content"]
  
df.to_csv("RESULT_FOLDER_PATH" + "CSV_FILE_NAME" + ".csv")
