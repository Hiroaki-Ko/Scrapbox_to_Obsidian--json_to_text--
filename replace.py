import re

def replace(text): #テキストを変換してテキストで返す
    text = re.sub(r'\t ', r'- ', text) #箇条書きをつくる
    text = re.sub(r'\[\*\*\* (.*)\](?=\n)', r'## \1', text) #h2
    text = re.sub(r'\[\*\* (.*)\](?=\n)', r'### \1', text) #h3
    text = re.sub(r'\[/ (.*)\](?=\n)', r'*\1*', text) #斜体
    text = re.sub(r'\[\_ (.*)\](?=\n)', r'**\1**', text) #下線ないから太字へ
    text = re.sub(r'\[\* (.*)\](?=\n)', r'**\1**', text) #太字をつくる1
    text = re.sub(r'\[\[(.*)\]\](?=\n)', r'**\1**', text) #太字2
    text = re.sub(r'\[', r'[[', text)
    text = re.sub(r'\]', r']]', text)
    return text