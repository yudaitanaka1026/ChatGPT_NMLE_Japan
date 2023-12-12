# ChatGPT API Scripts for NMLE in Japan
## Introduction

These scripts solve the original Japanese text questions and translated questions of the NMLE in Japan using the ChatGPT API. The scripts are provided for:

1. Original Japanese questions
2. Translated English questions
3. With optimized prompts

## Requirements

- OpenAI Python package. To install, use the command: `pip install openai`
- A valid OpenAI API Key
- Input CSV files with questions
- Dedicated folders for input questions and output results

## Scripts

Each task contains two types of code, one for non-comprehension questions and one for comprehension questions.

Setup requires:

- `YOUR_OPENAI_API_KEY`: Your OpenAI API key
- `YOUR_QUESTION_CSV_FILE_NAME`: Name of your question CSV file
- `PATH_TO_QUESTION_FOLDER`: Path to your question CSV file's folder
- `PATH_TO_RESULT_FOLDER`: Path to save the result
- `PATH_TO_PROMPT_CSV_FILE`: Path to the CSV file containing optimized prompts

### 1. Original Japanese questions

This script answers original Japanese questions.

[For Non-comprehension Question](1-1_Japanese_NonComprehension.py)

[For Comprehension Question](1-2_Japanese_Comprehension.py)

### 2.　Translated English questions

This script first translates the original Japanese questions into English and then answers the translated questions.

[For Non-comprehension Question](2-1_English_NonComprehension.py)

[For Comprehension Question](2-2_English_Comprehension.py)

### 3.　With optimized prompts

This script uses optimized prompts for translated questions. 

[For Non-comprehension Question](3-1_Optimized_NonComprehension.py)

[For Comprehension Question](3-2_Optimized_Comprehension.py)

## Prompt and Sample Questions

We provide `OptimizedPrompt.csv`, `SampleQuestion_NonComprehension.csv` and `SampleQuestion_Comprehension.csv` to test these scripts.

- **OptimizedPrompt.csv**: This file contains the optimized prompts that are used in `03_chatgptAPI_optimized.py` for more accurate results.

- **SampleQuestion_NonComprehension.csv**: This file contains sample non-comprehension questions in CSV format.
- **SampleQuestion_Comprehension.csv**: This file contains sample comprehension questions in CSV format. 

Also, you can check all 117th NMLE question and output in our paper's Supplemental Data.

## Citations
If you use the scripts and data provided, please cite our research as follows.

```bibtex
Performance of Generative Pretrained Transformer on the National Medical Licensing Examination in Japan
Yudai Tanaka, Takuto Nakata, Ko Aiga, Takahide Etani, Ryota Muramatsu, Shun Katagiri, Hiroyuki Kawai, Fumiya Higashino, Masahiro Enomoto, Masao Noda, Mitsuhiro Kometani, Masayuki Takamura, Takashi Yoneda, Hiroaki Kakizaki, Akihiro Nomura
medRxiv 2023.04.17.23288603; doi: https://doi.org/10.1101/2023.04.17.23288603
