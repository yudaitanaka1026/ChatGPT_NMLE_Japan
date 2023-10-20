#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: tanakayudai

Solve the original Japanese text non-comprehension questions of the NMLE in Japan by ChatGPT API

Setup requires:
- `YOUR_OPENAI_API_KEY`: Your OpenAI API key
- `YOUR_QUESTION_CSV_FILE_NAME`: Name of your question CSV file
- `PATH_TO_QUESTION_FOLDER`: Path to your question CSV file's folder
- `PATH_TO_RESULT_FOLDER`: Path to save the result
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "YOUR_OPENAI_API_KEY"

# Answer the Original Japanese questions
# For non-comprehension questions
def japanese_ask(name):
  df = pd.read_csv("PATH_TO_QUESTION_FOLDER" + name + ".csv", header=0, index_col=0)
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
             "content": str(df.iloc[i, 3])+str(df.iloc[i, 4])
             }],
              temperature=0
              )
    df.iloc[i, 8] = res["choices"][0]["message"]["content"]
  
  df.to_csv("PATH_TO_RESULT_FOLDER" + name +".csv")

japanese_ask("YOUR_QUESTION_CSV_FILE_NAME")
