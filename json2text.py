from save import save
import json
import os
from save import save

dir_path = '/Users/bayashihi/Documents/VScode/paper/scrapbox'

def save(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)
        f.close()

with open('scrapbox.json') as f:
    js = json.load(f) # ここですでにtextというjsonが辞書としてよまれている？
    f.close()

cont_list = js['pages']

for a in cont_list:
    # a = cont_list[i] #i番目のdictを取得
    title = a['title']
    cont_pre = a['lines']
    content = '\n'.join(cont_pre)
    
    save(dir_path, title + '.md', content)



# data = json.load(json_open) で、jsonを文字列に
# with open(filename, mode = 'w')as f: f.write(text)