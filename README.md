# ChatGPT API Scripts for NMLE in Japan

These scripts solve the original Japanese text questions and translated questions of the NMLE in Japan using the ChatGPT API. The scripts are provided for:

1. Original Japanese questions
2. Translated English questions
3. Optimized processing with tuned prompts

## Requirements

- OpenAI Python package
- A valid OpenAI API Key
- Input CSV files with questions
- Dedicated folders for input questions and output results

## Scripts

### 01_chatgptAPI_japanese.py

This script answers original Japanese questions. Setup requires:

- `OPENAI_API_KEY`: Your OpenAI API key
- `CSV_FILE_NAME`: Name of your question CSV file
- `QUESTION_FOLDER_PATH`: Path to your question CSV file's folder
- `RESULT_FOLDER_PATH`: Path to save the result

[Link to Script](01_chatgptAPI_japanese.py)

### 02_chatgptAPI_english.py

This script first translates the original Japanese questions into English and then answers the translated questions. Setup requires:

- `OPENAI_API_KEY`: Your OpenAI API key
- `CSV_FILE_NAME`: Name of your question CSV file
- `QUESTION_FOLDER_PATH`: Path to your question CSV file's folder
- `RESULT_FOLDER_PATH`: Path to save the result

[Link to Script](02_chatgptAPI_english.py)

### 03_chatgptAPI_optimized.py

This script uses optimized prompts for translated questions. Setup requires:

- `OPENAI_API_KEY`: Your OpenAI API key
- `CSV_FILE_NAME`: Name of your question CSV file
- `QUESTION_FOLDER_PATH`: Path to your question CSV file's folder
- `RESULT_FOLDER_PATH`: Path to save the result
- `PROMPT_CSV_FILE_PATH`: Path to the CSV file containing optimized prompts

[Link to Script](03_chatgptAPI_optimized.py)

## Prompt and Sample Questions

We provide `OptimizedPrompt.csv` and `SampleQuestion.csv` to test these scripts.

- **OptimizedPrompt.csv**: This file contains the optimized prompts that are used in `03_chatgptAPI_optimized.py` for more accurate results.

- **SampleQuestion.csv**: This file contains sample questions in CSV format. Also, you can check all 117th NMLE question and output in our paper's Supplemental Data.