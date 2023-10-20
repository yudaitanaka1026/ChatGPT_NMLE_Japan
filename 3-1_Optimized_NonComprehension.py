#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Yudai Tanaka

Solve the translated non-comprehension questions of the NMLE in Japan by ChatGPT API with the optimized prompts.

Setup requires:
- `YOUR_OPENAI_API_KEY`: Your OpenAI API key
- `PATH_TO_QUESTION_FOLDER`: Path to your question CSV file's folder
- `PATH_TO_RESULT_FOLDER`: Path to save the result
- `PATH_TO_PROMPT_CSV_FILE`: Path to the CSV file containing optimized prompts

The CSV files should be named "BasicsOfMedicine(essential)", "ClinicalMedicine(essential)", "Comprehension(essential)", "BasicsOfMedicine(general)", "BasicsOfMedicine(specifics)", "ClinicalMedicine(general)", "ClinicalMedicine(specifics)" and "Comprehension" corresponding to the type of question.
"""

# Install the packages
!pip install openai
import openai
import pandas as pd
openai.api_key = "YOUR_OPENAI_API_KEY"

# Load the optimized prompts
df_p = pd.read_csv("PATH_TO_PROMPT_CSV_FILE", header=0, index_col=0)
df_p.head()

tra = [df_p.iloc[0, 0], df_p.iloc[1, 0], df_p.iloc[0, 0], df_p.iloc[0, 0], df_p.iloc[1, 0], df_p.iloc[1, 0]]
ex = [df_p.iloc[0, 1], df_p.iloc[1, 1], df_p.iloc[0, 1], df_p.iloc[0, 1], df_p.iloc[1, 1], df_p.iloc[1, 1]]

# Translation the original Japanese sentences into plain English and answer the translated questions
# For non-comprehension questions
def modified_ask(name, translation, exam):
  df = pd.read_csv("PATH_TO_QUESTION_FOLDER" + name + ".csv", header=0, index_col=0)
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
              "content": str(df.iloc[i, 3])+str(df.iloc[i, 4])
              }],
              temperature=0
              )
    df.iloc[i, 7] = english["choices"][0]["message"]["content"]
    
    res = []
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": exam
             },
             {
                 "role": "user",
              "content": df.iloc[i, 7]
              }],
              temperature=0
              )
    df.iloc[i, 8] = res["choices"][0]["message"]["content"]

  df.to_csv("PATH_TO_RESULT_FOLDER" + name + '.csv')

qtype = ['BasicsOfMedicine(essential)', 'ClinicalMedicine(essential)', 'BasicsOfMedicine(general)', 'BasicsOfMedicine(specifics)', 'ClinicalMedicine(general)', 'ClinicalMedicine(specifics)']

for i in range(-1, len(qtype)):
  modified_ask(qtype[i], tra[i], ex[i])
